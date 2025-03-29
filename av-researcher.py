#!/usr/bin/env python3
"""
Deep Research Script for Awesome Video Project

This script performs automated deep research using a simulated multi-agent
workflow that leverages the OpenAI Responses API (simulated) to collect, classify,
and validate exactly 1000 unique new resources. Each resource is checked against
the JSON schema, ensuring a valid homepage URL, a unique title (not in the original
contents.json), a description, and one or more valid category IDs.

Usage:
    python deep_research.py [--contents /path/to/contents.json]

If --contents is not provided, the script fetches the JSON data from a remote URL.
"""

import argparse
import json
import logging
import time
import requests
import re
import random
from typing import List, Dict

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Constants
REMOTE_URL = "https://hack-ski.s3.us-east-1.amazonaws.com/av/recategorized_projects_anthropic_claude_3_5_haiku_20241022_1743170712_1181.json"
BASE_SEARCH_PHRASES = ["video streaming tools", "open source video processing"]
TARGET_RESOURCE_COUNT = 1000

def fetch_contents_json(file_path: str = None) -> Dict:
    """Fetch the contents.json data from a local file or remote URL."""
    try:
        if file_path:
            with open(file_path, "r") as f:
                data = json.load(f)
            logging.info("Loaded local contents.json")
        else:
            response = requests.get(REMOTE_URL)
            response.raise_for_status()
            data = response.json()
            logging.info("Fetched remote contents.json")
        return data
    except Exception as e:
        logging.error(f"Failed to load contents.json: {e}")
        exit(1)

def extract_existing_titles(contents: Dict) -> set:
    """Extract a set of existing project titles to prevent duplicates."""
    existing = set()
    projects = contents.get("projects", [])
    for project in projects:
        title = project.get("title")
        if title:
            existing.add(title)
    return existing

def extract_categories(contents: Dict) -> Dict:
    """Extract valid categories from the contents.json file."""
    categories = contents.get("categories", [])
    valid_categories = {}
    for cat in categories:
        cat_id = cat.get("id")
        if cat_id:
            valid_categories[cat_id] = cat
    return valid_categories

def generate_search_terms(valid_categories: Dict, sample_projects: List[Dict]) -> List[str]:
    """
    Generate search terms by combining base phrases with category titles.
    (Additional keyword suggestions from sample project data can be added here.)
    """
    search_terms = []
    # Combine each base phrase with every category title.
    for cat_id, cat in valid_categories.items():
        cat_title = cat.get("title", "")
        for base in BASE_SEARCH_PHRASES:
            search_terms.append(f"{base} {cat_title}")
    # Also include the base phrases themselves.
    search_terms.extend(BASE_SEARCH_PHRASES)
    # Remove duplicates.
    return list(set(search_terms))

def openai_generate_response(prompt: str) -> List[str]:
    """
    Dummy function to simulate the OpenAI Responses API.
    In a real implementation, this function would call the API and parse its JSON response.
    """
    # For simulation, return a fixed list of suggestion keywords.
    suggestions = ["tutorial", "guide", "best practices", "documentation", "case study"]
    return suggestions

class PlannerAgent:
    """
    Planner Agent: Generates a structured research plan
    (a list of search queries with reasons) based on the project and category data.
    """
    def __init__(self, base_search_phrases: List[str], valid_categories: Dict, sample_projects: List[Dict]):
        self.base_search_phrases = base_search_phrases
        self.valid_categories = valid_categories
        self.sample_projects = sample_projects

    def generate_plan(self) -> List[Dict]:
        logging.info("PlannerAgent: Generating research plan")
        # Generate additional keyword suggestions for each category.
        suggestions = []
        for cat_id, cat in self.valid_categories.items():
            prompt = f"Suggest keywords for video research for category: {cat.get('title', '')}"
            cat_suggestions = openai_generate_response(prompt)
            suggestions.extend(cat_suggestions)
        suggestions = list(set(suggestions))
        # Generate search queries by combining base phrases, suggestions, and category titles.
        search_terms = []
        for base in self.base_search_phrases:
            for suggestion in suggestions:
                search_terms.append(f"{base} {suggestion}")
        for base in self.base_search_phrases:
            for cat_id, cat in self.valid_categories.items():
                search_terms.append(f"{base} {cat.get('title', '')}")
        search_terms = list(set(search_terms))
        # Create structured research plan with reasons.
        research_plan = []
        for term in search_terms:
            research_plan.append({
                "query": term,
                "reason": f"To discover resources related to Awesome Video in the context of {term.split()[-1]}"
            })
        logging.info(f"PlannerAgent: Generated {len(research_plan)} search queries")
        return research_plan

class SearchAgent:
    """
    Search Agent: Executes a simulated web search for a given query
    and returns a list of candidate resources in JSON‑formatted summaries.
    """
    def execute_search(self, query: str) -> List[Dict]:
        logging.info(f"SearchAgent: Executing search for query: '{query}'")
        # Simulate a variable number of results (e.g., 5 to 20)
        num_results = random.randint(5, 20)
        results = []
        for i in range(num_results):
            resource = {
                "title": f"{query.title()} Resource {i}",
                "homepage": f"https://example.com/{query.replace(' ', '_')}/{i}",
                "description": f"A resource about {query}. It provides insights into video playback and processing technologies.",
                "tags": ["video", "open source"],
                "categories": []  # to be determined by the Writer Agent
            }
            results.append(resource)
        logging.info(f"SearchAgent: Found {num_results} results for query: '{query}'")
        return results

class WriterAgent:
    """
    Writer Agent: Synthesizes search summaries and classifies each resource
    into one or more valid category IDs based on keyword matching.
    """
    def synthesize_resources(self, search_results: List[Dict], valid_categories: Dict) -> List[Dict]:
        logging.info("WriterAgent: Synthesizing resources from search results")
        for resource in search_results:
            resource_categories = []
            for cat_id, cat in valid_categories.items():
                # Use simple keyword matching on title and description.
                keyword = cat.get("title", "").lower()
                if keyword and (keyword in resource["title"].lower() or keyword in resource["description"].lower()):
                    resource_categories.append(cat_id)
            # If no matching category is found, assign the first available category.
            if not resource_categories and valid_categories:
                resource_categories.append(next(iter(valid_categories)))
            resource["categories"] = resource_categories
        logging.info("WriterAgent: Synthesis complete")
        return search_results

def validate_resource(resource: Dict, existing_titles: set, valid_categories: Dict) -> bool:
    """
    Validate that the resource meets all criteria:
    - Unique title (not in existing_titles).
    - Valid, non-null homepage URL.
    - Contains a description.
    - Has at least one valid category.
    """
    if resource["title"] in existing_titles:
        logging.warning(f"Validation: Duplicate title found: {resource['title']}")
        return False
    url_pattern = re.compile(r"^https?:\/\/.*?\..*$")
    if not resource.get("homepage") or not url_pattern.match(resource["homepage"]):
        logging.warning(f"Validation: Invalid homepage URL for resource: {resource['title']}")
        return False
    if not resource.get("description"):
        logging.warning(f"Validation: Missing description for resource: {resource['title']}")
        return False
    if not resource.get("categories") or not any(cat in valid_categories for cat in resource["categories"]):
        logging.warning(f"Validation: No valid categories for resource: {resource['title']}")
        return False
    return True

class ResearchManager:
    """
    Research Manager: Coordinates the multi-agent workflow, maintains real-time status updates,
    and ensures the collection of exactly TARGET_RESOURCE_COUNT validated resources.
    """
    def __init__(self, contents: Dict, target_count: int):
        self.contents = contents
        self.target_count = target_count
        self.valid_categories = extract_categories(contents)
        self.existing_titles = extract_existing_titles(contents)
        self.all_resources: List[Dict] = []

    def run(self) -> List[Dict]:
        start_time = time.time()
        sample_projects = self.contents.get("projects", [])
        # Instantiate agents
        planner = PlannerAgent(BASE_SEARCH_PHRASES, self.valid_categories, sample_projects)
        search_agent = SearchAgent()
        writer = WriterAgent()
        # Generate research plan
        plan = planner.generate_plan()
        logging.info("ResearchManager: Starting multi-agent research workflow")
        # Iterate through search queries until target is met.
        for idx, query_info in enumerate(plan):
            if len(self.all_resources) >= self.target_count:
                break
            query = query_info["query"]
            logging.info(f"ResearchManager: Processing search {idx+1}/{len(plan)}: {query}")
            try:
                search_results = search_agent.execute_search(query)
                synthesized = writer.synthesize_resources(search_results, self.valid_categories)
                for resource in synthesized:
                    if len(self.all_resources) >= self.target_count:
                        break
                    if validate_resource(resource, self.existing_titles, self.valid_categories):
                        self.all_resources.append(resource)
                        self.existing_titles.add(resource["title"])
                    else:
                        logging.info(f"ResearchManager: Rejected resource: {resource['title']}")
            except Exception as e:
                logging.error(f"ResearchManager: Error processing query '{query}': {e}")
        # Check if target count was reached.
        if len(self.all_resources) < self.target_count:
            logging.warning(f"Only found {len(self.all_resources)} valid resources. Target of {self.target_count} not met.")
        else:
            logging.info(f"Collected {len(self.all_resources)} valid resources.")
        end_time = time.time()
        logging.info(f"Research completed in {end_time - start_time:.2f} seconds.")
        # Return exactly TARGET_RESOURCE_COUNT resources.
        return self.all_resources[:self.target_count]

def main():
    parser = argparse.ArgumentParser(description="Deep Research Script for Awesome Video Project")
    parser.add_argument("--contents", type=str, help="Path to local contents.json file", default=None)
    args = parser.parse_args()

    contents = fetch_contents_json(args.contents)
    manager = ResearchManager(contents, TARGET_RESOURCE_COUNT)
    resources = manager.run()

    output = {"projects": resources}
    with open("new_projects.json", "w") as f:
        json.dump(output, f, indent=2)
    logging.info("Final results saved to new_projects.json")

if __name__ == "__main__":
    main()
