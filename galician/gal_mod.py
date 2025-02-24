import re

def process_first_bracketed_transcription(input_file, output_file):
    processed_data = []
    current_word = None  # To track the current word

    with open(input_file, 'r') as file:
        for line in file:
            line = line.strip()
            
            # Skip empty lines
            if not line:
                continue
            
            # Detect a new word (lines without indentation)
            if not line.startswith("IPA:"):
                current_word = line  # Update current word
                continue
            
            # Process IPA transcription lines
            if line.startswith("IPA:") and "[" in line:  # Look for [ ] transcription
                # Extract the transcription in square brackets
                match = re.search(r"\[([^\]]+)\]", line)
                if match and current_word:
                    ipa = match.group(1)  # Get the transcription
                    
                    # Remove stress markers and dots
                    ipa = ipa.replace("ˈ", "").replace(".", "")
                    
                    # Add the processed word and its IPA transcription to the list
                    processed_data.append(f"{current_word} {ipa}")
                    
                    # Stop after finding the first transcription for this word
                    current_word = None
                continue

    # Write the processed data to the output file
    with open(output_file, 'w') as out_file:
        out_file.write("\n".join(processed_data))
    print(f"Processed data saved to {output_file}")

# Example usage
input_file = "galician_nouns.txt"  # Replace with your input file
output_file = "processed_bracketed_output.txt"  # Replace with your desired output file
process_first_bracketed_transcription(input_file, output_file)


