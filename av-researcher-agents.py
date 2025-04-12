#!/usr/bin/env python3
"""
Awesome Video Streaming & Encoding Researcher

This script uses the OpenAI Agents SDK to find new resources and generate
project ideas related to video streaming, encoding, and processing for developers.
"""

import argparse
import asyncio
import datetime
import json
import logging
import os
import random
import sys
import time
import traceback
import textwrap
from typing import Dict, List, Tuple, Any, Optional, Set, Union

# Basic packages that should be installed by default
import requests

# Try to import tqdm (not critical for functionality)
try:
    from tqdm import tqdm
    TQDM_AVAILABLE = True
except ImportError:
    TQDM_AVAILABLE = False
    print("Warning: tqdm package not found. Progress bars will not be displayed.")

# Import the Agents SDK
try:
    from agents import Agent, Runner, Tool, RunResult, WebSearchTool, tool
    # Note: ToolOutput might not exist in the current version of the package
    AGENTS_SDK_AVAILABLE = True
    print("Successfully imported openai-agents SDK")
except ImportError as e:
    AGENTS_SDK_AVAILABLE = False
    print(f"Error importing openai-agents SDK: {e}")
    print("This script requires the OpenAI Agents SDK.")
    print("To install: pip install openai-agents")
    print("\nTrying alternative import paths...")
    try:
        import sys
        user_site_packages = '/Users/nick/Library/Python/3.12/lib/python/site-packages'
        if user_site_packages not in sys.path:
            sys.path.append(user_site_packages)
            print(f"Added {user_site_packages} to sys.path")
        from agents import Agent, Runner, Tool, RunResult, WebSearchTool, tool
        AGENTS_SDK_AVAILABLE = True
        print("Successfully imported openai-agents SDK from user site-packages")
    except ImportError as e2:
        print(f"Alternative import failed: {e2}")
        sys.exit(1)

# Import OpenAI SDK for agents
from openai import OpenAI

# Constants and configurations
DEFAULT_CACHE_DIR = ".cache"
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
JSON_INDENT = 2

# Schema definitions for validation
RESOURCE_SCHEMA = {
    "type": "object",
    "properties": {
        "title": {"type": "string"},
        "description": {"type": "string"},
        "url": {"type": "string", "format": "uri"},
        "category": {"type": "string"},
        "tags": {"type": "array", "items": {"type": "string"}}
    },
    "required": ["title", "description", "url", "category"]
}

PROJECT_IDEA_SCHEMA = {
    "type": "object",
    "properties": {
        "title": {"type": "string"},
        "description": {"type": "string"},
        "category": {"type": "string"},
        "tags": {"type": "array", "items": {"type": "string"}}
    },
    "required": ["title", "description", "category"]
}


def setup_logging(log_level=logging.INFO, log_file="research.log"):
    """Set up logging configuration."""
    # Create formatter
    formatter = logging.Formatter(LOG_FORMAT)

    # Setup console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # Setup file handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)

    # Configure root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(log_level)

    # Remove existing handlers to avoid duplicate logs
    for handler in root_logger.handlers[:]:
        root_logger.removeHandler(handler)

    # Add handlers
    root_logger.addHandler(console_handler)
    root_logger.addHandler(file_handler)

    # Create a logger for this module
    logger = logging.getLogger(__name__)
    logger.info(f"Logging initialized at level {logging.getLevelName(log_level)}")

    return logger


async def fetch_remote_json(url):
    """Fetch and parse a JSON file from a remote URL."""
    logging.info(f"Fetching remote JSON from {url}")
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        logging.info(f"Successfully fetched remote JSON from {url}")
        return data
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching remote JSON from {url}: {e}")
        raise
    except json.JSONDecodeError as e:
        logging.error(f"Error parsing remote JSON from {url}: {e}")
        raise
    except Exception as e:
        logging.error(f"Unexpected error fetching remote JSON from {url}: {e}")
        raise


async def load_contents(filepath_or_url):
    """Load contents from a local JSON file or remote URL and analyze the category structure."""
    logging.info(f"Loading contents from {filepath_or_url}")
    print(f"\n📂 LOADING CONTENTS FROM: {filepath_or_url}")

    # Check if it's a URL
    if filepath_or_url.startswith(('http://', 'https://')):
        data = await fetch_remote_json(filepath_or_url)
    else:
        # Local file
        try:
            with open(filepath_or_url, 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            logging.error(f"Contents file not found: {filepath_or_url}")
            raise
        except json.JSONDecodeError as e:
            logging.error(f"Error parsing contents file: {filepath_or_url}: {e}")
            raise
        except Exception as e:
            logging.error(f"Unexpected error loading contents file: {filepath_or_url}: {e}")
            raise

    # Process the data - handle hierarchical category structure
    categories = data.get("categories", [])

    # Save full category data for analysis
    categories_data = {}

    # Handle case where "categories" contains category objects with "title" field
    if categories and isinstance(categories[0], dict) and "title" in categories[0]:
        print("📊 ANALYZING HIERARCHICAL CATEGORY STRUCTURE...")
        # Extract category names
        category_names = []
        category_mapping = {}
        parent_child_relationships = {}

        for category in categories:
            if isinstance(category, dict) and "id" in category:
                cat_id = category.get("id")
                cat_title = category.get("title")
                cat_parent = category.get("parent", None)

                category_names.append(cat_id)
                category_mapping[cat_id] = cat_title
                categories_data[cat_id] = {
                    "id": cat_id,
                    "title": cat_title,
                    "parent": cat_parent,
                    "children": [],
                    "description": category.get("description", ""),
                    "related": category.get("related", [])
                }

                # Track parent-child relationships
                if cat_parent:
                    if cat_parent not in parent_child_relationships:
                        parent_child_relationships[cat_parent] = []
                    parent_child_relationships[cat_parent].append(cat_id)

                logging.debug(f"Category: {cat_title} (ID: {cat_id}, Parent: {cat_parent})")

        # Set children for each category
        for parent_id, children in parent_child_relationships.items():
            if parent_id in categories_data:
                categories_data[parent_id]["children"] = children
                print(f"  • Category '{category_mapping.get(parent_id, parent_id)}' has {len(children)} subcategories")
                for child in children:
                    print(f"    - {category_mapping.get(child, child)}")

        # If we're using a hierarchical structure, update the data structure
        if "categories" in data and all(isinstance(c, dict) for c in data.get("categories", [])):
            logging.info("Converting hierarchical category structure to flat structure")

            # Create a new structured data format
            restructured_data = {
                "categories": category_names,
                "_categories_data": categories_data  # Keep full category data
            }

            # Initialize empty lists for each category
            for cat_id in category_names:
                restructured_data[cat_id] = []

            # Add all items with their categories
            all_items = data.get("items", []) or data.get("projects", [])
            if all_items:
                logging.info(f"Processing {len(all_items)} items")
                for item in all_items:
                    if "category" in item:
                        cat_id = item["category"]
                        if cat_id in restructured_data:
                            restructured_data[cat_id].append(item)
                    elif "categories" in item and isinstance(item["categories"], list):
                        # Handle case where item has multiple categories
                        for cat_id in item["categories"]:
                            if cat_id in restructured_data:
                                item_copy = item.copy()
                                restructured_data[cat_id].append(item_copy)

            data = restructured_data
    else:
        # Handle flat structure (if categories is just a list of strings)
        # Create a basic category data structure
        for cat in categories:
            categories_data[cat] = {
                "id": cat,
                "title": cat,
                "parent": None,
                "children": [],
                "description": "",
                "related": []
            }

        # Add categories_data to the main data structure
        data["_categories_data"] = categories_data

    # Log the structure of the data
    categories = data.get("categories", [])
    logging.info(f"Loaded {len(categories)} categories from {filepath_or_url}")
    for category in categories:
        items_count = len(data.get(category, []))
        logging.info(f"  - Category '{category}': {items_count} items")

    # Analyze category structure further - identify relationships, popular categories, etc.
    await analyze_category_structure(data)

    return data


async def analyze_category_structure(data):
    """Analyze the category structure to understand relationships and provide insights."""
    print(f"\n📊 ANALYZING CONTENT STRUCTURE...")

    categories = data.get("categories", [])
    categories_data = data.get("_categories_data", {})

    # Skip if no categories
    if not categories:
        logging.warning("No categories found to analyze")
        return

    # Count items in each category
    category_counts = {}
    total_items = 0

    for category in categories:
        items = data.get(category, [])
        count = len(items)
        category_counts[category] = count
        total_items += count

    # Sort categories by item count
    sorted_categories = sorted(category_counts.items(), key=lambda x: x[1], reverse=True)

    # Find top-level categories (those with no parent)
    top_level_categories = []
    for cat_id, cat_data in categories_data.items():
        if not cat_data.get("parent"):
            top_level_categories.append(cat_id)

    # Log insights
    logging.info(f"CONTENT ANALYSIS: Found {len(categories)} categories with {total_items} total items")
    logging.info(f"CONTENT ANALYSIS: Top-level categories: {len(top_level_categories)}")

    if sorted_categories:
        top_5 = sorted_categories[:5]
        bottom_5 = sorted_categories[-5:] if len(sorted_categories) >= 5 else []

        print(f"  • Total categories: {len(categories)}")
        print(f"  • Total items: {total_items}")
        print(f"  • Top-level categories: {len(top_level_categories)}")

        print("\n  📈 TOP 5 MOST POPULATED CATEGORIES:")
        for cat, count in top_5:
            cat_title = categories_data.get(cat, {}).get("title", cat)
            print(f"    • {cat_title} ({cat}): {count} items")

        if bottom_5:
            print("\n  📉 LEAST POPULATED CATEGORIES:")
            for cat, count in bottom_5:
                cat_title = categories_data.get(cat, {}).get("title", cat)
                print(f"    • {cat_title} ({cat}): {count} items")

    return


async def generate_optimized_search_terms(category, category_data, existing_data, openai_client=None):
    """Generate optimized search terms based on category data and existing resources."""
    logging.info(f"Generating optimized search terms for category '{category}'")
    print(f"\n🔍 GENERATING SEARCH TERMS FOR '{category}'...")

    # Extract relevant information about the category
    cat_info = category_data.get("_categories_data", {}).get(category, {})
    cat_title = cat_info.get("title", category)
    cat_description = cat_info.get("description", "")
    related_categories = cat_info.get("related", [])
    parent_category = cat_info.get("parent", None)
    child_categories = cat_info.get("children", [])

    # Sample existing items in this category
    category_items = []
    for item in existing_data:
        if item.get("category") == category:
            category_items.append(item)

    # Limit to at most 5 samples
    sample_items = category_items[:5] if len(category_items) > 5 else category_items

    # Prepare information for OpenAI prompt
    category_info = {
        "id": category,
        "title": cat_title,
        "description": cat_description,
        "parent": parent_category,
        "children": child_categories,
        "related": related_categories
    }

    try:
        # Create a search agent specifically for term generation
        term_generator = Agent(
            name="Search Term Generator",
            instructions=f"""
            You are a Search Term Generator specializing in creating effective search terms for finding
            resources related to video streaming and encoding developer tools.

            Your task is to generate search terms that will help find valuable, specific resources
            in a given category. Your search terms should be diverse, specific, and effective.
            """
        )

        # Create the prompt
        prompt = f"""
        I need to generate effective search terms for finding resources in the '{cat_title}' category
        of a video streaming and encoding developer tools resource collection.

        CATEGORY INFORMATION:
        - ID: {category}
        - Title: {cat_title}
        - Description: {cat_description}
        - Parent category: {parent_category}
        - Child categories: {child_categories}
        - Related categories: {related_categories}

        EXISTING RESOURCES IN THIS CATEGORY (SAMPLE):
        {json.dumps(sample_items, indent=2)}

        Based on this information, please generate 5-10 search terms that would be most effective for finding:
        1. Specific GitHub repositories with tools or libraries
        2. Official documentation pages
        3. Tutorial websites or blog posts
        4. Conference videos or technical presentations
        5. Specialized tools or software

        The search terms should be diverse, covering different aspects of the category.
        DO NOT include generic terms that would return mostly search listings or generic pages.

        IMPORTANT: Return ONLY a JSON array of strings with your suggested search terms. Do not include any explanation.
        """

        # Run the agent
        result = await Runner.run(term_generator, prompt)
        json_text = result.final_output

        # Try to parse JSON array or extract it if needed
        if not json_text.strip().startswith('['):
            import re
            json_pattern = r'(\[[\s\S]*\])'
            matches = re.search(json_pattern, json_text)
            if matches:
                json_text = matches.group(1)

        search_terms = json.loads(json_text)

        # Log the generated terms
        logging.info(f"Generated {len(search_terms)} search terms for '{category}'")
        print(f"  ✅ GENERATED {len(search_terms)} SEARCH TERMS:")
        for i, term in enumerate(search_terms, 1):
            print(f"    {i}. {term}")

        return search_terms

    except Exception as e:
        logging.error(f"Error generating search terms for '{category}': {e}")
        print(f"  ❌ ERROR: Could not generate optimized search terms: {e}")

        # Fallback to basic search terms
        basic_terms = [
            f"best {cat_title} streaming tools",
            f"{cat_title} encoding github repositories",
            f"{cat_title} streaming API tutorials",
            f"{cat_title} video codec software",
            f"advanced {cat_title} streaming techniques",
            f"{cat_title} video encoding libraries"
        ]

        print(f"  ⚠️ USING FALLBACK SEARCH TERMS:")
        for i, term in enumerate(basic_terms, 1):
            print(f"    {i}. {term}")

        return basic_terms


class PlannerAgent:
    """Agent that creates research plans and coordinates the research process."""

    def __init__(self):
        self.agent = Agent(
            name="Research Planner",
            instructions="""
            You are a Research Planner specializing in video streaming and encoding developer tools.
            Your task is to analyze existing data and create a structured research plan that will guide
            the search for new, valuable resources and project ideas.

            The plan should include:
            1. Priority categories to focus on - diverse selection covering different aspects
            2. Specific search terms for each category
            3. Types of resources to look for
            4. Criteria for evaluating resources
            5. Ideas for generating new projects
            """
        )

    async def create_plan(self, contents_data):
        """Create a research plan based on the contents data."""
        # Extract categories and sample existing data
        categories = contents_data.get("categories", [])
        categories_data = contents_data.get("_categories_data", {})

        # Get a list of all categories with their titles for better context
        category_info = []
        for cat_id in categories:
            cat_data = categories_data.get(cat_id, {})
            title = cat_data.get("title", cat_id)
            description = cat_data.get("description", "")
            parent = cat_data.get("parent", None)
            children = cat_data.get("children", [])
            category_info.append({
                "id": cat_id,
                "title": title,
                "description": description,
                "parent": parent,
                "children": children
            })

        existing_data = []
        for category in categories:
            category_items = contents_data.get(category, [])
            for item in category_items:
                item_with_category = item.copy()
                item_with_category["category"] = category
                existing_data.append(item_with_category)

        # Create a sample of existing data for context
        sample_data = existing_data[:5] if len(existing_data) > 5 else existing_data

        prompt = f"""
        I need to create a research plan to find new resources and generate project ideas
        for video streaming and encoding developer tools. Here's what I already have:

        Category Structure: {json.dumps(category_info, indent=2)}

        Existing data sample: {json.dumps(sample_data, indent=2)}

        Based on this information, please create a detailed research plan that includes:
        1. Priority categories to focus on (choose 8-12 diverse categories across different areas)
        2. Key search terms to use for each category (2-3 terms per category)
        3. Types of resources to look for
        4. Criteria for evaluating resources
        5. A structured approach to generating new project ideas

        IMPORTANT: Select a diverse range of categories - include some popular ones, some niche ones,
        and make sure to cover different aspects of video streaming and encoding developer tools. Try to include both
        technical and creative categories.

        Return your plan as a structured JSON format with the following keys:
        - priority_categories (array of category IDs from the provided category structure)
        - search_terms (object with category IDs as keys and arrays of search terms as values)
        - resource_types (array of resource type strings)
        - evaluation_criteria (array of criteria strings)
        - project_idea_generation (array of approaches)
        """

        result = await Runner.run(self.agent, prompt)

        # Extract JSON from the response
        try:
            # Find JSON in the response
            json_text = result.final_output
            # Find JSON-like structure if it's not directly parseable
            if not json_text.strip().startswith('{'):
                import re
                json_pattern = r'(\{[\s\S]*\})'
                matches = re.search(json_pattern, json_text)
                if matches:
                    json_text = matches.group(1)

            research_plan = json.loads(json_text)
            logging.info("Successfully created research plan")
            return research_plan
        except Exception as e:
            logging.error(f"Error parsing research plan: {e}")
            logging.debug(f"Raw plan output: {result.final_output}")
            raise Exception(f"Failed to create a valid research plan: {e}")


class SearchAgent:
    """Agent that searches for resources using web search capabilities."""

    def __init__(self):
        self.agent = Agent(
            name="Resource Searcher",
            instructions="""
            You are a Resource Searcher specializing in finding high-quality resources related to video streaming and encoding developer tools.

            Your task is to search for resources related to specific search terms and categorize them properly.
            Your results MUST ONLY include SPECIFIC resources with DIRECT URLs to valuable content.

            NEVER include:
            - Generic search result pages (like Google search links)
            - Search result listings
            - Vague "collections" without specific content

            ONLY include:
            - GitHub repositories with specific tools or projects
            - Official documentation or websites for tools
            - Specific tutorials or guides on reputable sites
            - Conference videos, blog posts, or technical articles
            - Software download pages for specific tools

            Each resource you find should include:
            1. A clear, concise title
            2. A detailed description explaining what the resource offers
            3. The URL of the resource (must be a DIRECT link to the content, not a search page)
            4. The category it belongs to
            5. Relevant tags (up to 5)

            YOUR MOST IMPORTANT TASK IS TO FIND DIRECT URLs TO SPECIFIC RESOURCES, NOT SEARCH PAGES.
            """,
            tools=[WebSearchTool()]
        )

    async def search(self, search_term, category, timeout=60, max_retries=3):
        """Search for resources related to the provided search term and category."""
        logging.info(f"Searching for: '{search_term}' in category '{category}'")
        print(f"\n🔍 SEARCHING: '{search_term}' in category '{category}'")

        for attempt in range(1, max_retries + 1):
            try:
                print(f"  Attempt {attempt}/{max_retries}...")

                prompt = f"""
                Search for valuable resources related to '{search_term}' in the category '{category}'.

                Find 3-5 high-quality resources that would be valuable for people interested in video streaming and encoding developer tools.
                The resources MUST be SPECIFIC with DIRECT URLs - not search results or generic listings.

                GOOD examples:
                - GitHub repositories (e.g., "https://github.com/username/project-name")
                - Specific documentation (e.g., "https://ffmpeg.org/documentation.html")
                - Technical blog posts (e.g., "https://netflixtechblog.com/...")
                - Specific tutorial pages (e.g., "https://www.coursename.com/specific-tutorial")
                - Software tool websites (e.g., "https://www.blackmagicdesign.com/products/davinciresolve")

                BAD examples (DO NOT INCLUDE THESE):
                - Google search results (e.g., "https://www.google.com/search?q=...")
                - YouTube search results (e.g., "https://www.youtube.com/results?search_query=...")
                - Generic listings pages

                FOLLOW THESE STEPS:
                1. Search for '{search_term}'
                2. For each search result, verify it leads to a SPECIFIC resource (not a search page)
                3. Only include results with DIRECT URLs to content
                4. Make sure the URL is to a specific page, not a general homepage
                5. Extract the most valuable information about each resource

                For each resource, provide:
                1. Title
                2. Description (explain what it offers and why it's valuable)
                3. URL (direct link to content)
                4. Category: {category}
                5. Tags (up to 5 relevant tags)

                Return your findings as a JSON array of resource objects, each with the following structure:
                {{
                  "title": "Resource Title",
                  "description": "Detailed resource description",
                  "url": "https://example.com/specific-resource",
                  "category": "{category}",
                  "tags": ["tag1", "tag2", "tag3"]
                }}
                """

                # Log search attempt
                start_time = time.time()
                logging.debug(f"Running web search with query: '{search_term}'")
                print(f"  🔍 Running web search for '{search_term}'")

                # Use asyncio with timeout to prevent hanging
                try:
                    result = await asyncio.wait_for(
                        Runner.run(self.agent, prompt),
                        timeout=timeout
                    )

                    logging.debug(f"Search completed in {time.time() - start_time:.2f}s")
                    print(f"  ✅ Search completed in {time.time() - start_time:.2f}s")
                    logging.debug(f"Raw search result: {result.final_output[:500]}...")
                except asyncio.TimeoutError:
                    logging.warning(f"Search timeout after {timeout}s")
                    print(f"  ⚠️ Search timeout after {timeout}s")
                    continue  # Try the next attempt

                # Extract JSON array from the response
                try:
                    # Find JSON in the response
                    json_text = result.final_output
                    logging.debug(f"Attempting to parse JSON from: {json_text[:500]}...")

                    # Look for array pattern if needed
                    if not json_text.strip().startswith('['):
                        import re
                        # More robust JSON extraction - finds arrays surrounded by square brackets
                        json_pattern = r'(\[\s*\{[\s\S]*\}\s*\])'
                        matches = re.search(json_pattern, json_text)
                        if matches:
                            json_text = matches.group(1)
                            logging.debug(f"Extracted JSON array using regex: {json_text[:500]}...")
                        else:
                            # Try a more aggressive pattern matching approach
                            potential_json = json_text.strip()
                            first_brace = potential_json.find('[')
                            last_brace = potential_json.rfind(']')

                            if first_brace >= 0 and last_brace > first_brace:
                                # Extract what looks like a JSON array
                                json_text = potential_json[first_brace:last_brace+1]
                                logging.debug(f"Attempting with extracted section: {json_text[:500]}...")
                                print(f"  🔄 Attempting with extracted JSON section")
                            else:
                                logging.error(f"No JSON-like structure found in response")
                                print(f"  ❌ No JSON-like structure found in response")
                                continue  # Try the next attempt

                    # Try to fix common JSON issues before parsing
                    json_text = json_text.replace('\n', ' ').replace('\r', ' ')

                    # Replace any trailing commas before a closing bracket (common JSON error)
                    json_text = re.sub(r',\s*\]', ']', json_text)
                    json_text = re.sub(r',\s*\}', '}', json_text)

                    resources = json.loads(json_text)
                    logging.info(f"Successfully parsed JSON with {len(resources)} resources")

                    # Enhanced validation and filtering for resources
                    valid_resources = []
                    invalid_count = 0
                    search_url_count = 0

                    for resource in resources:
                        if not isinstance(resource, dict):
                            logging.warning(f"Skipping non-object resource: {resource}")
                            invalid_count += 1
                            continue

                        # Skip resources without required fields
                        if not all(key in resource for key in ["title", "url", "description"]):
                            logging.warning(f"Resource missing required fields: {resource}")
                            invalid_count += 1
                            continue

                        url = resource.get("url", "").lower()
                        title = resource.get("title", "Untitled")

                        if not url:
                            logging.warning(f"Resource missing URL: {title}")
                            invalid_count += 1
                            continue

                        # Skip generic search results - expanded list of patterns
                        search_patterns = [
                            "google.com/search",
                            "youtube.com/results",
                            "bing.com/search",
                            "search?q=",
                            "search_query=",
                            "amazon.com/s?",
                            "search-results",
                            "searchresults",
                            "search.html"
                        ]

                        if any(pattern in url for pattern in search_patterns):
                            logging.warning(f"Skipping search result URL: {url}")
                            search_url_count += 1
                            continue

                        # Ensure URL seems legitimate and well-formed
                        if (url.startswith(("http://", "https://")) and
                            "." in url and
                            len(url) > 12 and  # Minimum reasonable URL length
                            not url.endswith(("..", "."))):  # Avoid truncated URLs

                            # Apply the current category to the resource
                            resource["category"] = category

                            # Ensure tags exist
                            if "tags" not in resource or not resource["tags"]:
                                resource["tags"] = [category]

                            valid_resources.append(resource)
                            logging.debug(f"Valid resource found: {title} - {url}")
                        else:
                            logging.warning(f"Invalid URL format: {url} for resource: {title}")
                            invalid_count += 1

                    # Log statistics about filtered resources
                    logging.info(f"Found {len(valid_resources)} valid resources out of {len(resources)} total")
                    logging.info(f"Filtered out {invalid_count} invalid resources and {search_url_count} search URLs")
                    print(f"  📊 Found {len(valid_resources)} valid resources out of {len(resources)} total")
                    print(f"  ⚠️ Filtered out {invalid_count} invalid and {search_url_count} search URLs")

                    resources = valid_resources

                    # If we found valid resources, return them
                    if resources:
                        logging.info(f"Found {len(resources)} valid resources for '{search_term}'")

                        # Enhanced logging for each resource found
                        print(f"\n✅ FOUND {len(resources)} RESOURCES:")
                        for i, resource in enumerate(resources, 1):
                            title = resource.get("title", "Untitled")
                            url = resource.get("url", "No URL")
                            tags = ", ".join(resource.get("tags", []))

                            print(f"  {i}. {title}")
                            print(f"     URL: {url}")
                            print(f"     Tags: {tags}")

                            # Detailed logging
                            logging.info(f"Resource {i}: {title}")
                            logging.info(f"  URL: {url}")
                            logging.info(f"  Tags: {tags}")

                        return resources
                    else:
                        logging.warning(f"No valid resources found in attempt {attempt} for '{search_term}'")
                        print(f"  ⚠️ No valid resources found in this attempt. Retrying...")

                except json.JSONDecodeError as json_err:
                    logging.error(f"JSON parsing error: {json_err}")
                    print(f"  ❌ JSON parsing error: {json_err}")
                    # Log the problematic text
                    logging.debug(f"Problematic JSON text: {json_text[:200]}...")
                except Exception as e:
                    logging.error(f"Error processing search results: {str(e)}", exc_info=True)
                    print(f"  ❌ Error processing results: {type(e).__name__}: {str(e)}")

            except Exception as e:
                logging.error(f"Error in search attempt {attempt} for '{search_term}': {str(e)}", exc_info=True)
                print(f"  ❌ Error during search: {type(e).__name__}: {str(e)}")

            # Small delay before retry
            if attempt < max_retries:
                await asyncio.sleep(2)

        # If we reach here, we couldn't find valid resources after all retries
        logging.warning(f"No valid resources found for '{search_term}' after {max_retries} attempts")
        print(f"\n⚠️ Could not find valid resources for '{search_term}' after {max_retries} attempts")
        return []


class WriterAgent:
    """Agent that generates project ideas based on resources."""

    def __init__(self):
        self.agent = Agent(
            name="Project Idea Generator",
            instructions="""
            You are a Project Idea Generator specializing in creative and practical project ideas for video streaming and encoding developer tools.

            Your task is to generate unique, valuable project ideas based on existing projects and new resources.
            Each project idea should include:
            1. A compelling title
            2. A detailed description explaining the concept, approach, and value
            3. The category it belongs to
            4. Relevant tags (up to 5)
            """
        )

    async def generate_ideas(self, category, existing_data, new_resources):
        """Generate project ideas based on existing data and new resources."""
        logging.info(f"Generating project ideas for category: '{category}'")
        print(f"\n💡 GENERATING PROJECT IDEAS: Category '{category}'")

        if not new_resources:
            logging.warning(f"No new resources found for '{category}', skipping project idea generation")
            print(f"  ⚠️ No new resources found for this category, skipping")
            return []

        # Create samples of existing data and new resources for context
        sample_existing = [item for item in existing_data if item.get("category") == category]
        sample_existing = sample_existing[:3] if len(sample_existing) > 3 else sample_existing

        sample_new = new_resources[:3] if len(new_resources) > 3 else new_resources

        prompt = f"""
        Generate 3 creative project ideas for the '{category}' category based on existing projects and newly found resources.

        Existing projects: {json.dumps(sample_existing)}

        Newly found resources: {json.dumps(sample_new)}

        Please generate 3 unique, practical, and creative project ideas that:
        1. Are relevant to the '{category}' category
        2. Build upon the existing projects and new resources
        3. Offer clear value to someone interested in video streaming and encoding developer tools
        4. Include a compelling title and detailed description
        5. Have relevant tags

        Return your ideas as a JSON array of project ideas, each with the following structure:
        {{
          "title": "Project Idea Title",
          "description": "Detailed project description explaining the concept, approach, and value",
          "category": "{category}",
          "tags": ["tag1", "tag2", "tag3"]
        }}
        """

        result = await Runner.run(self.agent, prompt)

        # Extract JSON array from the response
        try:
            # Find JSON in the response
            json_text = result.final_output
            # Look for array pattern if needed
            if not json_text.strip().startswith('['):
                import re
                json_pattern = r'(\[[\s\S]*\])'
                matches = re.search(json_pattern, json_text)
                if matches:
                    json_text = matches.group(1)

            project_ideas = json.loads(json_text)
            logging.info(f"Generated {len(project_ideas)} project ideas for '{category}'")

            # Enhanced logging for each project idea
            print(f"\n💡 GENERATED {len(project_ideas)} PROJECT IDEAS:")
            for i, idea in enumerate(project_ideas, 1):
                title = idea.get("title", "Untitled")
                tags = ", ".join(idea.get("tags", []))

                print(f"  {i}. {title}")
                print(f"     Tags: {tags}")

                # Detailed logging
                logging.info(f"Project Idea {i}: {title}")
                logging.info(f"  Tags: {tags}")

            return project_ideas
        except Exception as e:
            logging.error(f"Error parsing project ideas: {e}")
            logging.debug(f"Raw output: {result.final_output}")
            print(f"\n❌ ERROR: Failed to generate project ideas: {e}")
            raise Exception(f"Failed to generate valid project ideas: {e}")


class ResearchManager:
    """Manager that coordinates the research process between agents."""

    def __init__(self):
        self.planner_agent = PlannerAgent()
        self.search_agent = SearchAgent()
        self.writer_agent = WriterAgent()

    async def run(self, contents_data, min_results=10, time_limit=300, global_timeout=14400, randomize=False, random_seed=None):
        """Run the complete research process with the given parameters."""
        start_time = time.time()
        all_new_resources = []
        all_project_ideas = []

        # PHASE 1: Planning
        logging.info("Starting research planning phase")
        print("\n🔍 PLANNING RESEARCH...")

        try:
            research_plan = await self._plan_searches(contents_data)
            logging.info("Research plan created successfully")
        except Exception as e:
            logging.error(f"Error creating research plan: {e}")
            print(f"\n❌ ERROR creating research plan: {e}")
            return 1, [], []

        # Setup progress tracking
        categories = contents_data.get("categories", [])
        categories_data = contents_data.get("_categories_data", {})
        priority_categories = research_plan.get("priority_categories", categories)
        search_terms = research_plan.get("search_terms", {})

        # Randomize category order if requested
        if randomize:
            if random_seed is not None:
                random.seed(random_seed)
                logging.info(f"Using random seed: {random_seed}")
            else:
                random_seed = int(time.time())
                random.seed(random_seed)
                logging.info(f"Using random seed: {random_seed}")

            random.shuffle(priority_categories)
            logging.info("Randomized category order")
            print("\n🎲 RANDOMIZED CATEGORY ORDER:")
            for i, cat in enumerate(priority_categories[:5], 1):
                cat_title = categories_data.get(cat, {}).get("title", cat)
                print(f"  {i}. {cat_title} ({cat})")
            if len(priority_categories) > 5:
                print(f"  ... and {len(priority_categories) - 5} more categories")

        # PHASE 2: Execute searches for each category
        for category_index, category in enumerate(priority_categories):
            # Check global timeout
            if time.time() - start_time > global_timeout:
                logging.warning(f"Global timeout ({global_timeout}s) reached after {category_index} categories")
                print(f"\n⏱️ GLOBAL TIMEOUT REACHED: Script has been running for {(time.time() - start_time):.2f} seconds")
                print(f"Completed {category_index}/{len(priority_categories)} categories")
                break

            time_so_far = time.time() - start_time
            cat_title = categories_data.get(category, {}).get("title", category)
            logging.info(f"Researching category: {cat_title} ({category}) ({category_index+1}/{len(priority_categories)}) - Time elapsed: {time_so_far:.2f}s")

            print(f"\n{'='*70}")
            print(f"📌 CATEGORY {category_index+1}/{len(priority_categories)}: {cat_title} ({category})")
            print(f"{'='*70}")
            print(f"⏱️ Time elapsed: {time_so_far:.2f}s, {(global_timeout - time_so_far):.2f}s remaining until timeout")

            # Get category time limit
            category_start_time = time.time()
            category_time_limit = min(time_limit, global_timeout - time_so_far)

            # Skip if less than 30 seconds left
            if category_time_limit < 30:
                logging.warning(f"Insufficient time left for category '{category}', skipping")
                print(f"⚠️ Less than 30 seconds of timeout remaining, skipping this category")
                continue

            print(f"⏱️ Time limit for this category: {category_time_limit:.2f}s")

            # Get search terms for this category
            category_search_terms = search_terms.get(category, [])
            if not category_search_terms:
                cat_title = categories_data.get(category, {}).get("title", category)
                category_search_terms = [
                    f"best {cat_title} streaming tools",
                    f"{cat_title} encoding github repositories",
                    f"{cat_title} streaming API tutorials",
                    f"{cat_title} video codec software",
                    f"advanced {cat_title} streaming techniques",
                    f"{cat_title} video encoding libraries"
                ]
                print(f"⚠️ Using default search terms for '{cat_title}'")

            # PHASE 3: Perform parallel searches
            logging.info(f"Executing {len(category_search_terms)} searches for '{category}'")
            print(f"🔍 EXECUTING {len(category_search_terms)} SEARCH QUERIES:")
            for term in category_search_terms:
                print(f"  • {term}")

            # Run searches in parallel using asyncio
            category_resources = await self._perform_searches(category, category_search_terms, category_time_limit)

            # Filter out duplicates
            seen_urls = set()
            unique_resources = []

            print(f"\n🔍 CHECKING FOR DUPLICATES IN {len(category_resources)} RESOURCES...")
            for resource in category_resources:
                url = resource.get("url", "")
                if url and url not in seen_urls:
                    seen_urls.add(url)
                    unique_resources.append(resource)
                    print(f"  ✅ UNIQUE: {resource.get('title', 'Untitled')} - {url}")
                else:
                    print(f"  ⚠️ DUPLICATE: {resource.get('title', 'Untitled')} - {url}")

            # Check if we found any resources
            if unique_resources:
                logging.info(f"After filtering, {len(unique_resources)} unique resources for '{category}'")
                print(f"\n📊 AFTER FILTERING DUPLICATES: {len(unique_resources)} unique resources for '{category}'")

                # Add to overall collection
                all_new_resources.extend(unique_resources)

                # PHASE 4: Generate project ideas if we have resources
                if time.time() - start_time <= global_timeout:
                    try:
                        project_ideas = await self._generate_ideas(category,
                                                                  [item for item in contents_data.get(category, [])],
                                                                  unique_resources)
                        logging.info(f"Generated {len(project_ideas)} project ideas for '{category}'")
                        all_project_ideas.extend(project_ideas)
                    except Exception as e:
                        logging.error(f"Error generating project ideas: {e}")
                        print(f"\n⚠️ Error generating project ideas: {e}")
                else:
                    logging.warning("Global timeout reached before generating project ideas")
                    print("\n⏱️ GLOBAL TIMEOUT REACHED: Skipping project idea generation")
            else:
                logging.warning(f"No resources found for category '{category}'")
                print(f"\n⚠️ No resources found for category '{category}'")

            # Log progress
            print(f"\n🔄 PROGRESS: {len(all_new_resources)} total resources and {len(all_project_ideas)} ideas so far")

            category_time = time.time() - category_start_time
            logging.info(f"Finished category '{category}' in {category_time:.2f} seconds")
            print(f"⏱️ Category '{cat_title}' completed in {category_time:.2f} seconds")

        # Return results
        return 0, all_new_resources, all_project_ideas

    async def _plan_searches(self, contents_data):
        """Create a research plan using the planner agent."""
        logging.info("Creating research plan")
        print("\n📋 CREATING RESEARCH PLAN...")

        try:
            research_plan = await self.planner_agent.create_plan(contents_data)

            # Enhanced logging for the plan
            print("\n✅ RESEARCH PLAN CREATED")
            print("\n🔍 PRIORITY CATEGORIES:")
            categories_data = contents_data.get("_categories_data", {})

            for i, category_id in enumerate(research_plan.get('priority_categories', []), 1):
                title = categories_data.get(category_id, {}).get("title", category_id)
                print(f"  {i}. {title} ({category_id})")

            print("\n🔍 SEARCH TERMS BY CATEGORY:")
            for category_id, terms in research_plan.get('search_terms', {}).items():
                title = categories_data.get(category_id, {}).get("title", category_id)
                print(f"  • {title} ({category_id}):")
                for i, term in enumerate(terms, 1):
                    print(f"    {i}. {term}")

            return research_plan
        except Exception as e:
            logging.error(f"Error in planning phase: {e}")
            raise

    async def _perform_searches(self, category, search_terms, time_limit):
        """Perform searches in parallel using asyncio tasks."""
        logging.info(f"Starting parallel searches for {len(search_terms)} terms in category '{category}'")
        print(f"🔍 STARTING PARALLEL SEARCHES: {len(search_terms)} terms in category '{category}'")

        start_time = time.time()
        all_resources = []

        # Create search tasks and run them in parallel
        search_tasks = []
        for term in search_terms:
            search_tasks.append(self._search(term, category, timeout=60))

        try:
            # Run all searches in parallel with overall time limit
            remaining_time = max(5, time_limit - (time.time() - start_time))
            results = await asyncio.wait_for(
                asyncio.gather(*search_tasks, return_exceptions=True),
                timeout=remaining_time
            )

            # Process results
            for i, result in enumerate(results):
                try:
                    if isinstance(result, Exception):
                        # Handle exception from task
                        term = search_terms[i] if i < len(search_terms) else f"term-{i}"
                        if isinstance(result, asyncio.TimeoutError):
                            logging.warning(f"Search for '{term}' timed out")
                            print(f"  ⚠️ Search for '{term}' timed out")
                        else:
                            logging.error(f"Error in search for '{term}': {str(result)}")
                            print(f"  ❌ Error in search for '{term}': {type(result).__name__}: {str(result)}")
                    else:
                        # Process successful result
                        term = search_terms[i] if i < len(search_terms) else f"term-{i}"
                        resources = result or []  # Ensure we have a list even if None was returned

                        if resources:
                            logging.info(f"Found {len(resources)} resources for '{term}'")
                            print(f"  ✅ Found {len(resources)} resources for '{term}'")
                            all_resources.extend(resources)
                        else:
                            logging.warning(f"No resources found for '{term}'")
                            print(f"  ⚠️ No resources found for '{term}'")
                except Exception as e:
                    logging.error(f"Error processing result: {str(e)}", exc_info=True)
                    print(f"  ❌ Error processing result: {str(e)}")

        except asyncio.TimeoutError:
            logging.warning(f"Overall search timeout after {time_limit:.2f}s for category '{category}'")
            print(f"\n⚠️ Overall search timeout for category '{category}' after {time_limit:.2f}s")
            print(f"  Some search tasks were cancelled")

        except Exception as e:
            logging.error(f"Unexpected error in parallel searches: {str(e)}", exc_info=True)
            print(f"\n❌ Error in parallel searches: {str(e)}")

        # Log results summary
        search_time = time.time() - start_time
        resource_count = len(all_resources)
        logging.info(f"Completed {len(search_terms)} searches in {search_time:.2f}s, found {resource_count} resources")
        print(f"\n📊 SEARCH SUMMARY: Completed {len(search_terms)} searches in {search_time:.2f}s")
        print(f"  Found {resource_count} resources for category '{category}'")

        return all_resources

    async def _search(self, search_term, category, timeout=60):
        """Execute a single search using the search agent."""
        logging.info(f"Searching for: '{search_term}' in category '{category}'")
        print(f"\n🔍 SEARCHING: '{search_term}' in category '{category}'")

        try:
            # Enhance the search term to be more specific and effective
            enhanced_term = f"{search_term} video technology resources"
            logging.debug(f"Using enhanced search term: '{enhanced_term}'")

            resources = await self.search_agent.search(enhanced_term, category, timeout=timeout)

            # Validate returned resources
            if resources:
                # Check if all URLs are unique
                urls = [r.get("url", "") for r in resources]
                unique_urls = set(urls)

                if len(unique_urls) < len(urls):
                    logging.warning(f"Found {len(urls) - len(unique_urls)} duplicate URLs in search results")

                # Check for invalid category assignments
                for resource in resources:
                    if resource.get("category") != category:
                        logging.warning(f"Fixing incorrect category in resource: {resource.get('title')}")
                        resource["category"] = category

                # Additional logging
                logging.info(f"Successfully found {len(resources)} resources for '{search_term}'")
                print(f"  ✓ Found {len(resources)} valid resources")
            else:
                logging.warning(f"No resources found for '{search_term}'")
                print(f"  ⚠️ No resources found")

            return resources
        except Exception as e:
            logging.error(f"Search error for '{search_term}': {e}", exc_info=True)
            print(f"  ❌ Search error: {type(e).__name__}: {str(e)}")
            return []

    async def _generate_ideas(self, category, existing_data, new_resources):
        """Generate project ideas using the writer agent."""
        logging.info(f"Generating project ideas for category: '{category}'")
        print(f"\n💡 GENERATING PROJECT IDEAS: Category '{category}'")

        try:
            project_ideas = await self.writer_agent.generate_ideas(category, existing_data, new_resources)
            return project_ideas
        except Exception as e:
            logging.error(f"Error generating project ideas: {e}")
            raise


async def run_system_checks():
    """Run basic validation checks to ensure the system is ready to operate."""
    checks_passed = True
    results = []

    # Check if OPENAI_API_KEY is set
    logging.info("Running system check: OpenAI API Key")
    api_key = os.environ.get("OPENAI_API_KEY")
    if api_key:
        results.append(("OpenAI API Key", "PASS", "API key is set"))
        print("  ✅ OpenAI API Key: Found")
    else:
        results.append(("OpenAI API Key", "FAIL", "API key is not set"))
        checks_passed = False
        print("  ❌ OpenAI API Key: Not found")

    # Check OpenAI API
    logging.info("Running system check: OpenAI API")
    print("  🔄 Testing OpenAI API connection...")
    try:
        agent = Agent(name="Tester", instructions="You are a test agent.")
        result = await Runner.run(agent, "Respond with the word 'HEALTHY' if you can process this message.")
        if "HEALTHY" in result.final_output:
            results.append(("OpenAI API", "PASS", "API is responding correctly"))
            print("  ✅ OpenAI API: Connection successful")
        else:
            results.append(("OpenAI API", "WARNING", f"API responded with unexpected content: {result.final_output[:50]}..."))
            print(f"  ⚠️ OpenAI API: Responded with unexpected content")
    except Exception as e:
        results.append(("OpenAI API", "FAIL", f"Error: {str(e)}"))
        checks_passed = False
        print(f"  ❌ OpenAI API: Connection failed: {str(e)}")
        # If the API doesn't work, we can't proceed
        logging.error("System checks failed - OpenAI API is required")
        return False

    # Check Web Search Tool - critical for functioning
    logging.info("Running system check: Web Search Tool")
    print("  🔄 Testing web search capability...")
    try:
        web_search_agent = Agent(
            name="Search Tester",
            instructions="""
            You are a search agent for testing web search capability.
            Your task is to search for a specific term and return ONE specific resource with a direct URL.
            DO NOT return search result pages like Google or YouTube search URLs.
            Only return a SINGLE direct URL to a specific website, tool, or resource related to video streaming or encoding.
            Return ONLY the direct URL with no other text or explanation.
            """,
            tools=[WebSearchTool()]
        )
        search_prompt = "Search for 'ffmpeg video streaming' and return ONLY a direct URL to the official FFmpeg website or documentation (not a search page)"

        # Use asyncio with timeout to prevent hanging
        try:
            search_result = await asyncio.wait_for(
                Runner.run(web_search_agent, search_prompt),
                timeout=30  # 30 second timeout for test
            )

            if search_result.final_output and len(search_result.final_output.strip()) > 10:
                # Extract URL using regex
                import re
                url_pattern = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'
                urls = re.findall(url_pattern, search_result.final_output)

                # Check if any valid URLs were found and they're not search pages
                if urls:
                    # Check if any URL is a search result
                    search_patterns = [
                        "google.com/search",
                        "youtube.com/results",
                        "bing.com/search",
                        "search?q=",
                        "search_query="
                    ]

                    valid_urls = []
                    for url in urls:
                        if not any(pattern in url.lower() for pattern in search_patterns):
                            valid_urls.append(url)

                    if valid_urls:
                        # Found at least one valid direct URL
                        example_url = valid_urls[0]
                        results.append(("Web Search Tool", "PASS", f"Web search returned valid direct URL: {example_url}"))
                        print(f"  ✅ Web Search: Working properly - found direct URL: {example_url}")
                    else:
                        # Only found search URLs
                        results.append(("Web Search Tool", "WARNING", f"Web search only returned search page URLs"))
                        print("  ⚠️ Web Search: Only returned search page URLs")
                        print("    This will impact the script's ability to find valuable resources")
                else:
                    # No URLs found at all
                    results.append(("Web Search Tool", "WARNING", "Web search didn't return any URLs"))
                    print("  ⚠️ Web Search: Returned response without URLs")
                    print("    Response: " + search_result.final_output[:100] + "...")
            else:
                # Empty or very short response
                results.append(("Web Search Tool", "WARNING", f"Web search returned limited results: {search_result.final_output}"))
                print("  ⚠️ Web Search: Returned limited results")
                print("    The script may struggle to find valuable resources")
        except asyncio.TimeoutError:
            results.append(("Web Search Tool", "WARNING", "Web search timed out after 30 seconds"))
            print("  ⚠️ Web Search: Test timed out after 30 seconds")
            print("    This may indicate slow responses but the tool may still work")
    except Exception as e:
        results.append(("Web Search Tool", "FAIL", f"Error: {str(e)}"))
        checks_passed = False
        print(f"  ❌ Web Search: Failed: {str(e)}")
        print("    The web search functionality is CRITICAL for this script to work properly")
        print("    Without working web search, the script won't find any valuable resources")
        logging.error(f"Web search check failed: {e}", exc_info=True)

    # Log results
    logging.info("System check results:")
    for check, status, message in results:
        if status == "PASS":
            logging.info(f"  ✓ {check}: {message}")
        elif status == "WARNING":
            logging.warning(f"  ⚠ {check}: {message}")
        else:
            logging.error(f"  ✗ {check}: {message}")

    if not checks_passed:
        print("\n⚠️ Some critical checks failed. The script may not work properly.")
    else:
        print("\n✅ All critical checks passed. The script should work properly.")

    return checks_passed


async def save_intermediate_results(resources, project_ideas, final=False, output_dir="."):
    """Save intermediate results to a file."""
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    results = {
        "new_resources": resources,
        "new_project_ideas": project_ideas,
        "timestamp": datetime.datetime.now().isoformat(),
        "stats": {
            "resources_count": len(resources),
            "project_ideas_count": len(project_ideas),
            "resources_by_category": {},
            "ideas_by_category": {}
        }
    }

    # Calculate statistics
    for resource in resources:
        category = resource.get("category", "uncategorized")
        if category not in results["stats"]["resources_by_category"]:
            results["stats"]["resources_by_category"][category] = 0
        results["stats"]["resources_by_category"][category] += 1

    for idea in project_ideas:
        category = idea.get("category", "uncategorized")
        if category not in results["stats"]["ideas_by_category"]:
            results["stats"]["ideas_by_category"][category] = 0
        results["stats"]["ideas_by_category"][category] += 1

    # Always include timestamp in filenames to avoid conflicts between parallel runs
    if final:
        filename = f"final_results_{timestamp}_{len(resources)}_resources.json"
    else:
        filename = f"intermediate_results_{timestamp}.json"

    filepath = os.path.join(output_dir, filename)

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    with open(filepath, 'w') as f:
        json.dump(results, f, indent=JSON_INDENT)

    logging.info(f"Saved {len(resources)} resources and {len(project_ideas)} project ideas to {filepath}")

    if final:
        print(f"\n📁 FINAL RESULTS SAVED TO: {filepath}")
        print("\n📊 RESOURCE STATISTICS BY CATEGORY:")
        for category, count in results["stats"]["resources_by_category"].items():
            print(f"  • {category}: {count} resources")

        print("\n📊 PROJECT IDEA STATISTICS BY CATEGORY:")
        for category, count in results["stats"]["ideas_by_category"].items():
            print(f"  • {category}: {count} project ideas")

        # Log statistics
        logging.info("Final statistics:")
        for category, count in results["stats"]["resources_by_category"].items():
            logging.info(f"  - {count} resources in category '{category}'")
        for category, count in results["stats"]["ideas_by_category"].items():
            logging.info(f"  - {count} project ideas in category '{category}'")
    else:
        print(f"\n📁 INTERMEDIATE RESULTS SAVED: {filepath}")

    return filepath


async def update_contents(original_filepath_or_url, new_resources, new_project_ideas, output_dir="."):
    """Update the original contents file or create a new file with the combined results."""
    logging.info(f"Updating contents with new findings")
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    # For remote files, we can't update them directly
    is_remote = original_filepath_or_url.startswith(('http://', 'https://'))

    # Determine output file path
    if is_remote:
        output_filename = f"updated_contents_{timestamp}.json"
        output_filepath = os.path.join(output_dir, output_filename)
        logging.info(f"Remote URL detected, results will be saved to: {output_filepath}")
    else:
        # Create a new timestamped file instead of overwriting
        basename = os.path.basename(original_filepath_or_url)
        filename_without_ext, ext = os.path.splitext(basename)
        output_filename = f"{filename_without_ext}_updated_{timestamp}{ext}"
        output_filepath = os.path.join(output_dir, output_filename)
        logging.info(f"Local file detected, creating updated version at: {output_filepath}")

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    try:
        # Load original contents
        contents = await load_contents(original_filepath_or_url)

        # Count initial items
        initial_counts = {}
        for category in contents.get("categories", []):
            initial_counts[category] = len(contents.get(category, []))

        logging.info(f"Original contents has categories: {list(initial_counts.keys())}")

        # Add new resources to their respective categories
        resources_added = 0
        resources_by_category = {}

        for resource in new_resources:
            category = resource.get("category")
            if category in contents:
                # Remove category from resource to match original format
                resource_copy = resource.copy()
                category_field = resource_copy.pop("category", None)

                contents[category].append(resource_copy)
                resources_added += 1

                # Track additions by category
                if category not in resources_by_category:
                    resources_by_category[category] = 0
                resources_by_category[category] += 1
            else:
                logging.warning(f"Category '{category}' not found in original contents, skipping resource: {resource.get('title', 'Untitled')}")

        # Count final items
        final_counts = {}
        for category in contents.get("categories", []):
            final_counts[category] = len(contents.get(category, []))

        # Create a backup if this is a local file
        if not is_remote and os.path.exists(original_filepath_or_url):
            backup_path = f"{original_filepath_or_url}.bak.{timestamp}"
            logging.info(f"Creating backup of original file at {backup_path}")
            with open(backup_path, 'w') as f:
                json.dump(contents, f, indent=JSON_INDENT)

        # Write updated contents to file
        with open(output_filepath, 'w') as f:
            json.dump(contents, f, indent=JSON_INDENT)

        # Log results
        logging.info(f"Successfully saved updated contents to {output_filepath}")
        logging.info(f"Added {resources_added} new resources:")
        for category, count in resources_by_category.items():
            logging.info(f"  - Added {count} resources to '{category}' (now has {final_counts.get(category, 0)} items)")

        return output_filepath
    except Exception as e:
        logging.error(f"Error updating contents: {e}")
        if is_remote:
            logging.error(f"Consider specifying a local output file instead of a remote URL")
        return None


async def generate_awesome_list(contents_data, new_resources, output_file="awesome-video.md", output_dir="."):
    """Generate an Awesome List markdown file following specifications from sindresorhus/awesome.

    This function creates a properly formatted markdown file that follows all the guidelines
    and best practices for Awesome Lists, ensuring it will pass awesome-lint validation.
    """
    logging.info(f"Generating Awesome List markdown file")

    # Add timestamp to filename to prevent conflicts
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    # Split the output filename into base and extension
    filename_base, filename_ext = os.path.splitext(output_file)
    timestamped_filename = f"{filename_base}_{timestamp}{filename_ext}"

    # Create full path
    output_path = os.path.join(output_dir, timestamped_filename)

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    print(f"\n📄 GENERATING AWESOME LIST: {output_path}")

    # Extract categories and resources
    categories = contents_data.get("categories", [])
    categories_data = contents_data.get("_categories_data", {})

    if not categories:
        logging.error("No categories found in contents data")
        print(f"  ❌ ERROR: No categories found in contents data")
        return False

    # Count items for logging
    total_resources = 0
    resource_counts = {}
    subcategory_counts = {}

    # Find top-level categories (those with no parent)
    top_level_categories = []
    for cat_id, cat_data in categories_data.items():
        if not cat_data.get("parent"):
            top_level_categories.append(cat_id)
            # Count subcategories
            children = cat_data.get("children", [])
            subcategory_counts[cat_id] = len(children)

    # Merge new resources with existing ones
    for category in categories:
        existing_resources = contents_data.get(category, [])
        category_new_resources = [r for r in new_resources if r.get("category") == category]

        # Keep track of counts
        resource_counts[category] = len(existing_resources) + len(category_new_resources)
        total_resources += resource_counts[category]

    logging.info(f"Preparing to generate Awesome List with {total_resources} resources across {len(categories)} categories")
    logging.info(f"Found {len(top_level_categories)} top-level categories and {sum(subcategory_counts.values())} subcategories")

    # Start generating the markdown content
    lines = []

    # Add Awesome badge, title, and description
    lines.append("# Awesome Video Streaming & Encoding [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)")
    lines.append("")
    lines.append("> A curated list of awesome tools, resources, and projects related to video streaming, encoding, and processing for developers")
    lines.append("")

    # Add standard sections required by Awesome List spec
    lines.append("## Contents")
    lines.append("")

    # Generate table of contents
    for cat_id in top_level_categories:
        cat_data = categories_data.get(cat_id, {})
        cat_title = cat_data.get("title", cat_id)
        lines.append(f"- [{cat_title}](#{cat_title.lower().replace(' ', '-').replace('/', '').replace('.', '').replace(':', '')})")

        # Add subcategories to TOC if any
        children = cat_data.get("children", [])
        if children:
            for child_id in children:
                child_data = categories_data.get(child_id, {})
                child_title = child_data.get("title", child_id)
                lines.append(f"  - [{child_title}](#{child_title.lower().replace(' ', '-').replace('/', '').replace('.', '').replace(':', '')})")

    # Add Contributing and License sections to TOC
    lines.append("- [Contributing](#contributing)")
    lines.append("")

    # Generate content for each category
    print(f"  📊 Organizing {total_resources} resources into {len(top_level_categories)} main categories")
    resource_counter = 0

    for cat_id in top_level_categories:
        cat_data = categories_data.get(cat_id, {})
        cat_title = cat_data.get("title", cat_id)
        cat_description = cat_data.get("description", "")

        # Add category heading and description
        lines.append(f"## {cat_title}")
        if cat_description:
            lines.append("")
            lines.append(cat_description)
        lines.append("")

        # Add resources directly in this category (if it's not just a parent category)
        category_resources = contents_data.get(cat_id, [])
        category_new_resources = [r for r in new_resources if r.get("category") == cat_id]
        all_resources = category_resources + category_new_resources

        if all_resources:
            resource_counter += len(all_resources)
            for resource in all_resources:
                title = resource.get("title", "")
                url = resource.get("url", resource.get("homepage", ""))
                description = resource.get("description", "")

                # Format according to Awesome List spec: "- [Name](URL) - Description."
                # Ensure description starts with uppercase and ends with period
                if description and not description.endswith(('.', '!', '?')):
                    description = description + "."

                if description and description[0].islower():
                    description = description[0].upper() + description[1:]

                if title and url:
                    lines.append(f"- [{title}]({url}) - {description}")

            lines.append("")

        # Add subcategories and their resources
        children = cat_data.get("children", [])
        for child_id in children:
            child_data = categories_data.get(child_id, {})
            child_title = child_data.get("title", child_id)
            child_description = child_data.get("description", "")

            # Add subcategory heading and description
            lines.append(f"### {child_title}")
            if child_description:
                lines.append("")
                lines.append(child_description)
            lines.append("")

            # Add resources in this subcategory
            child_resources = contents_data.get(child_id, [])
            child_new_resources = [r for r in new_resources if r.get("category") == child_id]
            all_child_resources = child_resources + child_new_resources

            if all_child_resources:
                resource_counter += len(all_child_resources)
                for resource in all_child_resources:
                    title = resource.get("title", "")
                    url = resource.get("url", resource.get("homepage", ""))
                    description = resource.get("description", "")

                    # Format according to Awesome List spec
                    if description and not description.endswith(('.', '!', '?')):
                        description = description + "."

                    if description and description[0].islower():
                        description = description[0].upper() + description[1:]

                    if title and url:
                        lines.append(f"- [{title}]({url}) - {description}")

                lines.append("")

    # Add Contributing section
    lines.append("## Contributing")
    lines.append("")
    lines.append("Contributions welcome! Read the [contribution guidelines](contributing.md) first.")
    lines.append("")

    # Write the output file
    try:
        with open(output_path, 'w') as f:
            f.write('\n'.join(lines))

        # Create a basic contributing.md file if it doesn't exist
        if not os.path.exists("contributing.md"):
            with open("contributing.md", 'w') as f:
                f.write("# Contribution Guidelines\n\n")
                f.write("Please note that this project is released with a [Contributor Code of Conduct](code-of-conduct.md). By participating in this project you agree to abide by its terms.\n\n")
                f.write("## Adding to this list\n\n")
                f.write("Please ensure your pull request adheres to the following guidelines:\n\n")
                f.write("- Search previous suggestions before making a new one, as yours may be a duplicate.\n")
                f.write("- Make sure the resource is useful before submitting.\n")
                f.write("- Make an individual pull request for each suggestion.\n")
                f.write("- Use title-casing (AP style).\n")
                f.write("- Use the following format: `[Name](link) - Description.`\n")
                f.write("- Start the description with a capital and end with a full stop.\n")
                f.write("- Check your spelling and grammar.\n")
                f.write("- Make sure your text editor is set to remove trailing whitespace.\n")
                f.write("- The pull request and commit should have a useful title.\n")
                f.write("- The body of your commit message should contain a link to the resource.\n\n")
                f.write("Thank you for your suggestions!\n")

        # Create a code-of-conduct.md file if it doesn't exist
        if not os.path.exists("code-of-conduct.md"):
            with open("code-of-conduct.md", 'w') as f:
                f.write("# Contributor Covenant Code of Conduct\n\n")
                f.write("## Our Pledge\n\n")
                f.write("In the interest of fostering an open and welcoming environment, we as contributors and maintainers pledge to making participation in our project and our community a harassment-free experience for everyone.\n\n")
                # Add more standard code of conduct content here

        # Create a license file (CC0) if it doesn't exist
        if not os.path.exists("license"):
            with open("license", 'w') as f:
                f.write("CC0 1.0 Universal\n\n")
                f.write("Statement of Purpose\n\n")
                f.write("The laws of most jurisdictions throughout the world automatically confer exclusive Copyright and Related Rights upon the creator and subsequent owner(s) of an original work of authorship.\n\n")
                # Add more CC0 license content here

        logging.info(f"Successfully generated Awesome List at {output_path}")
        logging.info(f"Included {resource_counter} resources across {len(top_level_categories)} main categories")
        logging.info(f"Created necessary support files: contributing.md, code-of-conduct.md, license")

        print(f"  ✅ AWESOME LIST GENERATED: {output_path}")
        print(f"  📊 STATISTICS:")
        print(f"    • {resource_counter} total resources")
        print(f"    • {len(top_level_categories)} main categories")
        print(f"    • {sum(subcategory_counts.values())} subcategories")
        print(f"  📝 CREATED SUPPORTING FILES:")
        print(f"    • contributing.md")
        print(f"    • code-of-conduct.md")
        print(f"    • license (CC0)")

        return output_path
    except Exception as e:
        logging.error(f"Error generating Awesome List: {e}")
        print(f"  ❌ ERROR: Could not generate Awesome List: {e}")
        return False


async def verify_awesome_list(filepath):
    """Perform basic validation checks on the generated Awesome List markdown file.

    While this doesn't replace running awesome-lint, it checks for common
    issues that might cause awesome-lint to fail.
    """
    logging.info(f"Verifying Awesome List compliance: {filepath}")
    print(f"\n🔍 VERIFYING AWESOME LIST: {filepath}")

    verification_errors = []

    try:
        with open(filepath, 'r') as f:
            content = f.read()
            lines = content.splitlines()

        # Check for required elements
        if not any(line.startswith("# Awesome") for line in lines):
            verification_errors.append("Missing 'Awesome' in the main title")

        if not any("[![Awesome]" in line and "https://awesome.re" in line for line in lines):
            verification_errors.append("Missing Awesome badge after main heading")

        if not any(line == "## Contents" for line in lines):
            verification_errors.append("Missing Table of Contents section")

        if not any(line == "## Contributing" for line in lines):
            verification_errors.append("Missing Contributing section")

        # Check for list item format consistency
        resource_lines = [line for line in lines if line.startswith("- [")]

        for line in resource_lines:
            # Check if line follows format: "- [Name](URL) - Description."
            if not re.match(r"^- \[[^\]]+\]\([^)]+\) - .+[\.!?]$", line):
                verification_errors.append(f"Invalid resource format: {line[:50]}...")

        # Verify support files exist
        if not os.path.exists("contributing.md"):
            verification_errors.append("Missing contributing.md file")

        if not os.path.exists("license") and not os.path.exists("LICENSE"):
            verification_errors.append("Missing license file")

        # Log verification results
        if verification_errors:
            logging.warning(f"Found {len(verification_errors)} issues with Awesome List format")
            print(f"  ⚠️ FOUND {len(verification_errors)} FORMATTING ISSUES:")
            for error in verification_errors:
                logging.warning(f"  - {error}")
                print(f"    • {error}")

            return False, verification_errors
        else:
            logging.info("Awesome List validation successful")
            print(f"  ✅ AWESOME LIST FORMAT VALIDATION SUCCESSFUL")

            # Recommend running awesome-lint
            print(f"  ℹ️ For complete validation, run: npx awesome-lint {filepath}")
            return True, []

    except Exception as e:
        logging.error(f"Error verifying Awesome List: {e}")
        print(f"  ❌ ERROR: Could not verify Awesome List: {e}")
        return False, [f"Error during verification: {str(e)}"]


async def generate_combined_contents(original_filepath_or_url, new_resources, output_dir="."):
    """Generate a new contents.json file that combines original contents and new resources.

    The filename includes timestamp and total project count.
    """
    logging.info(f"Generating combined contents file from {original_filepath_or_url} with {len(new_resources)} new resources")
    print(f"\n📊 GENERATING COMBINED CONTENTS FILE...")

    try:
        # Load original contents
        contents = await load_contents(original_filepath_or_url)

        # Count initial items and categories
        categories = contents.get("categories", [])
        initial_project_count = 0
        initial_counts = {}

        for category in categories:
            category_items = contents.get(category, [])
            item_count = len(category_items)
            initial_counts[category] = item_count
            initial_project_count += item_count

        logging.info(f"Original contents has {initial_project_count} total projects across {len(categories)} categories")

        # Add new resources to their respective categories
        resources_added = 0
        resources_by_category = {}

        for resource in new_resources:
            category = resource.get("category")
            if category in contents:
                # Remove category from resource to match original format
                resource_copy = resource.copy()
                category_field = resource_copy.pop("category", None)

                contents[category].append(resource_copy)
                resources_added += 1

                # Track additions by category
                if category not in resources_by_category:
                    resources_by_category[category] = 0
                resources_by_category[category] += 1
            else:
                logging.warning(f"Category '{category}' not found in original contents, skipping resource: {resource.get('title', 'Untitled')}")

        # Generate filename with timestamp and project count
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        total_projects = initial_project_count + resources_added
        filename = f"contents_{timestamp}_{total_projects}_projects.json"
        filepath = os.path.join(output_dir, filename)

        # Write updated contents to file
        with open(filepath, 'w') as f:
            json.dump(contents, f, indent=JSON_INDENT)

        logging.info(f"Successfully saved combined contents to {filepath}")
        print(f"✅ COMBINED CONTENTS SAVED: {filepath}")
        print(f"  • Original projects: {initial_project_count}")
        print(f"  • New projects added: {resources_added}")
        print(f"  • Total projects: {total_projects}")

        return filepath, resources_by_category, initial_counts, total_projects

    except Exception as e:
        logging.error(f"Error generating combined contents: {e}")
        print(f"❌ ERROR: Could not generate combined contents: {e}")
        return None, {}, {}, 0


async def main():
    parser = argparse.ArgumentParser(description="Video Research Assistant")
    parser.add_argument("--contents", default="contents.json", help="Path to contents JSON file")
    parser.add_argument("--min-results", type=int, default=10, help="Minimum number of new resources to find")
    parser.add_argument("--time-limit", type=int, default=180, help="Time limit for each search in seconds")
    parser.add_argument("--global-timeout", type=int, default=14400, help="Global timeout for the entire process in seconds")
    parser.add_argument("--update", action="store_true", help="Update the contents file with new resources")
    parser.add_argument("--gen-awesome-list", action="store_true", help="Generate an awesome list from the contents")
    parser.add_argument("--verify", action="store_true", help="Verify an existing awesome list")
    parser.add_argument("--awesome-file", default="awesome-video.md", help="Path to the awesome list file")
    parser.add_argument("--randomize", action="store_true", help="Randomize the order of searches")
    parser.add_argument("--random-seed", type=int, help="Seed for randomization")
    parser.add_argument("--debug", action="store_true", help="Enable debug logging")
    parser.add_argument("--output-dir", default=None, help="Directory to store output files")
    parser.add_argument("--save-summary", action="store_true", help="Generate and save a research summary")
    args = parser.parse_args()

    start_time = time.time()

    # Create a timestamped directory for outputs if not specified
    if args.output_dir is None:
        timestamp = datetime.datetime.now().strftime("%Y%m%d")
        args.output_dir = f"research_results_{timestamp}"

    # Create the output directory if it doesn't exist
    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir, exist_ok=True)
        print(f"\n📁 Created output directory: {args.output_dir}")

    # Setup logging
    log_level = logging.DEBUG if args.debug else logging.INFO
    log_file = os.path.join(args.output_dir, "research.log")
    logger = setup_logging(log_level=log_level, log_file=log_file)

    try:
        # Print banner
        print("\n" + "="*70)
        print("🎬 AWESOME VIDEO STREAMING & ENCODING RESEARCHER")
        print("="*70)

        # Log environment info
        logger.info(f"Starting Awesome Video Streaming & Encoding Researcher script using OpenAI Agents SDK")
        logger.info(f"Python version: {sys.version}")
        logger.info(f"OS: {os.name}")
        print(f"\n🚀 STARTING RESEARCH PROCESS")
        print(f"  • Log file: {log_file}")
        print(f"  • Output directory: {args.output_dir}")
        print(f"  • Target new resources: {args.min_results}")
        print(f"  • Time limit per category: {args.time_limit} seconds")
        print(f"  • Global timeout: {args.global_timeout} seconds ({args.global_timeout/3600:.1f} hours)")
        if args.randomize:
            print(f"  • Category order: RANDOMIZED")
            if args.random_seed:
                print(f"  • Random seed: {args.random_seed}")

        # Check for OpenAI API key
        if "OPENAI_API_KEY" not in os.environ:
            logger.error("OPENAI_API_KEY environment variable is not set")
            print("\n❌ ERROR: OPENAI_API_KEY environment variable is not set")
            print("Please set it with: export OPENAI_API_KEY=your_api_key_here")
            return 1

        # Run system checks
        system_check_passed = await run_system_checks()
        if not system_check_passed:
            logger.warning("System checks failed, proceeding with caution")
            print("\n⚠️ System checks failed, proceeding with caution")

        # Load contents data
        try:
            contents_data = await load_contents(args.contents)
            logger.info(f"Successfully loaded contents data from {args.contents}")
            print(f"\n✅ Successfully loaded contents data from {args.contents}")
        except Exception as e:
            logger.error(f"Error loading contents data: {e}")
            print(f"\n❌ ERROR: Could not load contents data: {e}")
            return 1

        # Prepare for research
        manager = ResearchManager()

        # Execute research
        print(f"\n🔍 BEGINNING RESEARCH: Finding at least {args.min_results} new resources...")
        logger.info(f"Starting research with minimum {args.min_results} results, time limit {args.time_limit}s per category")

        # Execute research process
        start_research_time = time.time()
        code, new_resources, project_ideas = await manager.run(
            contents_data,
            min_results=args.min_results,
            time_limit=args.time_limit,
            global_timeout=args.global_timeout,
            randomize=args.randomize,
            random_seed=args.random_seed
        )
        research_time = time.time() - start_research_time

        # Save intermediate results
        await save_intermediate_results(new_resources, project_ideas, final=True, output_dir=args.output_dir)

        # Update contents file if requested
        if args.update and new_resources:
            logger.info(f"Updating contents with {len(new_resources)} new resources")
            print(f"\n📝 UPDATING CONTENTS WITH {len(new_resources)} NEW RESOURCES...")

            # Generate combined contents file
            combined_file, resources_by_category, initial_counts, total_projects = await generate_combined_contents(
                args.contents, new_resources, output_dir=args.output_dir
            )

            # Updated contents file
            if combined_file:
                logger.info(f"Contents update saved to {combined_file}")
                print(f"✅ CONTENTS UPDATE SAVED: {combined_file}")
            else:
                logger.error("Failed to update contents file")
                print("❌ Failed to update contents file")

        # Generate awesome list if requested
        if args.gen_awesome_list and (new_resources or args.update):
            logger.info("Generating Awesome List")
            print(f"\n📄 GENERATING AWESOME LIST...")

            # Determine input for awesome list - use combined file if available
            awesome_input = combined_file if args.update and combined_file else args.contents

            if awesome_input:
                try:
                    # Load the most recent contents for the awesome list
                    if awesome_input != args.contents:
                        awesome_data = await load_contents(awesome_input)
                    else:
                        awesome_data = contents_data

                    # Generate the awesome list
                    awesome_file = await generate_awesome_list(
                        awesome_data, new_resources,
                        output_file=args.awesome_file, output_dir=args.output_dir
                    )

                    if awesome_file:
                        logger.info(f"Awesome List generated: {awesome_file}")
                        print(f"✅ AWESOME LIST GENERATED: {awesome_file}")

                        # Verify awesome list format
                        if args.verify:
                            valid, errors = await verify_awesome_list(awesome_file)
                            if valid:
                                logger.info("Awesome List verification passed")
                            else:
                                logger.warning(f"Awesome List verification found {len(errors)} issues")
                except Exception as e:
                    logger.error(f"Error generating Awesome List: {e}")
                    print(f"❌ ERROR: Could not generate Awesome List: {e}")

        # Generate research summary if requested
        if args.save_summary:
            logger.info("Generating research summary")
            print(f"\n📊 GENERATING RESEARCH SUMMARY...")

            combined_file_path = None
            if 'combined_file' in locals() and combined_file:
                combined_file_path = combined_file

            resources_by_cat = None
            if 'resources_by_category' in locals() and resources_by_category:
                resources_by_cat = resources_by_category

            init_counts = None
            if 'initial_counts' in locals() and initial_counts:
                init_counts = initial_counts

            total_projs = None
            if 'total_projects' in locals() and total_projects:
                total_projs = total_projects

            # Generate the summary
            summary = await generate_research_summary(
                contents_data, new_resources, project_ideas, research_time,
                combined_file=combined_file_path,
                new_resources_by_category=resources_by_cat,
                initial_counts=init_counts,
                total_projects=total_projs
            )

            # Save the summary to a file
            summary_file = os.path.join(args.output_dir, f"research_summary_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")
            with open(summary_file, 'w') as f:
                f.write(summary)

            logger.info(f"Research summary saved to {summary_file}")
            print(f"✅ RESEARCH SUMMARY SAVED: {summary_file}")

            # Print summary to console
            print("\n" + summary)

        return 0
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        print(f"\n❌ ERROR: {e}")
        if args.debug:
            logger.exception("Detailed error information:")
            import traceback
            traceback.print_exc()
        return 1
    finally:
        # Always log completion
        elapsed_time = time.time() - start_time
        logger.info(f"Script execution completed in {elapsed_time:.2f} seconds")
        print(f"\n⏱️ TOTAL EXECUTION TIME: {elapsed_time:.2f} seconds ({elapsed_time/3600:.2f} hours)")


async def generate_research_summary(original_contents_data, new_resources, project_ideas, research_time, combined_file=None, new_resources_by_category=None, initial_counts=None, total_projects=None):
    """Generate a detailed summary report of the research process and findings.

    The summary includes:
    - Overall statistics (time taken, resources found, etc.)
    - Breakdown by category of what new resources were added
    - Analysis of which categories saw the most growth
    - Overview of new project ideas

    Returns a string containing the summary.
    """
    logging.info("Generating detailed research summary")
    print("\n📊 GENERATING DETAILED RESEARCH SUMMARY...")

    # Format time
    hours, remainder = divmod(research_time, 3600)
    minutes, seconds = divmod(remainder, 60)
    time_str = f"{int(hours)}h {int(minutes)}m {int(seconds)}s"

    # Get categories from original data
    categories = original_contents_data.get("categories", [])
    categories_data = original_contents_data.get("_categories_data", {})

    # Count new resources by category
    if not new_resources_by_category:
        new_resources_by_category = {}
        for resource in new_resources:
            category = resource.get("category", "uncategorized")
            if category not in new_resources_by_category:
                new_resources_by_category[category] = 0
            new_resources_by_category[category] += 1

    # Get original counts if not provided
    if not initial_counts:
        initial_counts = {}
        for category in categories:
            initial_counts[category] = len(original_contents_data.get(category, []))

    # Calculate growth percentages
    growth_percentages = {}
    for category in categories:
        if category in new_resources_by_category and category in initial_counts:
            original = initial_counts[category]
            new = new_resources_by_category[category]
            if original > 0:
                growth_percentages[category] = (new / original) * 100
            else:
                growth_percentages[category] = float('inf')  # Infinite growth from zero
        else:
            growth_percentages[category] = 0

    # Sort categories by growth and addition count
    sorted_by_growth = sorted(growth_percentages.items(), key=lambda x: x[1], reverse=True)
    sorted_by_additions = sorted(new_resources_by_category.items(), key=lambda x: x[1], reverse=True)

    # Start building summary text
    summary_lines = []

    # Header
    summary_lines.append("=" * 80)
    summary_lines.append("📊 DETAILED RESEARCH SUMMARY")
    summary_lines.append("=" * 80)
    summary_lines.append("")

    # Overall statistics
    summary_lines.append("📈 OVERALL STATISTICS")
    summary_lines.append("-" * 40)
    summary_lines.append(f"🕒 Total research time: {time_str}")
    summary_lines.append(f"🔍 Total new resources found: {len(new_resources)}")
    summary_lines.append(f"💡 Total new project ideas generated: {len(project_ideas)}")
    if combined_file:
        summary_lines.append(f"📁 Combined contents file: {combined_file}")
        if total_projects:
            summary_lines.append(f"📊 Total projects in combined file: {total_projects}")
    summary_lines.append("")

    # Breakdown by category
    summary_lines.append("📋 NEW RESOURCES BY CATEGORY")
    summary_lines.append("-" * 40)

    # Show top categories with most new resources
    if sorted_by_additions:
        summary_lines.append("Top categories with most new resources:")
        for i, (category, count) in enumerate(sorted_by_additions[:10], 1):
            cat_title = categories_data.get(category, {}).get("title", category)
            original = initial_counts.get(category, 0)
            growth = growth_percentages.get(category, 0)
            if growth == float('inf'):
                growth_str = "∞"
            else:
                growth_str = f"{growth:.1f}%"
            summary_lines.append(f"  {i}. {cat_title} ({category}): +{count} resources (from {original} to {original+count}, {growth_str} growth)")

    summary_lines.append("")
    summary_lines.append("Categories with highest growth percentage:")
    for i, (category, growth) in enumerate(sorted_by_growth[:10], 1):
        if growth > 0:
            cat_title = categories_data.get(category, {}).get("title", category)
            original = initial_counts.get(category, 0)
            new = new_resources_by_category.get(category, 0)
            if growth == float('inf'):
                growth_str = "∞"
            else:
                growth_str = f"{growth:.1f}%"
            summary_lines.append(f"  {i}. {cat_title} ({category}): {growth_str} growth (from {original} to {original+new})")

    summary_lines.append("")

    # Project idea overview
    if project_ideas:
        summary_lines.append("💡 PROJECT IDEAS OVERVIEW")
        summary_lines.append("-" * 40)

        # Count ideas by category
        ideas_by_category = {}
        for idea in project_ideas:
            category = idea.get("category", "uncategorized")
            if category not in ideas_by_category:
                ideas_by_category[category] = []
            ideas_by_category[category].append(idea)

        # Sort categories by number of ideas
        sorted_idea_categories = sorted(ideas_by_category.items(), key=lambda x: len(x[1]), reverse=True)

        # Show top categories with most ideas
        for i, (category, ideas) in enumerate(sorted_idea_categories[:5], 1):
            cat_title = categories_data.get(category, {}).get("title", category)
            summary_lines.append(f"{i}. {cat_title} ({category}): {len(ideas)} new project ideas")

            # List the top 3 ideas for this category
            for j, idea in enumerate(ideas[:3], 1):
                title = idea.get("title", "Untitled Idea")
                summary_lines.append(f"   {j}. {title}")

            if len(ideas) > 3:
                summary_lines.append(f"      ... and {len(ideas) - 3} more ideas")

            summary_lines.append("")

    # Conclusion
    summary_lines.append("=" * 80)
    summary_lines.append("🏁 RESEARCH SUMMARY COMPLETE")
    summary_lines.append("=" * 80)

    # Join all lines and return
    summary = "\n".join(summary_lines)

    # Log completion
    logging.info("Research summary generated successfully")
    print("✅ DETAILED RESEARCH SUMMARY GENERATED")

    return summary


if __name__ == "__main__":
    asyncio.run(main())


# cd /Users/nick/Desktop/awesome-video && python3 av-researcher-agents.py --contents https://hack-ski.s3.us-east-1.amazonaws.com/av/recategorized_projects_anthropic_claude_3_5_haiku_20241022_1743170712_1181.json --min-results 1000 --global-timeout 18000 --time-limit 300 --randomize --gen-awesome-list --update --debug --output-dir "research_results_$(date +%Y%m%d)" --save-summary