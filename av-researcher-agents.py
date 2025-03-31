#!/usr/bin/env python3
"""
Awesome Video Researcher

This script uses the OpenAI Agents SDK to find new resources and generate
project ideas related to video creation and editing.
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
from typing import Dict, List, Any, Optional
import re

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
            resources related to video creation and editing.

            Your task is to generate search terms that will help find valuable, specific resources
            in a given category. Your search terms should be diverse, specific, and effective.
            """
        )

        # Create the prompt
        prompt = f"""
        I need to generate effective search terms for finding resources in the '{cat_title}' category
        of a video creation and editing resource collection.

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
            f"best {cat_title} tools",
            f"{cat_title} github repositories",
            f"{cat_title} tutorials",
            f"{cat_title} software",
            f"advanced {cat_title} techniques",
            f"{cat_title} for video"
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
            You are a Research Planner specializing in video creation and editing resources.
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
        for video creation and editing. Here's what I already have:

        Category Structure: {json.dumps(category_info, indent=2)}

        Existing data sample: {json.dumps(sample_data, indent=2)}

        Based on this information, please create a detailed research plan that includes:
        1. Priority categories to focus on (choose 8-12 diverse categories across different areas)
        2. Key search terms to use for each category (2-3 terms per category)
        3. Types of resources to look for
        4. Criteria for evaluating resources
        5. A structured approach to generating new project ideas

        IMPORTANT: Select a diverse range of categories - include some popular ones, some niche ones,
        and make sure to cover different aspects of video creation and editing. Try to include both
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
            You are a Resource Searcher specializing in finding high-quality resources related to video creation and editing.

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

            Each resource you find should include:
            1. A clear, concise title
            2. A detailed description explaining what the resource offers
            3. The URL of the resource (must be a DIRECT link to the content, not a search page)
            4. The category it belongs to
            5. Relevant tags (up to 5)
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

                Find 3-5 high-quality resources that would be valuable for people interested in video creation and editing.
                The resources MUST be SPECIFIC with DIRECT URLs - not search results or generic listings.

                GOOD examples:
                - GitHub repositories (e.g., "https://github.com/username/project-name")
                - Specific documentation (e.g., "https://ffmpeg.org/documentation.html")
                - Technical blog posts (e.g., "https://netflixtechblog.com/...")
                - Specific tutorial pages (e.g., "https://www.coursename.com/specific-tutorial")

                BAD examples (DO NOT INCLUDE THESE):
                - Google search results (e.g., "https://www.google.com/search?q=...")
                - YouTube search results (e.g., "https://www.youtube.com/results?search_query=...")
                - Generic listings pages

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
                        json_pattern = r'(\[[\s\S]*\])'
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

                    resources = json.loads(json_text)
                    logging.info(f"Successfully parsed JSON with {len(resources)} resources")

                    # Filter out search links and other invalid resources
                    valid_resources = []
                    for resource in resources:
                        url = resource.get("url", "").lower()
                        if not url:
                            logging.warning(f"Resource missing URL: {resource.get('title', 'Untitled')}")
                            continue

                        # Skip generic search results
                        if "google.com/search" in url or "youtube.com/results" in url:
                            logging.warning(f"Skipping search result URL: {url}")
                            continue

                        # Ensure URL seems legitimate
                        if url.startswith(("http://", "https://")) and "." in url:
                            valid_resources.append(resource)
                            logging.debug(f"Valid resource found: {resource.get('title', 'Untitled')} - {url}")
                        else:
                            logging.warning(f"Invalid URL format: {url}")

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
            You are a Project Idea Generator specializing in creative and practical project ideas for video creation and editing.

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
        3. Offer clear value to someone interested in video creation/editing
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
                    f"best {cat_title} tools",
                    f"{cat_title} software",
                    f"{cat_title} tutorials",
                    f"github {cat_title}",
                    f"{cat_title} for video editing"
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

        start_time = time.time()
        all_resources = []

        # Create tasks for each search
        tasks = []
        for search_term in search_terms:
            # Check if we're within the time limit
            if time.time() - start_time > time_limit:
                logging.warning(f"Time limit ({time_limit:.2f}s) reached for category '{category}'")
                print(f"\n⚠️ Time limit reached for this category, stopping searches")
                break

            # Create task
            task = asyncio.create_task(
                self._search(search_term, category, timeout=60)
            )
            tasks.append((search_term, task))

        # Process tasks as they complete
        for search_term, task in tasks:
            try:
                # Wait for the task with a timeout
                remaining_time = max(1, time_limit - (time.time() - start_time))
                resources = await asyncio.wait_for(task, timeout=remaining_time)

                if resources:
                    logging.info(f"Found {len(resources)} resources for '{search_term}'")
                    all_resources.extend(resources)

                    # If we've met our minimum, move to the next category
                    if len(all_resources) >= 10:  # Minimum threshold
                        logging.info(f"Found sufficient resources ({len(all_resources)}), stopping search")
                        print(f"\n✅ Found sufficient resources, stopping search for this category")
                        break
                else:
                    logging.warning(f"No resources found for '{search_term}'")
            except asyncio.TimeoutError:
                logging.warning(f"Search for '{search_term}' timed out")
                print(f"  ⚠️ Search for '{search_term}' timed out")
            except Exception as e:
                logging.error(f"Error searching for '{search_term}': {e}")
                print(f"  ❌ Error during search for '{search_term}': {e}")

        return all_resources

    async def _search(self, search_term, category, timeout=60):
        """Execute a single search using the search agent."""
        logging.info(f"Searching for: '{search_term}' in category '{category}'")
        print(f"\n🔍 SEARCHING: '{search_term}' in category '{category}'")

        try:
            resources = await self.search_agent.search(search_term, category, timeout=timeout)
            return resources
        except Exception as e:
            logging.error(f"Search error: {e}")
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
            instructions="You are a search agent for testing.",
            tools=[WebSearchTool()]
        )
        search_result = await Runner.run(web_search_agent, "Search for 'latest video editing software' and return one specific result with a direct URL (not a search page)")
        if search_result.final_output and len(search_result.final_output) > 10:
            # Check if it contains a valid URL
            import re
            url_pattern = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'
            urls = re.findall(url_pattern, search_result.final_output)

            if urls and not any(('google.com/search' in url or 'youtube.com/results' in url) for url in urls):
                results.append(("Web Search Tool", "PASS", f"Web search returned valid results with URLs"))
                print("  ✅ Web Search: Working properly with direct URLs")
            else:
                results.append(("Web Search Tool", "WARNING", f"Web search may only return search page URLs"))
                print("  ⚠️ Web Search: May return search page URLs instead of direct resources")
                print("    This will impact the script's ability to find valuable resources")
        else:
            results.append(("Web Search Tool", "WARNING", f"Web search returned limited results"))
            print("  ⚠️ Web Search: Returned limited results")
            print("    The script may struggle to find valuable resources")
    except Exception as e:
        results.append(("Web Search Tool", "FAIL", f"Error: {str(e)}"))
        checks_passed = False
        print(f"  ❌ Web Search: Failed: {str(e)}")
        print("    The web search functionality is CRITICAL for this script to work properly")
        print("    Without working web search, the script won't find any valuable resources")

    # Log results
    logging.info("System check results:")
    for check, status, message in results:
        if status == "PASS":
            logging.info(f"  ✓ {check}: {message}")
        elif status == "WARNING":
            logging.warning(f"  ⚠ {check}: {message}")
        else:
            logging.error(f"  ✗ {check}: {message}")

    return checks_passed


async def save_intermediate_results(resources, project_ideas, final=False):
    """Save intermediate results to a file."""
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

    filename = "new_projects.json" if final else f"intermediate_results_{int(time.time())}.json"

    with open(filename, 'w') as f:
        json.dump(results, f, indent=JSON_INDENT)

    logging.info(f"Saved {len(resources)} resources and {len(project_ideas)} project ideas to {filename}")

    if final:
        print(f"\n📁 FINAL RESULTS SAVED TO: {filename}")
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
        print(f"\n📁 INTERMEDIATE RESULTS SAVED: {filename}")

    return filename


async def update_contents(original_filepath_or_url, new_resources, new_project_ideas):
    """Update the original contents file or create a new file with the combined results."""
    logging.info(f"Updating contents with new findings")

    # For remote files, we can't update them directly
    is_remote = original_filepath_or_url.startswith(('http://', 'https://'))

    # Determine output file path
    if is_remote:
        output_filepath = "updated_contents.json"
        logging.info(f"Remote URL detected, results will be saved to: {output_filepath}")
    else:
        output_filepath = original_filepath_or_url

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
        if not is_remote:
            backup_path = f"{output_filepath}.bak.{int(time.time())}"
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

        return True
    except Exception as e:
        logging.error(f"Error updating contents: {e}")
        if is_remote:
            logging.error(f"Consider specifying a local output file instead of a remote URL")
        return False


async def main():
    """Main async function to run the research script."""
    start_time = time.time()

    # Parse arguments
    DEFAULT_CONTENTS_URL = "https://hack-ski.s3.us-east-1.amazonaws.com/av/recategorized_projects_anthropic_claude_3_5_haiku_20241022_1743170712_1181.json"
    parser = argparse.ArgumentParser(description="Awesome Video Researcher using OpenAI Agents SDK")
    parser.add_argument("--contents-file", dest="contents_file", default=DEFAULT_CONTENTS_URL,
                      help=f"Path to the contents.json file or URL to a remote JSON file (default: {DEFAULT_CONTENTS_URL})")
    parser.add_argument("--update", action="store_true", help="Update contents with new findings")
    parser.add_argument("--output", help="Path to save the output (if different from input)")
    parser.add_argument("--debug", action="store_true", help="Enable debug logging")
    parser.add_argument("--log-file", default="research.log", help="Path to the log file")
    parser.add_argument("--min-results", type=int, default=10, help="Minimum number of results to find")
    parser.add_argument("--time-limit", type=int, default=300, help="Maximum time in seconds to spend searching per category")
    parser.add_argument("--global-timeout", type=int, default=14400, help="Maximum time in seconds for the entire script (default: 4 hours)")
    parser.add_argument("--randomize", action="store_true", help="Randomize the order of categories to research")
    parser.add_argument("--random-seed", type=int, help="Random seed for reproducible randomization")
    parser.add_argument("--skip-checks", action="store_true", help="Skip system checks")
    args = parser.parse_args()

    # Setup logging
    log_level = logging.DEBUG if args.debug else logging.INFO
    logger = setup_logging(log_level=log_level, log_file=args.log_file)

    try:
        # Print banner
        print("\n" + "="*70)
        print("🎬 AWESOME VIDEO RESEARCHER")
        print("="*70)

        # Log environment info
        logger.info(f"Starting Awesome Video Researcher script using OpenAI Agents SDK")
        logger.info(f"Python version: {sys.version}")
        logger.info(f"OS: {os.name}")
        print(f"\n🚀 STARTING RESEARCH PROCESS")
        print(f"  • Log file: {args.log_file}")
        print(f"  • Contents source: {args.contents_file}")
        print(f"  • Minimum results: {args.min_results}")
        print(f"  • Time limit per category: {args.time_limit} seconds")
        print(f"  • Global timeout: {args.global_timeout} seconds ({args.global_timeout/3600:.2f} hours)")
        if args.randomize:
            print(f"  • Category order: RANDOMIZED")
            if args.random_seed:
                print(f"  • Random seed: {args.random_seed}")

        # Check for OpenAI API key
        if not os.environ.get("OPENAI_API_KEY"):
            logger.error("OPENAI_API_KEY environment variable is not set")
            print("\n❌ ERROR: OPENAI_API_KEY environment variable is not set")
            print("Please set it using: export OPENAI_API_KEY=your_api_key_here")
            return 1

        # Run system checks
        if not args.skip_checks:
            logger.info("Running system checks")
            print("\n🔍 RUNNING SYSTEM CHECKS...")
            try:
                checks_passed = await run_system_checks()
                if not checks_passed:
                    logger.error("System checks failed, cannot proceed")
                    print("\n❌ ERROR: System checks failed, cannot proceed without functional API")
                    return 1
                print("✅ System checks passed")
            except Exception as e:
                logger.error(f"Error during system checks: {e}")
                print(f"\n❌ ERROR during system checks: {e}")
                return 1
        else:
            logger.info("System checks skipped")
            print("⚠️ System checks skipped")

        # Load contents
        logger.info(f"Loading contents from {args.contents_file}")
        try:
            contents_data = await load_contents(args.contents_file)
        except Exception as e:
            logger.error(f"Error loading contents: {e}")
            print(f"\n❌ ERROR loading contents: {e}")
            return 1

        # Get categories and existing data
        categories = contents_data.get("categories", [])
        if not categories:
            logger.error("No categories found in contents file")
            print(f"\n❌ ERROR: No categories found in contents file")
            return 1

        logger.info(f"Found {len(categories)} categories")
        print(f"\n📊 FOUND {len(categories)} CATEGORIES:")
        for i, category in enumerate(categories[:10], 1):
            item_count = len(contents_data.get(category, []))
            cat_title = contents_data.get("_categories_data", {}).get(category, {}).get("title", category)
            print(f"  {i}. {cat_title} ({category}): {item_count} items")
        if len(categories) > 10:
            print(f"  ... and {len(categories) - 10} more categories")

        # Initialize research manager
        research_manager = ResearchManager()

        # Run the research process
        result_code, all_new_resources, all_project_ideas = await research_manager.run(
            contents_data,
            min_results=args.min_results,
            time_limit=args.time_limit,
            global_timeout=args.global_timeout,
            randomize=args.randomize,
            random_seed=args.random_seed
        )

        if result_code != 0:
            logger.error("Research process failed")
            print("\n❌ ERROR: Research process failed")
            return 1

        # Check if we had to stop due to timeout
        total_time = time.time() - start_time
        if total_time >= args.global_timeout:
            logger.warning(f"Script stopped due to global timeout of {args.global_timeout} seconds")
            print(f"\n⏱️ SCRIPT REACHED GLOBAL TIMEOUT LIMIT OF {args.global_timeout} SECONDS")

        if not all_new_resources:
            logger.warning("No resources found across all categories")
            print("\n⚠️ WARNING: No resources were found in any category")
            print("  This indicates there may be issues with the web search functionality")
            print("  Or your API key may not have web search capabilities")

        # Save final results even if empty
        final_results_file = await save_intermediate_results(all_new_resources, all_project_ideas, final=True)
        logger.info(f"Saved final results to {final_results_file}")

        # Update original contents if requested and if we found resources
        output_file = args.output if args.output else args.contents_file
        if args.update and all_new_resources:
            logger.info(f"Updating contents with new findings")
            print(f"\n🔄 UPDATING CONTENTS FILE WITH NEW FINDINGS")
            try:
                update_success = await update_contents(output_file, all_new_resources, all_project_ideas)
                if update_success:
                    logger.info(f"Successfully updated contents at {output_file}")
                    print(f"✅ Successfully updated contents at {output_file}")
                else:
                    logger.error(f"Failed to update contents")
                    print(f"❌ Failed to update contents")
            except Exception as e:
                logger.error(f"Error updating contents: {e}")
                print(f"❌ Error updating contents: {e}")

        # Log statistics
        elapsed_time = time.time() - start_time
        logger.info(f"Research completed in {elapsed_time:.2f} seconds")
        logger.info(f"Found {len(all_new_resources)} new resources and generated {len(all_project_ideas)} project ideas")

        print("\n" + "="*70)
        print("🎉 RESEARCH COMPLETED!")
        print("="*70)
        print(f"⏱️  Time taken: {elapsed_time:.2f} seconds ({elapsed_time/3600:.2f} hours)")
        print(f"🔍 Found {len(all_new_resources)} new resources")
        print(f"💡 Generated {len(all_project_ideas)} project ideas")
        print(f"📁 Results saved to: {final_results_file}")
        print("="*70 + "\n")

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


if __name__ == "__main__":
    asyncio.run(main())
