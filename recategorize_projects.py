#!/usr/bin/env python3
"""
Recategorize Projects Script

This script reads projects from a JSON file, uses AI services to determine the best
matching category and subcategory from a predefined structure, and outputs a new JSON
file with the updated categorization.

Usage:
    python recategorize_projects.py --provider openai --model gpt-4 --input contents.json --output contents_recategorized.json
    python recategorize_projects.py --provider anthropic --model claude-3-opus-20240229 --input contents.json --output contents_recategorized.json
"""

import json
import logging
import argparse
import os
import time
import sys
from typing import Dict, List, Any, Tuple, Optional
import openai
import anthropic
from datetime import datetime
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("recategorize.log"),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

# Hardcoded categories and subcategories
HARDCODED_DATA = {
    "title": "Awesome Video",
    "header": "# Awesome Video\n\nProjects are organized into detailed categories with extensive subcategories covering all aspects of video processing, streaming, encoding, and more.",
    "header_contributing": "Please refer to the contribution guidelines before adding new projects.",
    "categories": [
        {"title": "Intro & Learning", "id": "intro-learning", "description": "Fundamental concepts, history, and educational resources for video streaming."},
        {"title": "Introduction", "id": "introduction", "description": "A high-level overview of video as a medium, its technical basics and creative impact.", "parent": "intro-learning"},
        {"title": "Learning Resources", "id": "learning-resources", "description": "Curated articles, books, courses, and talks offering in-depth knowledge of video streaming.", "parent": "intro-learning"},
        {"title": "Tutorials & Case Studies", "id": "tutorials-case-studies", "description": "Practical tutorials and real-world case studies demonstrating video streaming implementations.", "parent": "intro-learning"},
        {"title": "Protocols & Transport", "id": "protocols-transport", "description": "Resources covering the protocols and transport mechanisms that drive video delivery."},
        {"title": "Adaptive Streaming", "id": "adaptive-streaming", "description": "Standards and tools for adaptive streaming, primarily focused on HLS and DASH.", "parent": "protocols-transport"},
        {"title": "HLS", "id": "hls", "description": "Dedicated resources, libraries, and tools for HTTP Live Streaming.", "parent": "adaptive-streaming"},
        {"title": "DASH", "id": "dash", "description": "Dedicated resources, libraries, and tools for Dynamic Adaptive Streaming over HTTP.", "parent": "adaptive-streaming"},
        {"title": "Transport Protocols", "id": "transport-protocols", "description": "Protocols that ensure reliable video transport such as RIST, SRT, and RTMP.", "parent": "protocols-transport"},
        {"title": "RIST", "id": "rist", "description": "Resources focused on the Reliable Internet Stream Transport protocol.", "parent": "transport-protocols"},
        {"title": "SRT", "id": "srt", "description": "Resources dedicated to the Secure Reliable Transport protocol.", "parent": "transport-protocols"},
        {"title": "RTMP", "id": "rtmp", "description": "Resources covering the Real-Time Messaging Protocol for video.", "parent": "transport-protocols"},
        {"title": "Encoding & Codecs", "id": "encoding-codecs", "description": "Technologies and tools for video encoding, transcoding, and codec implementation."},
        {"title": "Encoding Tools", "id": "encoding-tools", "description": "Utilities and libraries (including FFMPEG-based solutions) for encoding and transcoding video.", "parent": "encoding-codecs"},
        {"title": "FFMPEG", "id": "ffmpeg", "description": "Resources, configurations, and scripts based on FFMPEG for video processing.", "parent": "encoding-tools"},
        {"title": "Other Encoders", "id": "other-encoders", "description": "Additional encoding libraries and tools beyond FFMPEG.", "parent": "encoding-tools"},
        {"title": "Codecs", "id": "codecs", "description": "Implementations and libraries for modern video codecs.", "parent": "encoding-codecs"},
        {"title": "HEVC", "id": "hevc", "description": "Resources and tools for the HEVC (H.265) codec.", "parent": "codecs"},
        {"title": "VP9", "id": "vp9", "description": "Libraries, tools, and examples for the VP9 codec.", "parent": "codecs"},
        {"title": "AV1", "id": "av1", "description": "Resources and implementations for the emerging AV1 codec.", "parent": "codecs"},
        {"title": "Players & Clients", "id": "players-clients", "description": "Software and hardware solutions for video playback across platforms."},
        {"title": "Hardware Players", "id": "hardware-players", "description": "Dedicated players for devices like Roku, Smart TVs, and Chromecast.", "parent": "players-clients"},
        {"title": "Roku", "id": "roku", "description": "Tools, SDKs, and examples specific to Roku app development.", "parent": "hardware-players"},
        {"title": "Smart TVs", "id": "smart-tv", "description": "Player frameworks and SDKs tailored for Smart TV platforms.", "parent": "hardware-players"},
        {"title": "Chromecast", "id": "chromecast", "description": "Libraries and resources for developing Chromecast-enabled video apps.", "parent": "hardware-players"},
        {"title": "Mobile & Web Players", "id": "mobile-web-players", "description": "Playback solutions and SDKs for mobile devices and web browsers.", "parent": "players-clients"},
        {"title": "iOS/tvOS", "id": "ios-tvos", "description": "Tools and SDKs for video playback on Apple's iOS and tvOS platforms.", "parent": "mobile-web-players"},
        {"title": "Android", "id": "android", "description": "Player solutions and SDKs for Android devices and FireTV.", "parent": "mobile-web-players"},
        {"title": "Web Players", "id": "web-players", "description": "HTML5 and browser-based video players and frameworks.", "parent": "mobile-web-players"},
        {"title": "Media Tools", "id": "media-tools", "description": "Utilities to enhance and manage media content in video streaming workflows."},
        {"title": "Audio & Subtitles", "id": "audio-subtitles", "description": "Libraries and tools for audio processing and subtitle/caption integration.", "parent": "media-tools"},
        {"title": "Audio", "id": "audio", "description": "Tools for processing and managing audio streams within video content.", "parent": "audio-subtitles"},
        {"title": "Subtitles & Captions", "id": "subtitles-captions", "description": "Libraries and utilities for creating and managing subtitles and closed captions.", "parent": "audio-subtitles"},
        {"title": "Ads & QoE", "id": "ads-qoe", "description": "Resources for integrating advertising and measuring quality of experience (QoE) in video streaming.", "parent": "media-tools"},
        {"title": "Advertising", "id": "advertising", "description": "Tools and platforms focused on video advertising and monetization strategies.", "parent": "ads-qoe"},
        {"title": "Quality & Testing", "id": "quality-testing", "description": "Solutions for assessing video quality and testing streaming performance.", "parent": "ads-qoe"},
        {"title": "Standards & Industry", "id": "standards-industry", "description": "Official specifications, standards, and industry resources shaping video streaming."},
        {"title": "Specs & Standards", "id": "specs-standards", "description": "Documentation on official video streaming specifications, including MPEG standards and related forums.", "parent": "standards-industry"},
        {"title": "Official Specs", "id": "official-specs", "description": "Direct access to official technical specifications and standards documentation.", "parent": "specs-standards"},
        {"title": "MPEG & Forums", "id": "mpeg-forums", "description": "Resources covering MPEG standards and industry discussions about video technology.", "parent": "specs-standards"},
        {"title": "Vendors & HDR", "id": "vendors-hdr", "description": "Vendor-specific documentation and resources, including HDR guidelines and product specifications.", "parent": "standards-industry"},
        {"title": "Vendor Docs", "id": "vendor-docs", "description": "Technical documentation and support resources provided by industry vendors.", "parent": "vendors-hdr"},
        {"title": "HDR Guidelines", "id": "hdr-guidelines", "description": "Best practices and technical standards for implementing HDR in video streaming.", "parent": "vendors-hdr"},
        {"title": "Infrastructure & Delivery", "id": "infrastructure-delivery", "description": "Backend systems and cloud technologies that enable reliable video content delivery."},
        {"title": "Streaming Servers", "id": "streaming-servers", "description": "Software platforms for hosting video origins, managing storage, and serving content.", "parent": "infrastructure-delivery"},
        {"title": "Origin Servers", "id": "origin-servers", "description": "Solutions for origin server management and content distribution.", "parent": "streaming-servers"},
        {"title": "Storage Solutions", "id": "storage-solutions", "description": "Systems designed to store and manage large volumes of video content.", "parent": "streaming-servers"},
        {"title": "Cloud & CDN", "id": "cloud-cdn", "description": "Cloud platforms and content delivery network (CDN) integrations that optimize video delivery.", "parent": "infrastructure-delivery"},
        {"title": "Cloud Platforms", "id": "cloud-platforms", "description": "Orchestration and cloud service providers (e.g., Kubernetes, AWS, GCP) for streaming infrastructures.", "parent": "cloud-cdn"},
        {"title": "CDN Integration", "id": "cdn-integration", "description": "Tools and resources for integrating CDNs with video streaming services.", "parent": "cloud-cdn"},
        {"title": "General Tools", "id": "general-tools", "description": "Miscellaneous utilities that streamline video processing and security workflows."},
        {"title": "FFMPEG & Tools", "id": "ffmpeg-tools", "description": "A collection of FFMPEG-based scripts, libraries, and utilities for advanced video processing.", "parent": "general-tools"},
        {"title": "DRM", "id": "drm", "description": "Digital rights management solutions and resources to secure video content and manage licensing.", "parent": "general-tools"},
        {"title": "Community & Events", "id": "community-events", "description": "Resources and platforms that facilitate networking, collaboration, and industry events in video streaming."},
        {"title": "Community Groups", "id": "community-groups", "description": "Online communities, forums, Slack channels, and meetups for video professionals.", "parent": "community-events"},
        {"title": "Online Forums", "id": "online-forums", "description": "Dedicated discussion boards and online communities focused on video streaming technology.", "parent": "community-groups"},
        {"title": "Slack & Meetups", "id": "slack-meetups", "description": "Resources for real-time chat groups and local meetup events in the video streaming community.", "parent": "community-groups"},
        {"title": "Events & Conferences", "id": "events-conferences", "description": "A comprehensive list of conferences, talks, webinars, and podcasts related to video streaming.", "parent": "community-events"},
        {"title": "Conferences", "id": "conferences", "description": "Major industry conferences and live events dedicated to video streaming.", "parent": "events-conferences"},
        {"title": "Podcasts & Webinars", "id": "podcasts-webinars", "description": "Recorded talks, webinars, and podcasts sharing insights on video streaming trends and technology.", "parent": "events-conferences"}
    ]
}

def read_input_file(file_path: str) -> Dict[str, Any]:
    """
    Read the input JSON file.

    Args:
        file_path: Path to the input JSON file

    Returns:
        Dictionary containing the parsed JSON data
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        logger.info(f"Successfully read input file: {file_path}")
        logger.info(f"Found {len(data.get('projects', []))} projects in the input file")
        return data
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.error(f"Error reading input file: {e}")
        raise

def load_env_file():
    """
    Load environment variables from .env file if it exists.
    """
    env_path = Path('.env')
    if env_path.exists():
        logger.info("Loading environment variables from .env file")
        with open(env_path) as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#') or '=' not in line:
                    continue
                key, value = line.split('=', 1)
                os.environ[key.strip()] = value.strip().strip('"').strip("'")

def get_api_key(provider: str) -> str:
    """
    Get the API key for the specified provider from environment variables or .env file.

    Args:
        provider: The AI provider ('openai' or 'anthropic')

    Returns:
        The API key as a string
    """
    # Try to load from .env file first
    load_env_file()

    if provider == 'openai':
        api_key = os.environ.get('OPENAI_API_KEY')
        if not api_key:
            logger.error("OPENAI_API_KEY environment variable not set")
            raise ValueError("OPENAI_API_KEY environment variable not set. Please set it in your environment or in a .env file.")
        return api_key
    elif provider == 'anthropic':
        api_key = os.environ.get('ANTHROPIC_API_KEY')
        if not api_key:
            logger.error("ANTHROPIC_API_KEY environment variable not set")
            raise ValueError("ANTHROPIC_API_KEY environment variable not set. Please set it in your environment or in a .env file.")
        return api_key
    else:
        logger.error(f"Unsupported provider: {provider}")
        raise ValueError(f"Unsupported provider: {provider}")

def categorize_project_with_ai(
    project: Dict[str, Any],
    provider: str,
    model: str
) -> Tuple[str, str]:
    """
    Use AI to categorize a project into the best matching category and subcategory.

    Args:
        project: Dictionary containing project information
        provider: The AI provider to use ('openai' or 'anthropic')
        model: The model to use for the specified provider

    Returns:
        Tuple of (category_id, parent_category_id)
    """
    # Prepare the prompt with project information and categories
    categories_text = ""

    # Group categories by parents and top-level
    top_level_categories = []
    child_categories = {}

    for category in HARDCODED_DATA["categories"]:
        if "parent" not in category:
            top_level_categories.append(category)
        else:
            if category["parent"] not in child_categories:
                child_categories[category["parent"]] = []
            child_categories[category["parent"]].append(category)

    # Create hierarchical text representation
    for top_cat in top_level_categories:
        categories_text += f"Category: {top_cat['title']} (id: {top_cat['id']})\n"
        categories_text += f"Description: {top_cat['description']}\n"

        if top_cat["id"] in child_categories:
            categories_text += "Subcategories:\n"
            for sub_cat in child_categories[top_cat["id"]]:
                categories_text += f"  - {sub_cat['title']} (id: {sub_cat['id']}): {sub_cat['description']}\n"

                # Include third level categories if they exist
                if sub_cat["id"] in child_categories:
                    categories_text += "    Child categories:\n"
                    for child_cat in child_categories[sub_cat["id"]]:
                        categories_text += f"      - {child_cat['title']} (id: {child_cat['id']}): {child_cat['description']}\n"

        categories_text += "\n"

    prompt = f"""
You are a video technology expert tasked with categorizing projects into the most appropriate category.

Project Information:
- Title: {project.get('title', 'N/A')}
- Description: {project.get('description', 'N/A')}
- Homepage: {project.get('homepage', 'N/A')}
- Current category: {project.get('category', 'N/A')}

Available Categories:
{categories_text}

Based on the project information, determine the most appropriate category ID from the list above.
Choose the most specific category that applies to this project.

Respond in JSON format with only these fields:
{{
  "category_id": "the_most_appropriate_category_id",
  "reason": "A brief explanation of why this category was chosen",
  "tags": ["tag1", "tag2", "tag3"]
}}

The tags should be keywords that describe the project.
"""

    # Log the API call details
    log_api_call_start(provider, model, project)

    try:
        if provider == 'openai':
            return categorize_with_openai(prompt, model)
        elif provider == 'anthropic':
            return categorize_with_anthropic(prompt, model)
        else:
            logger.error(f"Unsupported provider: {provider}")
            raise ValueError(f"Unsupported provider: {provider}")
    except Exception as e:
        logger.error(f"Error during AI categorization: {e}")
        # Return a default categorization in case of error
        return "general-tools", "Miscellaneous error occurred during categorization"

def categorize_with_openai(prompt: str, model: str) -> Tuple[str, str]:
    """
    Use OpenAI to categorize a project.

    Args:
        prompt: The prompt to send to the OpenAI API
        model: The OpenAI model to use

    Returns:
        Tuple of (category_id, reason)
    """
    try:
        start_time = time.time()

        client = openai.OpenAI()
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a video technology expert that categorizes projects accurately."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2,
            max_tokens=150
        )

        elapsed_time = time.time() - start_time
        response_text = response.choices[0].message.content.strip()

        # Log the API response
        log_api_call_complete('openai', model, elapsed_time, response_text)

        # Parse the JSON response
        try:
            result = json.loads(response_text)
            return result.get("category_id"), result.get("reason")
        except json.JSONDecodeError:
            logger.error(f"Failed to parse OpenAI response as JSON: {response_text}")
            # Try to extract category ID using string parsing as fallback
            return extract_category_from_text(response_text)

    except Exception as e:
        logger.error(f"Error with OpenAI API: {e}")
        raise

def categorize_with_anthropic(prompt: str, model: str) -> Tuple[str, str]:
    """
    Use Anthropic to categorize a project.

    Args:
        prompt: The prompt to send to the Anthropic API
        model: The Anthropic model to use

    Returns:
        Tuple of (category_id, reason)
    """
    try:
        start_time = time.time()

        # Update the prompt to request only JSON without any explanatory text
        updated_prompt = prompt + "\n\nIMPORTANT: Respond with ONLY the JSON object, no additional text before or after."

        client = anthropic.Anthropic()
        response = client.messages.create(
            model=model,
            max_tokens=150,
            temperature=0.2,
            system="You are a video technology expert that categorizes projects accurately. Always respond with only a JSON object.",
            messages=[
                {"role": "user", "content": updated_prompt}
            ]
        )

        elapsed_time = time.time() - start_time
        response_text = response.content[0].text.strip()

        # Log the API response
        log_api_call_complete('anthropic', model, elapsed_time, response_text)

        # Parse the JSON response
        try:
            # Try to clean up the response if it still contains text before/after JSON
            if not response_text.startswith('{'):
                # Find the first opening brace
                start_idx = response_text.find('{')
                if start_idx != -1:
                    # Find the matching closing brace
                    end_idx = response_text.rfind('}')
                    if end_idx != -1 and end_idx > start_idx:
                        response_text = response_text[start_idx:end_idx+1]

            result = json.loads(response_text)
            return result.get("category_id"), result.get("reason")
        except json.JSONDecodeError:
            logger.error(f"Failed to parse Anthropic response as JSON: {response_text}")
            # Try to extract category ID using string parsing as fallback
            return extract_category_from_text(response_text)

    except Exception as e:
        logger.error(f"Error with Anthropic API: {e}")
        raise

def extract_category_from_text(text: str) -> Tuple[str, str]:
    """
    Extract category_id and reason from text when JSON parsing fails.

    Args:
        text: The response text from the AI service

    Returns:
        Tuple of (category_id, reason)
    """
    # Default fallback values
    default_category_id = "general-tools"
    default_reason = "Extracted using fallback method"

    # Look for patterns like "category_id: X" or "category: X"
    lines = text.split('\n')
    category_id = None
    reason = None

    for line in lines:
        line = line.strip().lower()
        if line.startswith("category_id:") or line.startswith("\"category_id\":"):
            category_text = line.split(":", 1)[1].strip().strip('"').strip("'").strip(",")
            # Find the closest matching category_id
            category_id = find_closest_match(category_text, [cat["id"] for cat in HARDCODED_DATA["categories"]])

        if line.startswith("reason:") or line.startswith("\"reason\":"):
            reason = line.split(":", 1)[1].strip().strip('"').strip("'").strip(",")

    # If we couldn't find a category_id or reason, use the defaults
    if not category_id:
        category_id = default_category_id
    if not reason:
        reason = default_reason

    return category_id, reason

def find_closest_match(text: str, options: List[str]) -> str:
    """
    Find the closest matching option for a given text.

    Args:
        text: The text to match
        options: List of possible options

    Returns:
        The closest matching option
    """
    # Simple implementation - just check if the text is contained in any option or vice versa
    text = text.lower()
    for option in options:
        if text in option.lower() or option.lower() in text:
            return option

    # If no match found, return the first option
    return options[0] if options else ""

def log_api_call_start(provider: str, model: str, project: Dict[str, Any]) -> None:
    """
    Log the start of an API call.

    Args:
        provider: The AI provider ('openai' or 'anthropic')
        model: The model being used
        project: The project being categorized
    """
    logger.info(f"API Call: {provider.upper()} - Model: {model}")
    logger.info(f"Project: {project.get('title', 'N/A')}")
    logger.info(f"Current category: {project.get('category', 'N/A')}")

def log_api_call_complete(provider: str, model: str, elapsed_time: float, response: str) -> None:
    """
    Log the completion of an API call.

    Args:
        provider: The AI provider ('openai' or 'anthropic')
        model: The model being used
        elapsed_time: Time taken for the API call
        response: The response from the API
    """
    logger.info(f"API Response: {provider.upper()} - Model: {model}")
    logger.info(f"Time taken: {elapsed_time:.2f} seconds")
    logger.info(f"Response: {response[:100]}..." if len(response) > 100 else f"Response: {response}")

def process_projects(
    input_data: Dict[str, Any],
    provider: str,
    model: str
) -> Dict[str, Any]:
    """
    Process all projects in the input data and categorize them.

    Args:
        input_data: Dictionary containing the input data
        provider: The AI provider to use ('openai' or 'anthropic')
        model: The model to use for the specified provider

    Returns:
        Dictionary containing the updated data
    """
    projects = input_data.get('projects', [])
    total_projects = len(projects)
    logger.info(f"Starting to process {total_projects} projects")
    print(f"Starting to process {total_projects} projects")

    # Create a copy of the input data to modify
    output_data = input_data.copy()
    output_data['projects'] = []

    # Add metadata about the categorization process
    output_data['metadata'] = {
        'provider': provider,
        'model': model,
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'total_projects': total_projects
    }

    # Dictionary to track category counts
    category_counts = {}

    for i, project in enumerate(projects):
        progress_msg = f"Processing project {i+1}/{total_projects} ({(i+1)/total_projects*100:.1f}%): {project.get('title', 'N/A')}"
        logger.info(progress_msg)
        print(progress_msg)

        try:
            # Get the category_id and reason from AI
            category_id, reason = categorize_project_with_ai(project, provider, model)

            # Update the project with the new category
            updated_project = project.copy()
            updated_project['new_category_id'] = category_id
            updated_project['categorization_reason'] = reason

            # Add to output data
            output_data['projects'].append(updated_project)

            # Update category counts
            if category_id not in category_counts:
                category_counts[category_id] = 0
            category_counts[category_id] += 1

            # Log the categorization
            logger.info(f"Categorized '{project.get('title', 'N/A')}' as {category_id}")

            # Add a small delay to avoid rate limiting
            time.sleep(0.5)

        except Exception as e:
            logger.error(f"Error processing project {project.get('title', 'N/A')}: {e}")
            # Add the project without categorization
            output_data['projects'].append(project)

    # Generate and log the summary
    summary = generate_summary(category_counts)
    logger.info("Categorization Summary:")
    logger.info(summary)

    return output_data

def generate_summary(category_counts: Dict[str, int]) -> str:
    """
    Generate a summary of the categorization results.

    Args:
        category_counts: Dictionary containing category_id counts

    Returns:
        String containing the summary
    """
    summary = []
    total_projects = sum(category_counts.values())

    summary.append(f"Total Projects Processed: {total_projects}\n")

    # Create a mapping of category_id to title for better reporting
    id_to_title = {cat["id"]: cat["title"] for cat in HARDCODED_DATA["categories"]}

    for category_id, count in sorted(category_counts.items(), key=lambda x: x[1], reverse=True):
        title = id_to_title.get(category_id, category_id)
        summary.append(f"{title} ({category_id}): {count} projects")

    return "\n".join(summary)

def write_output_file(data: Dict[str, Any], file_path: str) -> None:
    """
    Write the output data to a JSON file.

    Args:
        data: Dictionary containing the output data
        file_path: Path to the output JSON file
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        logger.info(f"Successfully wrote output file: {file_path}")
    except Exception as e:
        logger.error(f"Error writing output file: {e}")
        raise

def generate_output_filename(provider, model, input_file):
    """
    Generate an output filename that includes timestamp, provider, and model.

    Args:
        provider: The AI provider used
        model: The model used
        input_file: The input file path

    Returns:
        A filename string with timestamp, provider, and model
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    input_base = os.path.splitext(os.path.basename(input_file))[0]
    # Extract just the model name without version numbers if it's too long
    model_short = model.split('-')[0] if len(model) > 15 else model
    return f"{input_base}_recategorized_{provider}_{model_short}_{timestamp}.json"

def main():
    """Main function to run the script."""
    parser = argparse.ArgumentParser(description='Recategorize projects using AI services.')
    parser.add_argument('--provider', choices=['openai', 'anthropic'], default='anthropic',
                        help='AI provider to use (default: anthropic)')
    parser.add_argument('--model',
                        help='Model to use for the specified provider (default depends on provider)')
    parser.add_argument('--input', default='contents.json',
                        help='Path to the input JSON file (default: contents.json)')
    parser.add_argument('--output',
                        help='Path to the output JSON file (default: auto-generated with timestamp and provider)')

    args = parser.parse_args()

    # Set default model based on provider if not specified
    if not args.model:
        if args.provider == 'anthropic':
            args.model = 'claude-3-opus-20240229'  # Use the known working model
        else:
            args.model = 'gpt-4'

    # Generate output filename if not specified
    if not args.output:
        args.output = generate_output_filename(args.provider, args.model, args.input)

    logger.info(f"Starting recategorization with provider: {args.provider}, model: {args.model}")
    logger.info(f"Input file: {args.input}, Output file: {args.output}")

    try:
        # Get API key from environment variables
        get_api_key(args.provider)

        # Read input file
        input_data = read_input_file(args.input)

        # Process projects
        output_data = process_projects(input_data, args.provider, args.model)

        # Write output file
        write_output_file(output_data, args.output)

        logger.info("Recategorization completed successfully")

    except Exception as e:
        logger.error(f"Error during recategorization: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
