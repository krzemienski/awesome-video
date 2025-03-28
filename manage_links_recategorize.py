#!/usr/bin/env python3
import argparse
import json
import os
import requests
import base64
import openai
import re
import sys
import logging
from urllib.parse import urlparse

try:
    import jsonschema
    from jsonschema import validate
except ImportError:
    print("jsonschema module not found. Please install it via pip install jsonschema")
    sys.exit(1)

# JSON Schema as provided
JSON_SCHEMA = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "$id": "https://raw.githubusercontent.com/matteocrippa/awesome-swift/master/.github/schema.json",
    "type": "object",
    "properties": {
        "title": {"type": "string"},
        "header_contributing": {"type": "string"},
        "header": {"type": "string"},
        "ios_app_link": {"type": "string"},
        "categories": {
            "type": "array",
            "uniqueItems": True,
            "items": {
                "title": "Category Object",
                "description": "A category to group project objects under.",
                "properties": {
                    "title": {
                        "title": "Category Title",
                        "description": "A human-readable identifier for the category.",
                        "type": "string"
                    },
                    "id": {
                        "title": "Category Identifier",
                        "description": "A short identifier designed for programs. It should only contain lowercase alphanumeric characters and a - (dash) for replacing spaces.",
                        "type": "string",
                        "pattern": "^[^A-Z_ ]+$"
                    },
                    "description": {
                        "title": "Category Description",
                        "description": "A description of the category meant to be provided to the user.",
                        "type": "string",
                        "default": ""
                    },
                    "parent": {
                        "title": "Category Parent",
                        "description": "Makes the current category a subcategory of the category with an id that matches this value.",
                        "type": ["string", "null"],
                        "default": None
                    }
                },
                "required": ["title", "id"],
                "additionalProperties": False
            }
        },
        "projects": {
            "type": "array",
            "uniqueItems": True,
            "items": {
                "title": "Project Object",
                "description": "An object that holds all the information for a specific project.",
                "properties": {
                    "title": {
                        "title": "Project Title",
                        "description": "The official title of the project.",
                        "type": "string"
                    },
                    "category": {
                        "title": "Project Category",
                        "description": "The category or list of categories that the project falls under. If it is a list, the categories should be ordered from most to least relevant/applicable to the project.",
                        "type": ["string", "array"],
                        "items": {"type": "string"}
                    },
                    "description": {
                        "title": "Project Description",
                        "description": "A brief 1 sentence summary of the project.",
                        "type": "string"
                    },
                    "homepage": {
                        "title": "Project Homepage",
                        "description": "The URL for the project's homepage.",
                        "type": ["string", "null"],
                        "pattern": "^https?:\\/\\/.*?\\..*$",
                        "default": None
                    },
                    "tags": {
                        "title": "Project Tags",
                        "description": "A place to put any metadata for a project. The items can be any type.",
                        "type": "array",
                        "default": []
                    },
                    "swift": {
                        "title": "Supported Swift Version",
                        "description": "Currently supported swift version",
                        "type": "number"
                    }
                },
                "required": ["title", "category", "homepage"],
                "additionalProperties": False
            }
        }
    },
    "required": ["title", "categories", "projects"],
    "additionalProperties": False
}


def load_json_file(path):
    logging.debug(f"Loading JSON file from: {path}")
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    logging.debug("JSON file loaded successfully.")
    return data


def write_json_file(data, path):
    logging.debug(f"Writing JSON data to: {path}")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    logging.info(f"Updated JSON written to {path}")


def validate_json_structure(data, schema):
    try:
        validate(instance=data, schema=schema)
        logging.debug("JSON validated successfully against the schema.")
        return True
    except jsonschema.exceptions.ValidationError as e:
        logging.error(f"JSON validation error: {e}")
        return False


def fetch_readme(repo_url):
    """
    Fetch the README content for a given GitHub repository URL using the GitHub API.
    Returns the decoded README text or an empty string if not found.
    """
    logging.info(f"Fetching README for: {repo_url}")
    parsed = urlparse(repo_url)
    path_parts = parsed.path.strip("/").split("/")
    if len(path_parts) < 2:
        logging.error(f"Invalid GitHub URL: {repo_url}")
        return ""
    owner, repo = path_parts[0], path_parts[1]
    api_url = f"https://api.github.com/repos/{owner}/{repo}/readme"
    headers = {"Accept": "application/vnd.github.v3+json"}
    response = requests.get(api_url, headers=headers)
    logging.debug(f"GitHub API URL: {api_url} | Status code: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        if "content" in data:
            try:
                content = base64.b64decode(data["content"]).decode("utf-8", errors="replace")
                logging.debug(f"Fetched README content of length {len(content)} for {repo_url}")
                return content
            except Exception as e:
                logging.error(f"Error decoding README for {repo_url}: {e}")
                return ""
        else:
            logging.warning(f"No content found in README for {repo_url}")
            return ""
    else:
        logging.error(f"Failed to fetch README for {repo_url}: HTTP {response.status_code}")
        return ""


def call_openai_for_classification(readme_content, existing_category_ids, openai_model, openai_call_type):
    """
    Use the OpenAI API to generate a refined short summary and suggest category IDs.
    The call type can be "chat" (using ChatCompletion) or "completion" (using text Completion).
    Returns a tuple: (summary, list_of_category_ids)
    """
    prompt = (
        "You are an assistant that helps recategorize GitHub repositories based on their README contents. "
        "Given the following README content, provide a refined short summary (1-2 sentences) describing the project, "
        "and suggest one or more category IDs from the following list: " +
        ", ".join(existing_category_ids) +
        ".\n\n"
        "Return the result in valid JSON format with two keys: \"summary\" and \"categories\". For example: "
        '{"summary": "A refined description.", "categories": ["utilities"]}\n\n'
        "README:\n" + readme_content
    )
    logging.debug(f"OpenAI prompt (first 300 chars): {prompt[:300]}")

    try:
        if openai_call_type.lower() == "chat":
            logging.info(f"Calling OpenAI ChatCompletion with model {openai_model}")
            response = openai.ChatCompletion.create(
                model=openai_model,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.5,
                max_tokens=150,
                n=1
            )
            message = response["choices"][0]["message"]["content"]
        elif openai_call_type.lower() == "completion":
            logging.info(f"Calling OpenAI Completion with model {openai_model}")
            response = openai.Completion.create(
                model=openai_model,
                prompt=prompt,
                temperature=0.5,
                max_tokens=150,
                n=1,
                stop=None,
            )
            message = response["choices"][0]["text"]
        else:
            logging.error(f"Invalid OpenAI call type: {openai_call_type}")
            return "", []
        logging.debug(f"OpenAI response: {message}")
        result = json.loads(message)
        summary = result.get("summary", "").strip()
        categories = result.get("categories", [])
        if isinstance(categories, str):
            categories = [categories.strip()]
        filtered_categories = [cat for cat in categories if cat in existing_category_ids]
        logging.info(f"Summary: {summary} | Categories: {filtered_categories}")
        return summary, filtered_categories
    except Exception as e:
        logging.error(f"Error calling OpenAI API: {e}")
        sentences = re.split(r"\. ", readme_content)
        fallback_summary = sentences[0].strip()
        if fallback_summary and not fallback_summary.endswith("."):
            fallback_summary += "."
        return fallback_summary, []


def recategorize_existing_links(json_data, openai_model, openai_call_type):
    """
    For each project whose homepage is a GitHub URL:
      - Fetch the README.
      - Use OpenAI to get a refined summary and suggested categories.
      - Update the project's description and category accordingly.
    """
    allowed_categories = [cat["id"] for cat in json_data.get("categories", [])]
    logging.debug(f"Allowed categories: {allowed_categories}")
    for project in json_data.get("projects", []):
        homepage = project.get("homepage", "")
        if "github.com" in homepage:
            logging.info(f"Recategorizing project '{project.get('title', 'Unknown')}' at {homepage}...")
            readme_content = fetch_readme(homepage)
            if not readme_content:
                logging.warning(f"Skipping {homepage} due to missing README.")
                continue
            summary, suggested_categories = call_openai_for_classification(
                readme_content, allowed_categories, openai_model, openai_call_type
            )
            chosen_category = (
                suggested_categories[0]
                if suggested_categories
                else project.get("category")
            )
            project["description"] = summary
            project["category"] = chosen_category
            logging.info(f"Updated project '{project.get('title', 'Unknown')}' with category '{chosen_category}'.")
    return json_data


def main():
    parser = argparse.ArgumentParser(
        description="Recategorize existing GitHub repo links in a JSON file using OpenAI."
    )
    parser.add_argument("--json-file", required=True, help="Path to the existing JSON file.")
    parser.add_argument("--output-file", required=True, help="Path to save the updated JSON file.")
    parser.add_argument("--openai-api-key", help="OpenAI API key (or set the OPENAI_API_KEY environment variable).")
    parser.add_argument("--openai-model", default="gpt-3.5-turbo", help="OpenAI model to use.")
    parser.add_argument("--openai-call-type", default="chat", choices=["chat", "completion"],
                        help="Type of OpenAI API call to use: 'chat' for ChatCompletion, 'completion' for text Completion.")
    parser.add_argument("--log-level", default="DEBUG", choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
                        help="Set the logging level.")
    args = parser.parse_args()

    numeric_level = getattr(logging, args.log_level.upper(), logging.DEBUG)
    logging.basicConfig(level=numeric_level,
                        format="%(asctime)s - %(levelname)s - %(message)s")

    openai_api_key = args.openai_api_key or os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        logging.error("OpenAI API key must be provided via --openai-api-key or the OPENAI_API_KEY environment variable.")
        sys.exit(1)
    openai.api_key = openai_api_key

    try:
        json_data = load_json_file(args.json_file)
    except Exception as e:
        logging.error(f"Error loading JSON file {args.json_file}: {e}")
        sys.exit(1)

    if not validate_json_structure(json_data, JSON_SCHEMA):
        logging.error("Initial JSON does not conform to the schema. Exiting.")
        sys.exit(1)

    json_data = recategorize_existing_links(json_data, args.openai_model, args.openai_call_type)

    if not validate_json_structure(json_data, JSON_SCHEMA):
        logging.error("Updated JSON does not conform to the schema. Exiting.")
        sys.exit(1)

    try:
        write_json_file(json_data, args.output_file)
    except Exception as e:
        logging.error(f"Error writing JSON to {args.output_file}: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()