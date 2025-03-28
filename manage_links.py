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

# Set up logging configuration
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('debug.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# -------------------------------------------------------------------
# Hard-coded finite artifact (your categories, header, title, etc.)
HARDCODED_DATA = {
    "title": "Awesome Video",
    "header": "# Awesome Video\n\nProjects are organized into detailed categories with extensive subcategories covering all aspects of video processing, streaming, encoding, and more.",
    "header_contributing": "Please refer to the contribution guidelines before adding new projects.",
    "categories": [
        {
            "name": "Video Players & Playback Libraries",
            "subcategories": [
                {"name": "Web Players"},
                {"name": "Mobile Players"},
                {"name": "Desktop Players"},
                {"name": "Smart TV Players"},
                {"name": "Set-top Box Players"},
                {"name": "Embedded Players"},
                {"name": "Frameworks & UI Components"},
                {"name": "Browser Extensions"}
            ]
        },
        {
            "name": "Video Editing & Processing Tools",
            "subcategories": [
                {"name": "Trimming & Cutting Tools"},
                {"name": "Conversion & Format Tools"},
                {"name": "Repair & Recovery Tools"},
                {"name": "Non-linear Editing Suites"},
                {"name": "Effects & Compositing Tools"},
                {"name": "Color Grading & Correction Tools"},
                {"name": "Subtitle & Caption Tools"},
                {"name": "Batch Processing & Automation"}
            ]
        },
        {
            "name": "Video Encoding, Transcoding & Packaging Tools",
            "subcategories": [
                {"name": "FFmpeg-Based Tools"},
                {"name": "Hardware Accelerated Transcoding"},
                {"name": "Software Transcoding Tools"},
                {"name": "Scripting & Automation Tools"},
                {"name": "Containerization & Packaging Tools"},
                {"name": "Cloud-Based Encoding Solutions"},
                {"name": "Multi-format Packaging Tools"},
                {"name": "Real-Time Encoding Solutions"}
            ]
        },
        {
            "name": "Video Streaming & Distribution Solutions",
            "subcategories": [
                {"name": "Live Streaming Servers"},
                {"name": "VOD Streaming Servers"},
                {"name": "CDN Integration & Distribution"},
                {"name": "RTMP/RTSP/HTTP Protocol Servers"},
                {"name": "Peer-to-Peer Streaming Solutions"},
                {"name": "Multi-CDN Management"},
                {"name": "Edge Computing & Caching Solutions"},
                {"name": "Streaming Analytics & Monitoring"}
            ]
        },
        {
            "name": "Adaptive Streaming & Manifest Tools",
            "subcategories": [
                {"name": "HLS Tools"},
                {"name": "DASH Tools"},
                {"name": "CMAF & fMP4 Packaging"},
                {"name": "HLS Manifest Parsers & Generators"},
                {"name": "DASH Manifest Tools"},
                {"name": "Encryption & DRM for Adaptive Streaming"},
                {"name": "Low-Latency Streaming Tools"},
                {"name": "Adaptive Bitrate Algorithms & Tools"}
            ]
        },
        {
            "name": "Media Analysis, Quality Metrics & AI Tools",
            "subcategories": [
                {"name": "Quality Analysis & Metrics"},
                {"name": "Scene Detection & Segmentation"},
                {"name": "AI & Machine Learning Tools"},
                {"name": "Video Analytics & Benchmarking"},
                {"name": "Audio Analysis & Processing"},
                {"name": "VMAF, PSNR, SSIM Tools"},
                {"name": "Color Science & Histogram Analysis"},
                {"name": "Metadata Extraction & Management"}
            ]
        },
        {
            "name": "Build Tools, Deployment & Utility Libraries",
            "subcategories": [
                {"name": "Docker & Containerization Tools"},
                {"name": "Build Scripts & Automation"},
                {"name": "Command-line Utilities & Wrappers"},
                {"name": "API Libraries & SDKs"},
                {"name": "Performance & Monitoring Tools"},
                {"name": "CI/CD Pipelines for Media"},
                {"name": "Logging & Debugging Tools"},
                {"name": "Infrastructure as Code for Video"}
            ]
        },
        {
            "name": "Standards, Specifications & Industry Resources",
            "subcategories": [
                {"name": "Video Codec Specifications"},
                {"name": "Adaptive Streaming Standards"},
                {"name": "DRM & Content Protection Standards"},
                {"name": "Closed Captioning & Subtitling Standards"},
                {"name": "Industry Forums & Standards Bodies"},
                {"name": "Regulatory & Compliance Resources"},
                {"name": "Best Practices & Guidelines"},
                {"name": "Open Source Licensing & Patents"}
            ]
        },
        {
            "name": "Learning, Tutorials & Documentation",
            "subcategories": [
                {"name": "Video Streaming Tutorials"},
                {"name": "Encoding & Transcoding Guides"},
                {"name": "Player Development Documentation"},
                {"name": "Subtitle & Caption Tutorials"},
                {"name": "Books & Courses"},
                {"name": "Case Studies & Whitepapers"},
                {"name": "Webinars & Conference Talks"},
                {"name": "Community Blogs & Forums"}
            ]
        },
        {
            "name": "Transcoding, Codecs & Hardware Acceleration",
            "subcategories": [
                {"name": "Software Codecs"},
                {"name": "Hardware Codecs & Acceleration"},
                {"name": "Open Source Encoder Projects"},
                {"name": "GPU Transcoding Libraries"},
                {"name": "Benchmarking & Performance Tools for Codecs"},
                {"name": "Comparative Analysis of Codecs"},
                {"name": "Multi-format Transcoding Solutions"},
                {"name": "Next-Generation Codecs (AV1, VVC)"}
            ]
        },
        {
            "name": "DRM, Security & Content Protection",
            "subcategories": [
                {"name": "DRM Solutions & Implementations"},
                {"name": "Encryption Tools for Streaming"},
                {"name": "License Management Systems"},
                {"name": "Widevine, FairPlay, PlayReady Integrations"},
                {"name": "Secure Packaging & Manifest Encryption"},
                {"name": "Content Watermarking & Fingerprinting"},
                {"name": "DRM Testing & Validation Tools"},
                {"name": "Case Studies & Best Practices in DRM"}
            ]
        },
        {
            "name": "Miscellaneous, Experimental & Niche Tools",
            "subcategories": [
                {"name": "Test Content & Sample Streams"},
                {"name": "Experimental Projects & Prototypes"},
                {"name": "Community & Collaboration Platforms"},
                {"name": "Legacy & Obsolete Tools"},
                {"name": "Research Projects & Academic Resources"},
                {"name": "Independent & Hobbyist Projects"},
                {"name": "Cross-Platform Media Tools"},
                {"name": "Specialized Utility Scripts"}
            ]
        }
    ]
}

# -------------------------------------------------------------------
# JSON schema for validation
SCHEMA = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "title": {"type": "string"},
        "header": {"type": "string"},
        "header_contributing": {"type": "string"},
        "categories": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "subcategories": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "name": {"type": "string"}
                            },
                            "required": ["name"]
                        }
                    }
                },
                "required": ["name", "subcategories"]
            }
        },
        "projects": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "title": {"type": "string"},
                    "category": {
                        "oneOf": [
                            {"type": "string"},
                            {
                                "type": "array",
                                "items": {"type": "string"}
                            }
                        ]
                    },
                    "description": {"type": ["string", "null"]},
                    "homepage": {"type": ["string", "null"]},
                    "tags": {
                        "type": "array",
                        "items": {"type": "string"},
                        "default": []
                    }
                },
                "required": ["title", "category", "homepage"],
                "additionalProperties": False
            }
        }
    },
    "required": ["title", "header", "header_contributing", "categories", "projects"]
}

# -------------------------------------------------------------------
# Utility functions

def load_json_file(path):
    logger.debug(f"Loading JSON file from: {path}")
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    logger.debug("JSON file loaded successfully.")
    return data

def write_json_file(data, path):
    logger.debug(f"Writing JSON data to: {path}")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    logger.info(f"Updated JSON written to {path}")

def validate_json_structure(data, schema):
    try:
        validate(instance=data, schema=schema)
        logger.debug("JSON validated successfully against the schema.")
        return True
    except jsonschema.exceptions.ValidationError as e:
        logger.error(f"JSON validation error: {e}")
        return False

def get_allowed_categories(data):
    """
    Returns three lists:
      - allowed main categories,
      - allowed subcategories,
      - combined allowed categories.
    """
    main_categories = []
    subcategories = []
    for cat in data.get("categories", []):
        if "name" in cat:
            main_categories.append(cat["name"])
        for sub in cat.get("subcategories", []):
            if "name" in sub:
                subcategories.append(sub["name"])
    combined = main_categories + subcategories
    logger.debug(f"Allowed main categories: {main_categories}")
    logger.debug(f"Allowed subcategories: {subcategories}")
    return main_categories, subcategories, combined

def fetch_readme(repo_url):
    """
    Fetch the README content for a given GitHub repository URL using the GitHub API.
    Returns the decoded README text or an empty string if not found.
    """
    logger.info(f"Fetching README for: {repo_url}")
    parsed = urlparse(repo_url)
    path_parts = parsed.path.strip("/").split("/")
    if len(path_parts) < 2:
        logger.error(f"Invalid GitHub URL: {repo_url}")
        return ""
    owner, repo = path_parts[0], path_parts[1]
    api_url = f"https://api.github.com/repos/{owner}/{repo}/readme"
    headers = {"Accept": "application/vnd.github.v3+json"}
    response = requests.get(api_url, headers=headers)
    logger.debug(f"GitHub API URL: {api_url} | Status code: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        if "content" in data:
            try:
                content = base64.b64decode(data["content"]).decode("utf-8", errors="replace")
                logger.debug(f"Fetched README content of length {len(content)} for {repo_url}")
                return content
            except Exception as e:
                logger.error(f"Error decoding README for {repo_url}: {e}")
                return ""
        else:
            logger.warning(f"No content found in README for {repo_url}")
            return ""
    else:
        logger.error(f"Failed to fetch README for {repo_url}: HTTP {response.status_code}")
        return ""

# -------------------------------------------------------------------
# Backend wrappers

def call_ollama_completion(prompt, model, ollama_url, temperature=0.5, max_tokens=200):
    """
    Calls the Ollama backend using a configurable URL.
    """
    url = f"{ollama_url}/api/models/{model}/completions"
    payload = {
        "prompt": prompt,
        "temperature": temperature,
        "max_tokens": max_tokens
    }
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            result = response.json()
            return result.get("completion", "")
        else:
            logger.error(f"Ollama API error: HTTP {response.status_code}")
            return ""
    except Exception as e:
        logger.error(f"Error calling Ollama API: {e}")
        return ""

def call_model_for_recategorization(readme_content, allowed_main, allowed_sub, allowed_combined,
                                    model, call_type, backend, ollama_url):
    logger.debug("Calling model for recategorization")
    logger.debug(f"Model: {model}, Backend: {backend}")
    
    prompt = (
        "You are an assistant that helps recategorize GitHub repositories based on their README contents. "
        "Given the following README content, provide a refined summary (1-2 sentences) describing the project. "
        "Then, based on the project's content, suggest the most appropriate main category and a relevant subcategory "
        "from the following lists:\n\n"
        f"Main categories: {', '.join(allowed_main)}\n"
        f"Subcategories: {', '.join(allowed_sub)}\n\n"
        "Format your response as a JSON object with 'summary', 'category', and 'subcategory' fields. "
        "For example: {\"summary\": \"A refined description.\", \"category\": \"Video Streaming & Distribution Solutions\", \"subcategory\": \"Live Streaming Servers\"}.\n\n"
        "README:\n" + readme_content
    )
    logger.debug(f"Prompt (first 300 chars): {prompt[:300]}")
    message = ""
    if backend.lower() == "openai":
        try:
            client = openai.OpenAI()
            if call_type.lower() == "chat":
                logger.info(f"Calling OpenAI ChatCompletion with model {model}")
                response = client.chat.completions.create(
                    model=model,
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant that categorizes GitHub repositories."},
                        {"role": "user", "content": prompt}
                    ]
                )
                message = response.choices[0].message.content
            elif call_type.lower() == "completion":
                logger.info(f"Calling OpenAI Completion with model {model}")
                response = client.completions.create(
                    model=model,
                    prompt=prompt,
                    max_tokens=200,
                    temperature=0.3
                )
                message = response.choices[0].text
            else:
                logger.error(f"Invalid call type: {call_type}")
                return "", "", ""
        except Exception as e:
            logger.error(f"Error calling OpenAI API: {e}")
            sentences = re.split(r"\. ", readme_content)
            fallback_summary = sentences[0].strip()
            if fallback_summary and not fallback_summary.endswith("."):
                fallback_summary += "."
            return fallback_summary, allowed_main[0] if allowed_main else "", ""
    elif backend.lower() == "ollama":
        logger.info(f"Calling Ollama for model {model} at {ollama_url}")
        message = call_ollama_completion(prompt, model, ollama_url, temperature=0.5, max_tokens=200)
        if not message:
            logger.error("Ollama returned an empty response.")
            sentences = re.split(r"\. ", readme_content)
            fallback_summary = sentences[0].strip()
            if fallback_summary and not fallback_summary.endswith("."):
                fallback_summary += "."
            return fallback_summary, allowed_main[0] if allowed_main else "", ""
    else:
        logger.error(f"Invalid backend: {backend}")
        return "", "", ""

    logger.debug(f"Raw response: {message}")
    try:
        result = json.loads(message)
    except Exception as e:
        logger.error(f"Error parsing JSON response: {e}")
        return "", "", ""

    summary = result.get("summary", "").strip()
    main_cat = result.get("category", "").strip()
    sub_cat = result.get("subcategory", "").strip()

    if main_cat not in allowed_main:
        logger.warning(f"Suggested main category '{main_cat}' not allowed. Defaulting.")
        main_cat = allowed_main[0] if allowed_main else ""
    if sub_cat and sub_cat not in allowed_sub:
        logger.warning(f"Suggested subcategory '{sub_cat}' not allowed. Ignoring subcategory.")
        sub_cat = ""

    logger.info(f"Summary: {summary} | Category: {main_cat} | Subcategory: {sub_cat}")
    return summary, main_cat, sub_cat

def extract_repo_name(repo_url):
    """
    Extract the repository name from a GitHub URL.
    """
    parsed = urlparse(repo_url)
    path_parts = parsed.path.strip("/").split("/")
    if len(path_parts) >= 2:
        return path_parts[1]
    return repo_url

# -------------------------------------------------------------------
# Mode functions

def add_new_links(data, repo_file_path, model, call_type, backend, ollama_url):
    logger.debug(f"Starting add_new_links with model={model}, call_type={call_type}, backend={backend}")
    
    try:
        with open(repo_file_path, 'r') as f:
            repo_urls = f.read().splitlines()
    except Exception as e:
        logger.error(f"Error reading repo file: {e}")
        return data

    allowed_main, allowed_sub, allowed_combined = get_allowed_categories(data)
    logger.debug(f"Found {len(allowed_main)} main categories and {len(allowed_sub)} subcategories")

    if "projects" not in data:
        data["projects"] = []
    for repo_url in repo_urls:
        logger.info(f"Processing repo: {repo_url}")
        readme_content = fetch_readme(repo_url)
        if not readme_content:
            logger.warning(f"Skipping {repo_url} due to missing README.")
            continue
        summary, main_cat, sub_cat = call_model_for_recategorization(
            readme_content, allowed_main, allowed_sub, allowed_combined, model, call_type, backend, ollama_url
        )
        category_str = f"{main_cat} – {sub_cat}" if sub_cat else main_cat
        project_exists = False
        for project in data.get("projects", []):
            if project.get("homepage", "").rstrip("/") == repo_url.rstrip("/"):
                logger.info(f"Updating existing project for {repo_url}.")
                project["description"] = summary
                project["category"] = category_str
                project_exists = True
                break
        if not project_exists:
            project_title = extract_repo_name(repo_url)
            new_project = {
                "title": project_title,
                "category": category_str,
                "description": summary,
                "homepage": repo_url,
                "tags": []
            }
            data["projects"].append(new_project)
            logger.info(f"Added new project: {project_title}")
    return data

def recategorize_projects(data, model, call_type, backend, ollama_url):
    """
    In recategorize mode:
      - For each project with a GitHub URL in its homepage, fetch its README and use the selected backend
        to get a refined summary, main category, and subcategory.
      - Update the project's description and category (formatted as "Main – Subcategory" if applicable).
    """
    allowed_main, allowed_sub, allowed_combined = get_allowed_categories(data)
    if "projects" not in data:
        logger.warning("No projects found to recategorize.")
        return data
    for project in data.get("projects", []):
        homepage = project.get("homepage", "")
        if "github.com" not in homepage:
            continue
        logger.info(f"Recategorizing project '{project.get('title', 'Unknown')}' at {homepage}...")
        readme_content = fetch_readme(homepage)
        if not readme_content:
            logger.warning(f"Skipping {homepage} due to missing README.")
            continue
        summary, main_cat, sub_cat = call_model_for_recategorization(
            readme_content, allowed_main, allowed_sub, allowed_combined, model, call_type, backend, ollama_url
        )
        category_str = f"{main_cat} – {sub_cat}" if sub_cat else main_cat
        project["description"] = summary
        project["category"] = category_str
        logger.info(f"Updated project '{project.get('title', 'Unknown')}' with category '{category_str}'.")
    return data

# -------------------------------------------------------------------
# Main

def main():
    parser = argparse.ArgumentParser(
        description="Manage and categorize GitHub repos using a finite, hard-coded categories artifact. "
                    "Use mode 'add' to add new repo URLs or 'recategorize' to update existing projects."
    )
    parser.add_argument("--mode", required=True, choices=["add", "recategorize"],
                        help="Operation mode: 'add' to add new repo URLs, 'recategorize' to update existing projects.")
    parser.add_argument("--json-file", required=True, help="Path to the existing JSON file.")
    parser.add_argument("--output-file", required=True, help="Path to save the updated JSON file.")
    parser.add_argument("--repo-file", help="Path to the text file containing GitHub repo URLs (required for add mode).")
    parser.add_argument("--backend", default="openai", choices=["openai", "ollama"],
                        help="Backend to use for completions (default: openai).")
    parser.add_argument("--model", default="gpt-3.5-turbo",
                        help="Model to use (for OpenAI or Ollama). For Ollama, ensure the model is available at the endpoint.")
    parser.add_argument("--call-type", default="chat", choices=["chat", "completion"],
                        help="Type of API call to use (for OpenAI; ignored for Ollama).")
    parser.add_argument("--ollama-url", default="http://localhost:11434",
                        help="Base URL for the Ollama backend (default: http://localhost:11434).")
    parser.add_argument("--openai-api-key", help="OpenAI API key (or set the OPENAI_API_KEY environment variable).")
    parser.add_argument("--log-level", default="DEBUG", choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
                        help="Set the logging level.")
    args = parser.parse_args()

    numeric_level = getattr(logging, args.log_level.upper(), logging.DEBUG)
    logging.basicConfig(level=numeric_level, format="%(asctime)s - %(levelname)s - %(message)s")

    if args.backend.lower() == "openai":
        openai_api_key = args.openai_api_key or os.getenv("OPENAI_API_KEY")
        if not openai_api_key:
            logger.error("OpenAI API key must be provided via --openai-api-key or the OPENAI_API_KEY environment variable.")
            sys.exit(1)
        openai.api_key = openai_api_key

    try:
        data = load_json_file(args.json_file)
    except Exception as e:
        logger.error(f"Error loading JSON file {args.json_file}: {e}")
        sys.exit(1)

    # Override title, header, and categories with the hard-coded artifact.
    data["title"] = HARDCODED_DATA["title"]
    data["header"] = HARDCODED_DATA["header"]
    data["header_contributing"] = HARDCODED_DATA["header_contributing"]
    data["categories"] = HARDCODED_DATA["categories"]

    if not validate_json_structure(data, SCHEMA):
        logger.error("Initial JSON does not conform to the schema. Exiting.")
        sys.exit(1)

    if args.mode == "add":
        if not args.repo_file:
            logger.error("In 'add' mode, --repo-file must be provided.")
            sys.exit(1)
        data = add_new_links(data, args.repo_file, args.model, args.call_type, args.backend, args.ollama_url)
    else:
        data = recategorize_projects(data, args.model, args.call_type, args.backend, args.ollama_url)

    if not validate_json_structure(data, SCHEMA):
        logger.error("Updated JSON does not conform to the schema. Exiting.")
        sys.exit(1)

    try:
        write_json_file(data, args.output_file)
    except Exception as e:
        logger.error(f"Error writing JSON to {args.output_file}: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
			
# Usage Examples

# Add Mode using OpenAI (default):

# python manage_links.py \
#   --mode=add \
#   --json-file=contents.json \
#   --repo-file=repo_urls.txt \
#   --output-file=updated_contents.json \
#   --backend=openai \
#   --model=gpt-3.5-turbo \
#   --call-type=chat \
#   --openai-api-key=sk-XYZ \
#   --log-level=DEBUG

# Recategorize Mode using Ollama with a custom URL:

# python manage_links.py \
#   --mode=recategorize \
#   --json-file=updated_contents.json \
#   --output-file=recategorized_contents.json \
#   --backend=ollama \
#   --model=your-ollama-model-name \
#   --call-type=chat \
#   --ollama-url=http://your-custom-ollama-url:port \
#   --log-level=DEBUG

# Explanation
# 	1.	Backend Selectio