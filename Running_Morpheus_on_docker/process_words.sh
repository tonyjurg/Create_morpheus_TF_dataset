#!/bin/bash

# Variables
INPUT_FILE="/mnt/gnt_words.txt"                # Input file with GNT words
OUTPUT_FILE="/mnt/gnt_morphology_results.txt"  # Output file for morphology results
CRUNCHER_COMMAND="/morpheus/bin/cruncher"      # Path to the cruncher command
MORPHLIB_PATH="/morpheus/stemlib"              # Path to the morphology library

# Check if the input file exists
if [[ ! -f "$INPUT_FILE" ]]; then
    echo "Error: Input file '$INPUT_FILE' not found."
    exit 1
fi

# Clear or create the output file
> "$OUTPUT_FILE"

echo "Processing words in '$INPUT_FILE'..."

# Process each word
while IFS= read -r word; do
    # Run cruncher and capture the result
    result=$(echo "$word" | MORPHLIB=$MORPHLIB_PATH $CRUNCHER_COMMAND -d -S)

    # Append the result to the output file
    if [[ -n "$result" ]]; then
        echo "Word: $word" >> "$OUTPUT_FILE"
        echo "$result" >> "$OUTPUT_FILE"
        echo "-----------------------------" >> "$OUTPUT_FILE"
    else
        echo "Word: $word" >> "$OUTPUT_FILE"
        echo "Error: No response for '$word'" >> "$OUTPUT_FILE"
        echo "-----------------------------" >> "$OUTPUT_FILE"
    fi
done < "$INPUT_FILE"

echo "Morphology lookup complete. Results saved to '$OUTPUT_FILE'."