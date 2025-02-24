import re

def parse_ipa_file(file_path, output_file_path):
    ipa_dict = {}  # A dictionary to store word-IPA pairs
    
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()  # Remove any surrounding whitespace
            if line:  # Skip empty lines
                # Use regex to extract the word and IPA transcriptions
                match = re.match(r"(\S+)\s+\[(.*?)\]", line)
                if match:
                    word = match.group(1)  # The word
                    ipa_list = match.group(2).split("', '")  # Get the list of IPA transcriptions
                    
                    # Take only the first IPA transcription
                    first_ipa = ipa_list[0].strip("'")  # Remove the single quotes around the IPA
                    
                    # Remove stress symbols and dots
                    first_ipa = first_ipa.replace('ˈ', '').replace('.', '')
                    
                    ipa_dict[word] = first_ipa  # Store the word-IPA pair in the dictionary

    # Save the processed data to a new file
    with open(output_file_path, 'w') as output_file:
        for word, ipa in ipa_dict.items():
            output_file.write(f"{word} {ipa}\n")

# Example usage
file_path = "italian_nouns.txt"  # Replace with your input file path
output_file_path = "processed_ipa.txt"  # Replace with the desired output file path
parse_ipa_file(file_path, output_file_path)

print(f"Processed IPA data saved to {output_file_path}")
