import json
import os
import logging
import requests
import time
import argparse
from openai import OpenAI
import anthropic  # Import Anthropic client

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Command-line arguments
def parse_args():
    parser = argparse.ArgumentParser(description="Categorize projects using AI APIs.")
    parser.add_argument("--json-url", type=str, default=os.getenv("JSON_URL", "https://example.com/path-to-your-json.json"), help="URL to fetch the JSON data")
    parser.add_argument("--output", type=str, default=None, help="Output filename (default: auto-generated with timestamp)")
    parser.add_argument("--provider", type=str, choices=["openai", "anthropic"], default=os.getenv("AI_PROVIDER", "openai"), help="AI provider to use (openai or anthropic)")
    parser.add_argument("--openai-key", type=str, default=os.getenv("OPENAI_API_KEY"), help="OpenAI API key")
    parser.add_argument("--anthropic-key", type=str, default=os.getenv("ANTHROPIC_API_KEY"), help="Anthropic API key")
    parser.add_argument("--openai-model", type=str, default=os.getenv("OPENAI_MODEL", "gpt-4o-mini"), help="OpenAI model to use")
    parser.add_argument("--anthropic-model", type=str, default=os.getenv("ANTHROPIC_MODEL", "claude-3-5-haiku-20241022"), help="Anthropic model to use")
    parser.add_argument("--limit", type=int, default=None, help="Number of projects to categorize (for testing purposes)")
    return parser.parse_args()


def fetch_json_from_url(url):
    logging.info(f"Fetching JSON data from URL: {url}")
    response = requests.get(url)
    response.raise_for_status()
    logging.info("JSON data fetched successfully")
    return response.json()


def save_json(data, filename):
    logging.info(f"Saving JSON data to '{filename}'")
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    logging.info("JSON data saved successfully")


def categorize_with_openai(client, project_text, categories, model, project_title, project_index, total_projects):
    """Categorize projects using OpenAI's API"""
    logging.info(f"Categorizing project {project_index}/{total_projects} with OpenAI: '{project_title}'")

    prompt = (
        "Categorize the following project into one of the provided categories. "
        "Provide a category_id, reason, and relevant tags.\n\n"
        f"Project Text:\n{project_text}\n\n"
        f"Categories:\n{json.dumps(categories, indent=2)}\n\n"
        "Respond with a JSON object containing 'category_id', 'reason', and 'tags'.\n\n"
        "Example of the expected response format:\n"
        "{\n"
        '  "category_id": "intro-learning",\n'
        '  "reason": "This is a learning resource that provides educational material about video processing",\n'
        '  "tags": ["tutorial", "education", "video"]\n'
        "}\n\n"
        "IMPORTANT: Return valid JSON only. Do not include any text before or after the JSON."
    )

    logging.debug(f"Prompt sent to OpenAI:\n{prompt}")

    # Use chat.completions API
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a video technology categorization expert. Always respond with valid JSON."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    # Get the response content from the chat completion
    response_content = response.choices[0].message.content
    logging.debug(f"Raw response from OpenAI: {response_content}")

    return parse_json_response(response_content)


def categorize_with_anthropic(client, project_text, categories, model, project_title, project_index, total_projects):
    """Categorize projects using Anthropic's API"""
    logging.info(f"Categorizing project {project_index}/{total_projects} with Anthropic: '{project_title}'")

    prompt = (
        "Categorize the following project into one of the provided categories. "
        "Provide a category_id, reason, and relevant tags.\n\n"
        f"Project Text:\n{project_text}\n\n"
        f"Categories:\n{json.dumps(categories, indent=2)}\n\n"
        "Respond with a JSON object containing 'category_id', 'reason', and 'tags'.\n\n"
        "Example of the expected response format:\n"
        "{\n"
        '  "category_id": "intro-learning",\n'
        '  "reason": "This is a learning resource that provides educational material about video processing",\n'
        '  "tags": ["tutorial", "education", "video"]\n'
        "}\n\n"
        "IMPORTANT: Return valid JSON only. Do not include any text before or after the JSON."
    )

    logging.debug(f"Prompt sent to Anthropic:\n{prompt}")

    try:
        response = client.messages.create(
            model=model,
            max_tokens=1000,
            temperature=0.2,
            system="You are a video technology categorization expert. Always respond with valid JSON.",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        # Extract the response text
        response_content = response.content[0].text
        logging.debug(f"Raw response from Anthropic: {response_content}")

        return parse_json_response(response_content)

    except Exception as e:
        logging.error(f"Error in Anthropic API call: {e}")
        raise


def parse_json_response(response_content):
    """Parse and extract JSON from AI response"""
    # Try to parse the JSON response, with error handling
    try:
        # Remove any markdown formatting if present
        if response_content.startswith("```json"):
            # Extract content between markdown code blocks
            content_parts = response_content.split("```")
            for part in content_parts:
                if part.strip() and not part.strip().startswith("json"):
                    response_content = part.strip()
                    break
        elif response_content.startswith("```"):
            # Handle unmarked code blocks
            content_parts = response_content.split("```")
            if len(content_parts) > 1:
                response_content = content_parts[1].strip()

        # Try to find JSON object if surrounded by other text
        if not response_content.startswith("{"):
            start_idx = response_content.find('{')
            end_idx = response_content.rfind('}')
            if start_idx != -1 and end_idx != -1 and end_idx > start_idx:
                response_content = response_content[start_idx:end_idx+1]

        return json.loads(response_content)
    except json.JSONDecodeError as e:
        logging.error(f"Error parsing JSON response: {e}")
        logging.error(f"Raw response: {response_content}")

        # Create a default response with a fallback category
        return {
            "category_id": "general-tools",
            "reason": f"Failed to parse model response. Defaulting to general category. Error: {str(e)}",
            "tags": ["auto-categorized", "parse-error"]
        }


def main():
    args = parse_args()
    provider = args.provider.lower()

    # Initialize the appropriate client based on provider
    if provider == "openai":
        if not args.openai_key:
            logging.error("OpenAI API key is required. Provide it via --openai-key argument or OPENAI_API_KEY environment variable.")
            return
        client = OpenAI(api_key=args.openai_key)
        model = args.openai_model
        logging.info(f"Using OpenAI with model: {model}")
    elif provider == "anthropic":
        if not args.anthropic_key:
            logging.error("Anthropic API key is required. Provide it via --anthropic-key argument or ANTHROPIC_API_KEY environment variable.")
            return
        client = anthropic.Anthropic(api_key=args.anthropic_key)
        model = args.anthropic_model
        logging.info(f"Using Anthropic with model: {model}")
    else:
        logging.error(f"Unsupported provider: {provider}")
        return

    data = fetch_json_from_url(args.json_url)
    projects = data.get("projects", [])

    categories = [
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

    timestamp = int(time.time())
    num_projects = len(projects) if args.limit is None else min(args.limit, len(projects))
    logging.info(f"Starting categorization of {num_projects} projects using {provider} with model {model}")

    # Generate output filename if not provided
    if args.output is None:
        args.output = f"recategorized_projects_{provider}_{model.replace('-', '_')}_{timestamp}_{num_projects}.json"
        logging.info(f"Auto-generated output filename: {args.output}")

    for idx, project in enumerate(projects[:num_projects], 1):
        title = project.get("title", "")
        description = project.get("description", "")
        project_text = f"Title: {title}\nDescription: {description}"

        if not title and not description:
            logging.warning("Skipping project without title and description")
            continue

        try:
            # Call the appropriate categorization function based on provider
            if provider == "openai":
                categorization_result = categorize_with_openai(client, project_text, categories, model, title, idx, num_projects)
            else:  # anthropic
                categorization_result = categorize_with_anthropic(client, project_text, categories, model, title, idx, num_projects)

            # Save the reason and tags but replace category with the new category_id
            project["category"] = categorization_result["category_id"]
            project["tags"] = categorization_result["tags"]

            # Remove the old category if it exists (it will be replaced)
            if "new_category" in project:
                del project["new_category"]
            if "categorization_reason" in project:
                del project["categorization_reason"]

            logging.info(f"Categorized '{title}' as '{categorization_result['category_id']}' with reason: '{categorization_result['reason'][:50]}...'")
        except Exception as e:
            logging.error(f"Error categorizing '{title}': {e}")
            # Add default values in case of error
            project["category"] = "general-tools"
            project["tags"] = ["error", "auto-categorized"]

            # Remove the old fields if they exist
            if "new_category" in project:
                del project["new_category"]
            if "categorization_reason" in project:
                del project["categorization_reason"]

    # Update output data with the new structure
    output_data = {
        "title": data.get("title", "Awesome Video"),
        "header": data.get("header", ""),
        "header_contributing": data.get("header_contributing", ""),
        "categories": categories,  # Use the new categories as the primary categories
        "model_used": model,
        "provider": provider,
        "timestamp": timestamp,
        "project_count": num_projects,
        "projects": projects[:num_projects]
    }

    save_json(output_data, args.output)
    logging.info(f"Categorization complete. Output saved to '{args.output}'")


if __name__ == "__main__":
    main()
