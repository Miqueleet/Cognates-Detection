import re

# Function to read the input text from a file
def read_input_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

# Function to write the result to an output file
def write_output_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

# Function to clean IPA transcription by removing periods, stress markers, and handling common symbols
def clean_ipa(ipa):
    # Remove stress markers and periods
    ipa = ipa.replace('.', '').replace('ˈ', '')

    # Return the cleaned IPA
    return ipa

# Define the regex pattern to match the word and its IPA lines
pattern = r'(?P<word>\w+)\n(?P<ipa_lines>(?:\s+IPA:\s*[/\[][^\]/\]]+[/\]]\s*\(Tags: [^)]+\)\n?)+)'

# Define the regex pattern to extract only one IPA line with `(Tags: Portugal)`
ipa_line_pattern = r'IPA:\s*[/\[]([^/\]]+)[/\]]\s*\(Tags: Portugal\)'

# Read the input from a .txt file
input_text = read_input_file("portuguese_nouns.txt")

# Find all matches for words and their IPA sections
matches = re.finditer(pattern, input_text)

# Output list to store the final cleaned results
output = []

for match in matches:
    word = match.group("word")  # Extract the word
    ipa_lines = match.group("ipa_lines")  # Extract the IPA lines
    
    # Extract only the first Portuguese-specific IPA transcription
    ipa_match = re.search(ipa_line_pattern, ipa_lines)
    if ipa_match:
        cleaned_ipa = clean_ipa(ipa_match.group(1))  # Clean the IPA transcription
        output.append(f"{word} {cleaned_ipa}")

# Join all output lines into a single string with line breaks
result = "\n".join(output)

# Print the result to the console (optional)
print(result)

# Write the result to an output file
write_output_file("output.txt", result)
