#!/usr/bin/env python3
import json
import jsonschema
import sys
import re
import os
from copy import deepcopy

def slugify(text):
    """Convert a string to a slug format (lowercase, hyphens instead of spaces)"""
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'\s+', '-', text)
    return text

def generate_description(category_name):
    """Generate a description for a category"""
    descriptions = {
        "Video Players & Playback Libraries": "Libraries and tools for video playback across various platforms.",
        "Web Players": "Video players designed for web browsers and web applications.",
        "Mobile Players": "Video players optimized for mobile devices.",
        "Desktop Players": "Video players for desktop operating systems.",
        "Smart TV Players": "Video players for Smart TV platforms.",
        "Set-top Box Players": "Video players for set-top box devices.",
        "Embedded Players": "Video players for embedded systems.",
        "Frameworks & UI Components": "Frameworks and UI components for building video playback solutions.",
        "Browser Extensions": "Browser extensions for enhanced video playback.",
        "Video Editing & Processing Tools": "Tools for editing, processing, and manipulating video content.",
        "Trimming & Cutting Tools": "Tools for trimming, cutting, and splitting video files.",
        "Conversion & Format Tools": "Tools for converting video between different formats.",
        "Repair & Recovery Tools": "Tools for repairing and recovering corrupted video files.",
        "Non-linear Editing Suites": "Complete software suites for non-linear video editing.",
        "Effects & Compositing Tools": "Tools for adding effects and compositing video.",
        "Color Grading & Correction Tools": "Tools for color grading and correction in video.",
        "Subtitle & Caption Tools": "Tools for working with subtitles and captions in video.",
        "Batch Processing & Automation": "Tools for batch processing and automating video workflows.",
        "Video Encoding, Transcoding & Packaging Tools": "Tools for encoding, transcoding, and packaging video content.",
        "FFmpeg-Based Tools": "Tools built on or extending FFmpeg functionality.",
        "Hardware Accelerated Transcoding": "Tools utilizing hardware acceleration for video transcoding.",
        "Software Transcoding Tools": "Software-based tools for video transcoding.",
        "Scripting & Automation Tools": "Tools for scripting and automating video encoding workflows.",
        "Containerization & Packaging Tools": "Tools for containerizing and packaging video content.",
        "Cloud-Based Encoding Solutions": "Cloud-based solutions for video encoding.",
        "Multi-format Packaging Tools": "Tools for packaging video in multiple formats.",
        "Real-Time Encoding Solutions": "Solutions for real-time video encoding.",
        "Video Streaming & Distribution Solutions": "Solutions for streaming and distributing video content.",
        "Live Streaming Servers": "Servers designed for live video streaming.",
        "VOD Streaming Servers": "Servers for video-on-demand streaming.",
        "CDN Integration & Distribution": "Tools and services for integrating with Content Delivery Networks.",
        "RTMP/RTSP/HTTP Protocol Servers": "Servers supporting RTMP, RTSP, and HTTP streaming protocols.",
        "Peer-to-Peer Streaming Solutions": "Solutions using peer-to-peer technology for video streaming.",
        "Multi-CDN Management": "Tools for managing multiple Content Delivery Networks.",
        "Edge Computing & Caching Solutions": "Solutions leveraging edge computing and caching for video delivery.",
        "Streaming Analytics & Monitoring": "Tools for analytics and monitoring of video streams.",
        "Adaptive Streaming & Manifest Tools": "Tools for adaptive streaming and manifest manipulation.",
        "HLS Tools": "Tools specifically for HTTP Live Streaming (HLS).",
        "DASH Tools": "Tools for Dynamic Adaptive Streaming over HTTP (DASH).",
        "CMAF & fMP4 Packaging": "Tools for Common Media Application Format and fragmented MP4 packaging.",
        "HLS Manifest Parsers & Generators": "Tools for parsing and generating HLS manifests.",
        "DASH Manifest Tools": "Tools for working with DASH manifests.",
        "Encryption & DRM for Adaptive Streaming": "Solutions for encryption and DRM in adaptive streaming.",
        "Low-Latency Streaming Tools": "Tools optimized for low-latency video streaming.",
        "Adaptive Bitrate Algorithms & Tools": "Algorithms and tools for adaptive bitrate streaming.",
        "Media Analysis, Quality Metrics & AI Tools": "Tools for media analysis, quality metrics, and AI applications.",
        "Quality Analysis & Metrics": "Tools for analyzing and measuring video quality.",
        "Scene Detection & Segmentation": "Tools for detecting scenes and segmenting video.",
        "AI & Machine Learning Tools": "Tools leveraging AI and machine learning for video processing.",
        "Video Analytics & Benchmarking": "Tools for video analytics and benchmarking.",
        "Audio Analysis & Processing": "Tools for analyzing and processing audio in video.",
        "VMAF, PSNR, SSIM Tools": "Tools for VMAF, PSNR, and SSIM quality metrics.",
        "Color Science & Histogram Analysis": "Tools for color science and histogram analysis in video.",
        "Metadata Extraction & Management": "Tools for extracting and managing video metadata.",
        "Build Tools, Deployment & Utility Libraries": "Tools and libraries for building, deploying, and utility functions.",
        "Docker & Containerization Tools": "Docker and containerization tools for video workflows.",
        "Build Scripts & Automation": "Scripts and automation tools for building video applications.",
        "Command-line Utilities & Wrappers": "Command-line utilities and wrappers for video processing.",
        "API Libraries & SDKs": "API libraries and SDKs for video processing.",
        "Performance & Monitoring Tools": "Tools for monitoring and optimizing performance in video applications.",
        "CI/CD Pipelines for Media": "CI/CD pipelines specifically for media workflows.",
        "Standards, Specifications & Industry Resources": "Standards, specifications, and resources for the video industry."
    }
    
    return descriptions.get(category_name, "Resources and tools related to " + category_name.lower() + ".")

def transform_categories(categories):
    """Transform categories to match schema format"""
    transformed_categories = []
    category_map = {}  # Maps old category names to new category IDs
    
    # First, create all main categories
    for category in categories:
        cat_id = slugify(category["name"])
        transformed_category = {
            "title": category["name"],
            "id": cat_id,
            "description": generate_description(category["name"])
        }
        # Only include parent if it's not null
        # We don't add parent for main categories since it would be null
        
        transformed_categories.append(transformed_category)
        category_map[category["name"]] = cat_id
        
        # Then create all subcategories with parent reference
        if "subcategories" in category:
            for subcategory in category["subcategories"]:
                subcat_id = slugify(subcategory["name"])
                transformed_subcategory = {
                    "title": subcategory["name"],
                    "id": subcat_id,
                    "description": generate_description(subcategory["name"]),
                    "parent": cat_id  # Subcategories always have a parent
                }
                transformed_categories.append(transformed_subcategory)
                category_map[subcategory["name"]] = subcat_id
    
    return transformed_categories, category_map

def transform_projects(projects, category_map):
    """Transform projects to match schema format"""
    transformed_projects = []
    
    for project in projects:
        new_project = deepcopy(project)
        
        # Check if we need to update the category based on new_category
        if "new_category" in project:
            new_category = project["new_category"]
            
            # Check if there's also a new_subcategory
            if "new_subcategory" in project:
                new_subcategory = project["new_subcategory"]
                # If we have both new_category and new_subcategory, use subcategory
                if new_subcategory in category_map:
                    new_project["category"] = category_map[new_subcategory]
                elif new_category in category_map:
                    new_project["category"] = category_map[new_category]
            elif new_category in category_map:
                new_project["category"] = category_map[new_category]
            
            # Remove new_category field
            if "new_category" in new_project:
                del new_project["new_category"]
                
            # Remove new_subcategory field
            if "new_subcategory" in new_project:
                del new_project["new_subcategory"]
        
        # Make sure all required fields are present
        if "description" not in new_project:
            new_project["description"] = "A tool or resource for " + new_project.get("category", "video") + "."
            
        transformed_projects.append(new_project)
    
    return transformed_projects

def main():
    if len(sys.argv) != 2:
        print("Usage: python fix_json.py <input_json_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    
    # Determine output filename
    base_name = os.path.splitext(input_file)[0]
    output_file = base_name + "_fixed.json"
    
    # Load input JSON
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Load schema JSON
    schema_file = os.path.join(os.path.dirname(input_file), "schema.json")
    with open(schema_file, 'r', encoding='utf-8') as f:
        schema = json.load(f)
    
    # Save original project count
    original_project_count = len(data.get("projects", []))
    
    # Transform categories
    transformed_categories, category_map = transform_categories(data.get("categories", []))
    
    # Transform projects
    transformed_projects = transform_projects(data.get("projects", []), category_map)
    
    # Create new data structure
    new_data = {
        "title": data.get("title", "Awesome Video"),
        "header": data.get("header", ""),
        "header_contributing": data.get("header_contributing", ""),
        "categories": transformed_categories,
        "projects": transformed_projects
    }
    
    # Verify project count is preserved
    if len(transformed_projects) != original_project_count:
        print("WARNING: Project count mismatch! Original: " + str(original_project_count) + ", New: " + str(len(transformed_projects)))
    
    # Validate against schema
    try:
        jsonschema.validate(new_data, schema)
        print("Validation successful! Data conforms to schema.")
    except jsonschema.exceptions.ValidationError as e:
        print("Validation error: " + str(e))
        sys.exit(1)
    
    # Write output JSON
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(new_data, f, indent=2)
    
    print("Processed " + str(len(transformed_projects)) + " projects")
    print("Created " + str(len(transformed_categories)) + " categories")
    print("Fixed JSON saved to " + output_file)

if __name__ == "__main__":
    main()
