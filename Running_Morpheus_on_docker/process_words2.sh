#!/bin/bash

# Variables
INPUT_FILE="/mnt/gnt_words.txt"                # Input file with GNT words
OUTPUT_FILE="/mnt/gnt_morphology_results2.txt"  # Output file for morphology results
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
    if [[ -n "$word" ]]; then
        result=$(echo "$word" | MORPHLIB=$MORPHLIB_PATH $CRUNCHER_COMMAND)

        if [[ -n "$result" ]]; then
            echo "$word => $result" >> "$OUTPUT_FILE"
        else
            echo "$word => (no result)" >> "$OUTPUT_FILE"
        fi
    fi
done < "$INPUT_FILE"

echo "Morphology lookup complete. Results saved to '$OUTPUT_FILE'."
