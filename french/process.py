import re

# Function to read the input text from a file
def read_input_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

# Function to write the result to an output file
def write_output_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

# Function to clean and deduplicate IPA transcriptions
def deduplicate_transcriptions(input_text):
    # Define the regex pattern to match words and their IPA transcriptions
    pattern = r'(?P<word>\S+)\n(?:\s+IPA:\s*(?P<ipa>[/\[][^\]/\]]+[/\]].*?)(?:\n|$))+'

    # Dictionary to store words and their first transcription
    word_transcriptions = {}

    # Find all matches in the input text
    matches = re.finditer(pattern, input_text)

    for match in matches:
        word = match.group("word")  # Extract the word
        ipa_transcriptions = re.findall(r'IPA:\s*([/\[][^\]/\]]+[/\]])', match.group(0))
        
        # Keep only the first transcription for the word
        if word not in word_transcriptions and ipa_transcriptions:
            word_transcriptions[word] = ipa_transcriptions[0].strip()

    # Format the results into a sorted output
    output_lines = [f"{word} {ipa}" for word, ipa in sorted(word_transcriptions.items())]
    return "\n".join(output_lines)

# Read the input data
input_file = "french_nouns.txt"  # Replace with your input file path
input_text = read_input_file(input_file)

# Process the input data
deduplicated_output = deduplicate_transcriptions(input_text)

# Write the deduplicated output to a file
output_file = "output.txt"  # Replace with your desired output file path
write_output_file(output_file, deduplicated_output)
