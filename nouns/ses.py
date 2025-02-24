import re

def read_file(file_path):
    """Read the content of a file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def write_file(file_path, content):
    """Write content to a file."""
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def apply_replacements(text, replacements):
    """Apply a list of replacements to the text."""
    for old, new in replacements.items():
        text = re.sub(old, new, text)
    return text

def process_text(file_path, language):
    """Process the text file based on the chosen language."""
    # Define replacement rules for each language
    replacements = {
        "italian": {
            r't͡s': 'ʦ',
            r'd͡z': 'ʣ',
            r't͡ʃ': 'ʧ',
            r'd͡ʒ': 'ʤ'
        },
        "spanish": {
            r'ẽ': 'e',
            r'ã': 'a',
            r'ĩ': 'i',
            r'õ': 'o',
            r'ũ': 'u',
            r't̪': 't',
            r'ɣ̞': 'ɣ',
            r'l': 'l',
            r'ð̞': 'ð',
            r'n̟': 'n',
            r'ɟ͡ʝ': 'ʝ',
            r'n̪': 'n',
            r'u̯': 'w',
            r'i̯': 'j',
            r't͡s': 'ʦ',
            r't͡ʃ': 'ʧ',
            r'β̞': 'β',
            r'd̪': 'd',



        },
        "portuguese": {
            # Define Portuguese-specific rules here if needed
        },

         "catalan": {
            r't͡s': 'ʦ',
            r'd͡z': 'dʣ',
            r't͡ʃ': 'ʧ',
            r'd͡ʒ': 'dʤ'

        }


    }

    # Validate language choice
    if language not in replacements:
        raise ValueError(f"Unsupported language: {language}")

    # Read input file
    text = read_file(file_path)

    # Apply replacements
    modified_text = apply_replacements(text, replacements[language])

    # Write output file
    output_file = f"modified_{language}.txt"
    write_file(output_file, modified_text)
    print(f"Processed text saved to {output_file}")

if __name__ == "__main__":
    # Input file path
    input_file = input("Enter the path to the input text file: ").strip()

    # Choose language
    print("Choose a language: italian, spanish, portuguese")
    chosen_language = input("Enter the language: ").strip().lower()

    # Process the text file
    try:
        process_text(input_file, chosen_language)
    except ValueError as e:
        print(e)
    except FileNotFoundError:
        print("The specified file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
