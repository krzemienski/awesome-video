#!/usr/bin/env python3
"""
Automated Deep Research Script for the Awesome Video Project

This script performs automated deep research to find new resources and generate 
project ideas related to video creation and editing.
"""

import argparse
import json
import logging
import os
import sys
import time
import datetime
import hashlib
import re
import pickle
import unittest
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass
from urllib.parse import urlparse

import requests
import jsonschema
from tqdm import tqdm
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import openai

# Constants and configurations
DEFAULT_CACHE_DIR = ".cache"
OPENAI_MODEL = "gpt-4-turbo-preview"
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

# Setup logging
def setup_logging(log_level=logging.INFO):
    """Set up logging configuration."""
    logging.basicConfig(
        level=log_level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler('research.log')
        ]
    )
    return logging.getLogger(__name__)

# Cache management
class Cache:
    """Cache class for storing and retrieving search results."""
    
    def __init__(self, cache_dir=DEFAULT_CACHE_DIR):
        self.cache_dir = cache_dir
        os.makedirs(cache_dir, exist_ok=True)
    
    def _get_cache_path(self, key):
        """Generate a cache file path from a key."""
        hashed_key = hashlib.md5(key.encode()).hexdigest()
        return os.path.join(self.cache_dir, f"{hashed_key}.pickle")
    
    def get(self, key):
        """Retrieve a value from the cache."""
        cache_path = self._get_cache_path(key)
        if os.path.exists(cache_path):
            try:
                with open(cache_path, 'rb') as f:
                    timestamp, value = pickle.load(f)
                    # Cache expiry check (24 hours)
                    if time.time() - timestamp < 86400:
                        return value
            except Exception as e:
                logging.warning(f"Cache retrieval error: {e}")
        return None
    
    def set(self, key, value):
        """Store a value in the cache."""
        cache_path = self._get_cache_path(key)
        try:
            with open(cache_path, 'wb') as f:
                pickle.dump((time.time(), value), f)
            return True
        except Exception as e:
            logging.warning(f"Cache storage error: {e}")
            return False


# OpenAI API wrapper
class OpenAIClient:
    """Client class for OpenAI API interactions."""
    
    def __init__(self, api_key=None, model=OPENAI_MODEL, max_retries=3, retry_delay=2):
        if api_key is None:
            api_key = os.environ.get("OPENAI_API_KEY")
            if api_key is None:
                raise ValueError("OpenAI API key is required. Set OPENAI_API_KEY environment variable.")
        
        openai.api_key = api_key
        self.model = model
        self.max_retries = max_retries
        self.retry_delay = retry_delay
        self.cache = Cache(os.path.join(DEFAULT_CACHE_DIR, "openai"))
    
    def _make_request(self, messages, temperature=0, response_format=None):
        """Make a request to the OpenAI API with retry logic."""
        attempts = 0
        while attempts < self.max_retries:
            try:
                kwargs = {
                    "model": self.model,
                    "messages": messages,
                    "temperature": temperature,
                }
                
                if response_format:
                    kwargs["response_format"] = response_format
                
                response = openai.chat.completions.create(**kwargs)
                return response.choices[0].message.content
            except openai.RateLimitError:
                attempts += 1
                if attempts < self.max_retries:
                    sleep_time = self.retry_delay * (2 ** (attempts - 1))  # Exponential backoff
                    logging.warning(f"Rate limit exceeded. Retrying in {sleep_time} seconds...")
                    time.sleep(sleep_time)
                else:
                    raise
            except Exception as e:
                logging.error(f"OpenAI API error: {e}")
                raise
    
    def generate_response(self, prompt, system_message=None, temperature=0, response_format=None, use_cache=True):
        """Generate a response using the OpenAI API with optional caching."""
        messages = []
        
        if system_message:
            messages.append({"role": "system", "content": system_message})
        
        messages.append({"role": "user", "content": prompt})
        
        # Generate cache key from messages and parameters
        cache_key = json.dumps({
            "messages": messages,
            "temperature": temperature,
            "response_format": response_format,
            "model": self.model
        })
        
        if use_cache:
            cached_result = self.cache.get(cache_key)
            if cached_result:
                return cached_result
        
        result = self._make_request(messages, temperature, response_format)
        
        if use_cache:
            self.cache.set(cache_key, result)
        
        return result

    def generate_json_response(self, prompt, system_message=None, temperature=0, use_cache=True):
        """Generate a JSON response using the OpenAI API."""
        response = self.generate_response(
            prompt=prompt,
            system_message=system_message,
            temperature=temperature,
            response_format={"type": "json_object"},
            use_cache=use_cache
        )
        
        try:
            return json.loads(response)
        except json.JSONDecodeError as e:
            logging.error(f"Failed to parse JSON from OpenAI response: {e}")
            logging.debug(f"Raw response: {response}")
            raise


# NLP Utilities
class NLPUtils:
    """Natural Language Processing utilities."""
    
    def __init__(self):
        # Download necessary NLTK resources if not already downloaded
        try:
            nltk.data.find('tokenizers/punkt')
        except LookupError:
            nltk.download('punkt')
        
        try:
            nltk.data.find('corpora/stopwords')
        except LookupError:
            nltk.download('stopwords')
        
        self.stop_words = set(stopwords.words('english'))
    
    def extract_key_terms(self, text, num_terms=10):
        """Extract key terms from a text."""
        # Tokenize and convert to lowercase
        tokens = word_tokenize(text.lower())
        
        # Remove stop words and non-alphabetic tokens
        filtered_tokens = [word for word in tokens if word.isalpha() and word not in self.stop_words]
        
        # Count term frequency
        term_freq = {}
        for token in filtered_tokens:
            term_freq[token] = term_freq.get(token, 0) + 1
        
        # Return the most frequent terms
        return [term for term, _ in sorted(term_freq.items(), key=lambda x: x[1], reverse=True)[:num_terms]]
    
    def calculate_similarity(self, text1, text2):
        """Calculate similarity between two texts using Jaccard similarity."""
        tokens1 = set(word_tokenize(text1.lower()))
        tokens2 = set(word_tokenize(text2.lower()))
        
        # Filter out stop words
        tokens1 = {word for word in tokens1 if word.isalpha() and word not in self.stop_words}
        tokens2 = {word for word in tokens2 if word.isalpha() and word not in self.stop_words}
        
        # Calculate Jaccard similarity
        intersection = len(tokens1.intersection(tokens2))
        union = len(tokens1.union(tokens2))
        
        if union == 0:
            return 0
        
        return intersection / union


# Web search and content extraction
class WebResearcher:
    """Class for performing web research and content extraction."""
    
    def __init__(self, cache_dir=os.path.join(DEFAULT_CACHE_DIR, "web"), max_depth=2):
        self.cache = Cache(cache_dir)
        self.max_depth = max_depth
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
    
    def search(self, query, depth=1):
        """Perform a web search for a query."""
        # Check cache first
        cache_key = f"search:{query}:{depth}"
        cached_result = self.cache.get(cache_key)
        if cached_result:
            return cached_result
        
        # For demonstration purposes, using a mock search
        # In a real implementation, this would call a search API
        results = self._mock_search(query, depth)
        
        # Cache the results
        self.cache.set(cache_key, results)
        
        return results
    
    def _mock_search(self, query, depth):
        """Mock search function for demonstration purposes."""
        # This would be replaced with actual API calls in production
        return [
            {
                "title": f"Best {query} tools for video creators",
                "url": f"https://example.com/video-tools/{query.replace(' ', '-')}",
                "snippet": f"A comprehensive guide to the best {query} tools for video creators in 2023."
            },
            {
                "title": f"How to use {query} in your video projects",
                "url": f"https://videoguides.org/{query.replace(' ', '_')}-tutorial",
                "snippet": f"Learn how to effectively use {query} techniques in your video projects."
            },
            {
                "title": f"Top 10 {query} resources for filmmakers",
                "url": f"https://filmresources.net/top-{query.replace(' ', '-')}-resources",
                "snippet": f"Discover the top 10 {query} resources that every filmmaker should know about."
            }
        ]
    
    def extract_content(self, url):
        """Extract content from a URL."""
        # Check cache first
        cache_key = f"content:{url}"
        cached_result = self.cache.get(cache_key)
        if cached_result:
            return cached_result
        
        try:
            # In a real implementation, this would make an actual HTTP request
            # For demonstration, we'll return mock content
            content = f"<html><body><h1>Content about {url}</h1><p>This is sample content that would be extracted from {url}</p></body></html>"
            
            # Cache the result
            self.cache.set(cache_key, content)
            
            return content
        except Exception as e:
            logging.error(f"Error extracting content from {url}: {e}")
            return None


# Agent Classes
class Agent:
    """Base agent class."""
    
    def __init__(self, openai_client, name="Agent"):
        self.openai_client = openai_client
        self.name = name
    
    def _get_system_message(self):
        """Get the system message for this agent."""
        return f"You are {self.name}, an AI assistant specialized in research tasks."
    
    def process(self, input_data):
        """Process input data and return a response."""
        raise NotImplementedError("Subclasses must implement this method")


class PlannerAgent(Agent):
    """Agent responsible for planning research strategy and assigning tasks."""
    
    def __init__(self, openai_client):
        super().__init__(openai_client, "Research Planner")
    
    def _get_system_message(self):
        return (
            f"You are {self.name}, an AI assistant specialized in planning research strategies. "
            "Your role is to analyze the existing data, determine the most effective research "
            "approach, and create a structured plan with specific tasks for other agents to follow."
        )
    
    def create_research_plan(self, existing_data, categories):
        """Create a research plan based on existing data and categories."""
        prompt = (
            f"I need to create a research plan to find new resources and generate project ideas "
            f"for video creation and editing. Here's what I already have:\n\n"
            f"Categories: {json.dumps(categories)}\n\n"
            f"Existing data sample: {json.dumps(existing_data[:3] if len(existing_data) > 3 else existing_data)}\n\n"
            f"Based on this information, please create a detailed research plan that includes:\n"
            f"1. Priority categories to focus on\n"
            f"2. Key search terms to use for each category\n"
            f"3. Types of resources to look for\n"
            f"4. Criteria for evaluating resources\n"
            f"5. A structured approach to generating new project ideas\n\n"
            f"Return your response as a JSON object with the following structure:\n"
            f"{{\n"
            f"  \"priority_categories\": [list of category names in order of priority],\n"
            f"  \"search_terms\": {{\n"
            f"    \"category_name\": [list of search terms for this category],\n"
            f"    ...\n"
            f"  }},\n"
            f"  \"resource_types\": [list of resource types to look for],\n"
            f"  \"evaluation_criteria\": [list of criteria for evaluating resources],\n"
            f"  \"project_idea_generation\": [list of approaches for generating project ideas]\n"
            f"}}"
        )
        
        return self.openai_client.generate_json_response(prompt, system_message=self._get_system_message())


class SearchAgent(Agent):
    """Agent responsible for performing web searches and retrieving information."""
    
    def __init__(self, openai_client, web_researcher):
        super().__init__(openai_client, "Research Search Agent")
        self.web_researcher = web_researcher
    
    def _get_system_message(self):
        return (
            f"You are {self.name}, an AI assistant specialized in searching for and extracting "
            "relevant information from the web. Your role is to find high-quality resources "
            "related to specific search terms and extract the most valuable information."
        )
    
    def search_and_extract(self, search_term, category):
        """Search for resources related to a search term and extract relevant information."""
        # Perform web search
        search_results = self.web_researcher.search(search_term)
        
        if not search_results:
            return []
        
        resources = []
        for result in search_results:
            # Extract content from the URL
            content = self.web_researcher.extract_content(result["url"])
            
            if not content:
                continue
            
            # Use OpenAI to analyze and extract structured information
            prompt = (
                f"I found a web page related to '{search_term}' in the category '{category}'. "
                f"Here's the title and snippet from the search result:\n\n"
                f"Title: {result['title']}\n"
                f"Snippet: {result['snippet']}\n\n"
                f"Based on this information, please create a structured resource entry with the following:\n"
                f"1. A clear, concise title (use the original if appropriate)\n"
                f"2. A detailed description explaining what this resource offers\n"
                f"3. The URL of the resource\n"
                f"4. The category it belongs to (from: {category})\n"
                f"5. Relevant tags (up to 5)\n\n"
                f"Return your response as a JSON object with the following structure:\n"
                f"{{\n"
                f"  \"title\": \"Resource Title\",\n"
                f"  \"description\": \"Resource Description\",\n"
                f"  \"url\": \"{result['url']}\",\n"
                f"  \"category\": \"{category}\",\n"
                f"  \"tags\": [\"tag1\", \"tag2\", ...]\n"
                f"}}"
            )
            
            try:
                resource = self.openai_client.generate_json_response(prompt, system_message=self._get_system_message())
                resources.append(resource)
            except Exception as e:
                logging.error(f"Error generating resource for {result['url']}: {e}")
        
        return resources


class WriterAgent(Agent):
    """Agent responsible for generating new project ideas and descriptions."""
    
    def __init__(self, openai_client):
        super().__init__(openai_client, "Content Writer")
    
    def _get_system_message(self):
        return (
            f"You are {self.name}, an AI assistant specialized in generating creative and practical "
            "project ideas and writing clear, engaging descriptions. Your role is to create new "
            "project concepts based on existing data and research findings."
        )
    
    def generate_project_ideas(self, existing_data, new_resources, category, num_ideas=3):
        """Generate new project ideas based on existing data and new resources."""
        # Sample data to provide context
        sample_existing = existing_data[:3] if len(existing_data) > 3 else existing_data
        sample_new = new_resources[:3] if len(new_resources) > 3 else new_resources
        
        prompt = (
            f"I need you to generate {num_ideas} new project ideas for the category '{category}' "
            f"based on existing projects and newly found resources. Here's some context:\n\n"
            f"Existing projects: {json.dumps(sample_existing)}\n\n"
            f"Newly found resources: {json.dumps(sample_new)}\n\n"
            f"Please generate {num_ideas} unique, practical, and creative project ideas that:\n"
            f"1. Are relevant to the '{category}' category\n"
            f"2. Build upon the existing projects and new resources\n"
            f"3. Offer clear value to someone interested in video creation/editing\n"
            f"4. Include a compelling title and detailed description\n"
            f"5. Have relevant tags\n\n"
            f"Return your response as a JSON array with {num_ideas} objects using the following structure:\n"
            f"[\n"
            f"  {{\n"
            f"    \"title\": \"Project Idea Title\",\n"
            f"    \"description\": \"Detailed project description explaining the concept, approach, and value\",\n"
            f"    \"category\": \"{category}\",\n"
            f"    \"tags\": [\"tag1\", \"tag2\", ...]\n"
            f"  }},\n"
            f"  ...\n"
            f"]"
        )
        
        return self.openai_client.generate_json_response(prompt, system_message=self._get_system_message())


class ResearchManagerAgent(Agent):
    """Agent responsible for coordinating the overall research process."""
    
    def __init__(self, openai_client, planner, search_agent, writer):
        super().__init__(openai_client, "Research Manager")
        self.planner = planner
        self.search_agent = search_agent
        self.writer = writer
    
    def _get_system_message(self):
        return (
            f"You are {self.name}, an AI assistant specialized in coordinating research projects. "
            "Your role is to oversee the entire research process, ensure all tasks are completed "
            "properly, validate results, and provide status updates."
        )
    
    def validate_resource(self, resource):
        """Validate a resource against the schema."""
        try:
            jsonschema.validate(resource, RESOURCE_SCHEMA)
            return True
        except jsonschema.exceptions.ValidationError as e:
            logging.error(f"Resource validation error: {e}")
            return False
    
    def validate_project_idea(self, project_idea):
        """Validate a project idea against the schema."""
        try:
            jsonschema.validate(project_idea, PROJECT_IDEA_SCHEMA)
            return True
        except jsonschema.exceptions.ValidationError as e:
            logging.error(f"Project idea validation error: {e}")
            return False
    
    def filter_duplicates(self, items, existing_items, nlp_utils, similarity_threshold=0.7):
        """Filter out duplicate or highly similar items."""
        filtered_items = []
        
        for new_item in items:
            is_duplicate = False
            
            # Check against existing items
            for existing_item in existing_items:
                # Compare titles
                title_similarity = nlp_utils.calculate_similarity(
                    new_item.get("title", ""), 
                    existing_item.get("title", "")
                )
                
                # Compare descriptions
                desc_similarity = nlp_utils.calculate_similarity(
                    new_item.get("description", ""), 
                    existing_item.get("description", "")
                )
                
                # Check URL if available
                url_match = False
                if "url" in new_item and "url" in existing_item:
                    url_match = new_item["url"] == existing_item["url"]
                
                # Determine if it's a duplicate
                if (title_similarity > similarity_threshold or 
                    desc_similarity > similarity_threshold or 
                    url_match):
                    is_duplicate = True
                    break
            
            # Check against already filtered items
            if not is_duplicate:
                for filtered_item in filtered_items:
                    title_similarity = nlp_utils.calculate_similarity(
                        new_item.get("title", ""), 
                        filtered_item.get("title", "")
                    )
                    
                    desc_similarity = nlp_utils.calculate_similarity(
                        new_item.get("description", ""), 
                        filtered_item.get("description", "")
                    )
                    
                    if (title_similarity > similarity_threshold or 
                        desc_similarity > similarity_threshold):
                        is_duplicate = True
                        break
            
            if not is_duplicate:
                filtered_items.append(new_item)
        
        return filtered_items
    
    def execute_research(self, contents_data, progress_callback=None):
        """Execute the full research process and coordinate all agents."""
        # Extract categories and existing data
        categories = contents_data.get("categories", [])
        existing_data = []
        for category in categories:
            category_items = contents_data.get(category, [])
            for item in category_items:
                item["category"] = category
                existing_data.append(item)
        
        # Step 1: Create research plan
        logging.info("Creating research plan...")
        if progress_callback:
            progress_callback("Creating research plan...", 0.1)
        
        research_plan = self.planner.create_research_plan(existing_data, categories)
        
        # Initialize results storage
        new_resources = []
        new_project_ideas = []
        
        # Initialize NLP utilities
        nlp_utils = NLPUtils()
        
        # Step 2: Execute searches based on the plan
        priority_categories = research_plan.get("priority_categories", categories)
        search_terms = research_plan.get("search_terms", {})
        
        total_categories = len(priority_categories)
        for i, category in enumerate(priority_categories):
            logging.info(f"Researching category: {category}")
            progress_percent = 0.1 + (0.7 * (i / total_categories))
            if progress_callback:
                progress_callback(f"Researching category: {category}", progress_percent)
            
            # Get search terms for this category
            category_search_terms = search_terms.get(category, [])
            if not category_search_terms:
                # Generate search terms if none were provided
                category_data = [item for item in existing_data if item.get("category") == category]
                prompt = (
                    f"I need to research the '{category}' category for video creation and editing resources. "
                    f"Based on this sample of existing data: {json.dumps(category_data[:3] if len(category_data) > 3 else category_data)}, "
                    f"please generate 5-10 specific search terms that would help find new, valuable resources in this category. "
                    f"Return your response as a JSON array of strings."
                )
                try:
                    category_search_terms = self.openai_client.generate_json_response(prompt)
                    if isinstance(category_search_terms, dict) and "search_terms" in category_search_terms:
                        category_search_terms = category_search_terms["search_terms"]
                except Exception as e:
                    logging.error(f"Error generating search terms for {category}: {e}")
                    category_search_terms = [f"best {category} tools", f"{category} software", f"{category} tutorials"]
            
            # Execute searches for each term
            for search_term in tqdm(category_search_terms, desc=f"Searching {category}"):
                logging.info(f"Searching for: {search_term}")
                
                resources = self.search_agent.search_and_extract(search_term, category)
                
                # Validate resources
                valid_resources = []
                for resource in resources:
                    if self.validate_resource(resource):
                        valid_resources.append(resource)
                    else:
                        logging.warning(f"Invalid resource found: {resource}")
                
                # Filter out duplicates
                filtered_resources = self.filter_duplicates(
                    valid_resources, 
                    existing_data + new_resources, 
                    nlp_utils
                )
                
                new_resources.extend(filtered_resources)
                
                # Save intermediate results
                self._save_intermediate_results(new_resources, new_project_ideas)
            
            # Generate project ideas for this category
            logging.info(f"Generating project ideas for: {category}")
            
            category_data = [item for item in existing_data if item.get("category") == category]
            category_resources = [item for item in new_resources if item.get("category") == category]
            
            if category_resources:
                project_ideas = self.writer.generate_project_ideas(
                    category_data, 
                    category_resources, 
                    category
                )
                
                # Validate project ideas
                valid_ideas = []
                for idea in project_ideas:
                    if self.validate_project_idea(idea):
                        valid_ideas.append(idea)
                    else:
                        logging.warning(f"Invalid project idea found: {idea}")
                
                # Filter out duplicates
                filtered_ideas = self.filter_duplicates(
                    valid_ideas, 
                    [idea for idea in new_project_ideas if idea.get("category") == category], 
                    nlp_utils
                )
                
                new_project_ideas.extend(filtered_ideas)
                
                # Save intermediate results
                self._save_intermediate_results(new_resources, new_project_ideas)
        
        # Step 3: Final validation and compilation
        logging.info("Finalizing results...")
        if progress_callback:
            progress_callback("Finalizing results...", 0.9)
        
        # Final save
        self._save_intermediate_results(new_resources, new_project_ideas, final=True)
        
        if progress_callback:
            progress_callback("Research completed", 1.0)
        
        return {
            "new_resources": new_resources,
            "new_project_ideas": new_project_ideas
        }
    
    def _save_intermediate_results(self, resources, project_ideas, final=False):
        """Save intermediate results to a file."""
        results = {
            "new_resources": resources,
            "new_project_ideas": project_ideas,
            "timestamp": datetime.datetime.now().isoformat()
        }
        
        filename = "new_projects.json" if final else f"intermediate_results_{int(time.time())}.json"
        
        with open(filename, 'w') as f:
            json.dump(results, f, indent=2)
        
        logging.info(f"Saved {len(resources)} resources and {len(project_ideas)} project ideas to {filename}")


# Main functions
def load_contents(filepath):
    """Load contents from a JSON file."""
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except Exception as e:
        logging.error(f"Error loading contents file: {e}")
        raise


def update_contents(original_filepath, new_resources, new_project_ideas):
    """Update the original contents.json file with new findings."""
    try:
        # Load original contents
        with open(original_filepath, 'r') as f:
            contents = json.load(f)
        
        # Add new resources to their respective categories
        for resource in new_resources:
            category = resource.get("category")
            if category in contents:
                # Remove category from resource to match original format
                resource_copy = resource.copy()
                resource_copy.pop("category", None)
                contents[category].append(resource_copy)
        
        # Write updated contents back to file
        backup_path = f"{original_filepath}.bak"
        logging.info(f"Creating backup of original file at {backup_path}")
        with open(backup_path, 'w') as f:
            json.dump(contents, f, indent=2)
        
        with open(original_filepath, 'w') as f:
            json.dump(contents, f, indent=2)
        
        logging.info(f"Updated {original_filepath} with {len(new_resources)} new resources")
        return True
    except Exception as e:
        logging.error(f"Error updating contents file: {e}")
        return False


# Unit tests
class TestOpenAIClient(unittest.TestCase):
    """Unit tests for the OpenAIClient class."""
    
    def setUp(self):
        self.client = OpenAIClient()
    
    def test_generate_response(self):
        """Test that the generate_response method returns a string."""
        response = self.client.generate_response("Say hello", use_cache=False)
        self.assertIsInstance(response, str)
    
    def test_generate_json_response(self):
        """Test that the generate_json_response method returns a dict."""
        response = self.client.generate_json_response(
            "Return a JSON object with keys 'greeting' and 'value'", 
            use_cache=False
        )
        self.assertIsInstance(response, dict)


class TestNLPUtils(unittest.TestCase):
    """Unit tests for the NLPUtils class."""
    
    def setUp(self):
        self.nlp = NLPUtils()
    
    def test_extract_key_terms(self):
        """Test that extract_key_terms returns a list of terms."""
        text = "This is a test sentence about video editing software and animation tools."
        terms = self.nlp.extract_key_terms(text, num_terms=5)
        self.assertIsInstance(terms, list)
        self.assertGreater(len(terms), 0)
    
    def test_calculate_similarity(self):
        """Test that calculate_similarity returns a float between 0 and 1."""
        text1 = "Video editing software for beginners"
        text2 = "Beginner-friendly video editing tools"
        similarity = self.nlp.calculate_similarity(text1, text2)
        self.assertIsInstance(similarity, float)
        self.assertGreaterEqual(similarity, 0)
        self.assertLessEqual(similarity, 1)


# Main execution
def main():
    """Main function to run the script."""
    # Parse arguments
    parser = argparse.ArgumentParser(description="Automated deep research script for the Awesome Video project")
    parser.add_argument("contents_file", help="Path to the contents.json file")
    parser.add_argument("--update", action="store_true", help="Update the original contents.json file with new findings")
    parser.add_argument("--debug", action="store_true", help="Enable debug logging")
    args = parser.parse_args()
    
    # Setup logging
    logger = setup_logging(log_level=logging.DEBUG if args.debug else logging.INFO)
    
    try:
        # Load contents
        logger.info(f"Loading contents from {args.contents_file}")
        contents_data = load_contents(args.contents_file)
        
        # Initialize OpenAI client
        openai_client = OpenAIClient()
        
        # Initialize web researcher
        web_researcher = WebResearcher()
        
        # Initialize agents
        planner = PlannerAgent(openai_client)
        search_agent = SearchAgent(openai_client, web_researcher)
        writer = WriterAgent(openai_client)
        research_manager = ResearchManagerAgent(openai_client, planner, search_agent, writer)
        
        # Setup progress tracking
        progress_bar = tqdm(total=100, desc="Research Progress")
        
        def update_progress(message, progress):
            """Update progress bar"""
            progress_bar.set_description(message)
            progress_bar.update(int(progress * 100) - progress_bar.n)
        
        # Execute research
        logger.info("Starting research process")
        results = research_manager.execute_research(contents_data, update_progress)
        
        progress_bar.close()
        
        # Update original contents if requested
        if args.update:
            logger.info("Updating original contents file")
            update_contents(args.contents_file, results["new_resources"], results["new_project_ideas"])
        
        logger.info(f"Research completed: Found {len(results['new_resources'])} new resources and generated {len(results['new_project_ideas'])} project ideas")
        logger.info(f"Results saved to new_projects.json")
        
        return 0
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        if args.debug:
            logger.exception("Detailed error information:")
        return 1


if __name__ == "__main__":
    sys.exit(main())