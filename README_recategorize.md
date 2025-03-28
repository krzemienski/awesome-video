# Project Recategorization Script

This script recategorizes video-related projects using AI services (OpenAI or Anthropic) to determine the best matching category and subcategory from a predefined structure.

## Features

- Reads projects from a JSON file
- Uses AI services (OpenAI or Anthropic) to categorize projects
- Logs detailed information about API calls and results
- Shows high-level progress information during processing
- Generates a summary of categorization results
- Creates a new JSON file with updated categorization
- Robust error handling and JSON parsing

## Requirements

- Python 3.7+
- Required Python packages:
  - openai
  - anthropic
  - argparse
  - json
  - logging

## Installation

1. Clone the repository or download the script
2. Install the required packages:

```bash
pip install -r requirements.txt
```

3. Set up your API keys as environment variables:

```bash
# For OpenAI
export OPENAI_API_KEY=your_openai_api_key

# For Anthropic
export ANTHROPIC_API_KEY=your_anthropic_api_key
```

   Alternatively, you can copy the `.env.example` file to `.env` and fill in your API keys:

```bash
cp .env.example .env
# Edit the .env file with your API keys
```

## Usage

### Using the Python Script Directly

```bash
# Using default settings (Anthropic with claude-3-opus-20240229)
python recategorize_projects.py

# Using OpenAI
python recategorize_projects.py --provider openai --model gpt-4

# Using Anthropic with a specific model
python recategorize_projects.py --provider anthropic --model claude-3-opus-20240229

# Specifying input file
python recategorize_projects.py --input contents.json
```

### Using the Shell Script

For convenience, you can also use the provided shell script:

```bash
# Using default settings (Anthropic with claude-3-opus-20240229)
./run_recategorize.sh

# Using OpenAI
./run_recategorize.sh --provider openai --model gpt-4

# Using Anthropic with a specific model
./run_recategorize.sh --provider anthropic --model claude-3-opus-20240229

# Specifying input and output files
./run_recategorize.sh --input contents.json --output new_categories.json
```

### Command-line Arguments

- `--provider`: AI provider to use (`openai` or `anthropic`, default: `anthropic`)
- `--model`: Model to use for the specified provider (default: `claude-3-opus-20240229` for Anthropic, `gpt-4` for OpenAI)
- `--input`: Path to the input JSON file (default: `contents.json`)
- `--output`: Path to the output JSON file (default: auto-generated with timestamp and provider, e.g., `contents_recategorized_anthropic_20250313_184523.json`)

## Output

The script generates:

1. A log file (`recategorize.log`) with detailed information about the categorization process
2. A JSON file with the updated categorization, which includes:
   - All original project data
   - New fields: `new_category` and `new_subcategory` for each project
   - The filename includes a timestamp and the provider used (e.g., `contents_recategorized_anthropic_20250313_184523.json`)
3. A summary of how many projects were assigned to each category and subcategory (printed to the console and log file)

## How It Works

1. The script reads the input JSON file containing projects
2. For each project, it sends a request to the specified AI service with project information and available categories
3. The AI service determines the best matching category and subcategory
4. The script updates the project with the new categorization
5. Progress is displayed in real-time, showing which project is being processed and the overall completion percentage
6. After processing all projects, it generates a summary and writes the updated data to the output file

## Testing

A test script is included to help verify the functionality:

```bash
# Run the test script with default settings
python test_recategorize.py

# Run the test script with specific provider
python test_recategorize.py --provider openai
```

The test script creates a small sample JSON file with a few projects and runs the recategorization script on it to demonstrate how it works.

## Error Handling

- If the AI service fails to categorize a project, it falls back to a default category
- All errors are logged to the log file
- The script continues processing even if some projects fail

## Example Summary Output

```
Total Projects Processed: 150

Video Players & Playback Libraries: 45 projects
  - Web Players: 20 projects
  - Mobile Players: 15 projects
  - Desktop Players: 10 projects

Video Encoding, Transcoding & Packaging Tools: 35 projects
  - FFmpeg-Based Tools: 15 projects
  - Software Transcoding Tools: 10 projects
  - Hardware Accelerated Transcoding: 10 projects

