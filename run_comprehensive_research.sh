#!/bin/bash
source ~/.zshrc
# Comprehensive Video Streaming & Encoding Research
# This script runs the researcher with settings for a thorough 5-hour search targeting 1000 new resources

# Make sure OPENAI_API_KEY is set
if [ -z "$OPENAI_API_KEY" ]; then
  echo "ERROR: OPENAI_API_KEY environment variable is not set"
  echo "Please set it with: export OPENAI_API_KEY=your_api_key_here"
  exit 1
fi

# Create a timestamped directory for all outputs
timestamp=$(date +%Y%m%d)
results_dir="research_results_$timestamp"
mkdir -p "$results_dir"

# Start the research process
echo "Starting comprehensive video streaming & encoding research..."
echo "Target: 1000 new resources, timeout: 5 hours"

# Make sure Python can find the packages
export PYTHONPATH=$PYTHONPATH:$HOME/Library/Python/3.12/lib/python/site-packages

python av-researcher-agents.py \
  --min-results 1000 \
  --global-timeout 18000 \
  --time-limit 300 \
  --randomize \
  --gen-awesome-list \
  --update \
  --debug \
  --output-dir "$results_dir" \
  --save-summary

echo "Research process complete!"
