import re

# Function to read the input text from a file
def read_input_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

# Function to write the result to an output file
def write_output_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

# Regular expression to capture the word and its first IPA transcription inside square brackets
pattern = r"(\S+)\s*IPA:\s*/[^/]+/\s*IPA:\s*\[([^\]]+)\]"

# Function to clean IPA transcription by removing periods, stress markers, and handling common symbols
def clean_ipa(ipa):
    # Remove stress markers and periods
    ipa = ipa.replace('.', '').replace('ˈ', '')

    # Return the cleaned IPA
    return ipa

# Read the input from a .txt file
input_text = read_input_file("spanish_nouns.txt")

# Find all matches using the regular expression
matches = re.findall(pattern, input_text)

# Output the word and its cleaned IPA transcription
output = []
for word, ipa in matches:
    cleaned_ipa = clean_ipa(ipa)  # Clean the IPA transcription
    output.append(f"{word} {cleaned_ipa}")  # Append the word and the cleaned IPA

# Join all output lines into a single string with line breaks
result = "\n".join(output)

# Print the result to the console (optional)
print(result)

# Write the result to an output file
write_output_file("output.txt", result)
