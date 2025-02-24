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

# Define the regex patterns for each region
ipa_patterns = {
    "Central": r'IPA:\s*[/\[]([^/\]]+)[/\]]\s*\(Tags:.*?\bCentral\b.*?\)',
    "Valencia": r'IPA:\s*[/\[]([^/\]]+)[/\]]\s*\(Tags:.*?\bValencia\b.*?\)',
    "Balearic": r'IPA:\s*[/\[]([^/\]]+)[/\]]\s*\(Tags:.*?\bBalearic\b.*?\)'
}

# Read the input from a .txt file
input_text = read_input_file("catalan_nouns.txt")

# Dictionary to store the results for each region
output_dict = {
    "Central": [],
    "Valencia": [],
    "Balearic": []
}

# Find all matches for words and their IPA sections
matches = re.finditer(pattern, input_text)

for match in matches:
    word = match.group("word")  # Extract the word
    ipa_lines = match.group("ipa_lines")  # Extract the IPA lines
    
    # Process each region and extract matching IPA transcriptions
    for region, ipa_pattern in ipa_patterns.items():
        ipa_matches = re.finditer(ipa_pattern, ipa_lines)  # Find all matches for the region
        for ipa_match in ipa_matches:
            cleaned_ipa = clean_ipa(ipa_match.group(1))  # Clean the IPA transcription
            output_dict[region].append(f"{word} {cleaned_ipa}")

# Write the results to separate files
for region, lines in output_dict.items():
    # Ensure each word appears only once per region (removing duplicates)
    unique_lines = sorted(set(lines))
    result = "\n".join(unique_lines)
    write_output_file(f"output_{region.lower()}.txt", result)
