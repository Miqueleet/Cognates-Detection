import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

consonants = {
    "p": {"place": 0.1, "manner": "ocl", "voiced": 0},
    "b": {"place": 0.1, "manner": "ocl", "voiced": 1},
    "t": {"place": 0.3, "manner": "ocl", "voiced": 0},
    "d": {"place": 0.3, "manner": "ocl", "voiced": 1},
    "k": {"place": 0.7, "manner": "ocl", "voiced": 0},
    "g": {"place": 0.7, "manner": "ocl", "voiced": 1},
    "m": {"place": 0.1, "manner": "nas", "voiced": 1},
    "n": {"place": 0.4, "manner": "nas", "voiced": 1},
    "ɲ": {"place": 0.6, "manner": "nas", "voiced": 1},
    "ŋ": {"place": 0.7, "manner": "nas", "voiced": 1},
    "ʁ": {"place": 0.8, "manner": "fri", "voiced": 1},
    "ɾ": {"place": 0.4, "manner": "vib", "voiced": 1},
    "r": {"place": 0.4, "manner": "vib", "voiced": 1},
    "β": {"place": 0.1, "manner": "aprox", "voiced": 1},
    "f": {"place": 0.2, "manner": "fri", "voiced": 0},
    "v": {"place": 0.2, "manner": "fri", "voiced": 1},
    "θ": {"place": 0.3, "manner": "fri", "voiced": 0},
    "ð": {"place": 0.3, "manner": "aprox", "voiced": 1},
    "ɣ": {"place": 0.7, "manner": "aprox", "voiced": 1},
    "s": {"place": 0.4, "manner": "fri", "voiced": 0},
    "ʦ": {"place": 0.4, "manner": "afr", "voiced": 0},
    "z": {"place": 0.4, "manner": "fri", "voiced": 1},
    "ʣ": {"place": 0.4, "manner": "afr", "voiced": 1},
    "ʃ": {"place": 0.5, "manner": "fri", "voiced": 0},
    "ʧ": {"place": 0.5, "manner": "afr", "voiced": 0},
    "ʒ": {"place": 0.5, "manner": "fri", "voiced": 1},
    "ʤ": {"place": 0.5, "manner": "afr", "voiced": 1},
    "x": {"place": 0.7, "manner": "fri", "voiced": 0},
    "ʝ": {"place": 0.6, "manner": "fri", "voiced": 1},
    "j": {"place": 0.6, "manner": "aprox", "voiced": 1},
    "χ": {"place": 0.8, "manner": "fri", "voiced": 0},
    "h": {"place": 1, "manner": "fri", "voiced": 0},
    "l": {"place": 0.4, "manner": "lat", "voiced": 1},
    "ʎ": {"place": 0.6, "manner": "lat", "voiced": 1},
    "ħ": {"place": 0.9, "manner": "fri", "voiced": 0}
}


vowels = {
    "ə": {"open": 0.625, "back": 0.6, "rounded": 0, "nasal": 0},
    "a": {"open": 1, "back": 0.2, "rounded": 0, "nasal": 0},
    "e": {"open": 0.5, "back": 0.2, "rounded": 0, "nasal": 0},
    "i": {"open": 0.25, "back": 0.2, "rounded": 0, "nasal": 0},
    "o": {"open": 0.5, "back": 1, "rounded": 1, "nasal": 0},
    "u": {"open": 0.25, "back": 1, "rounded": 1, "nasal": 0},
    "ɛ": {"open": 0.75, "back": 0.2, "rounded": 0, "nasal": 0},
    "ɔ": {"open": 0.75, "back": 1, "rounded": 1, "nasal": 0},
    "ɐ": {"open": 0.875, "back": 0.6, "rounded": 0, "nasal": 0},
    "ʊ": {"open": 0.375, "back": 0.8, "rounded": 1, "nasal": 0},
    "ɪ": {"open": 0.375, "back": 0.4, "rounded": 0, "nasal": 0},
    "ɨ": {"open": 0.25, "back": 0.6, "rounded": 0, "nasal": 0},
    "ɑ": {"open": 1, "back": 1, "rounded": 1, "nasal": 0},
    "y": {"open": 0.25, "back": 0.2, "rounded": 1, "nasal": 0},
    "œ": {"open": 0.75, "back": 0.2, "rounded": 1, "nasal": 0},
    "ø": {"open": 0.5, "back": 0.2, "rounded": 1, "nasal": 0},
    "ẽ": {"open": 0.5, "back": 0.2, "rounded": 0, "nasal": 1},
    "ũ": {"open": 0.25, "back": 1, "rounded": 1, "nasal": 1},
    "õ": {"open": 0.5, "back": 1, "rounded": 1, "nasal": 1},
    "ĩ": {"open": 0.25, "back": 0.2, "rounded": 0, "nasal": 1},
    "ã": {"open": 1, "back": 0.2, "rounded": 0, "nasal": 1},
    "ɔ̃": {"open": 0.75, "back": 1, "rounded": 1, "nasal": 1},
    "ɑ̃": {"open": 1, "back": 1, "rounded": 1, "nasal": 1},
    "ɛ̃": {"open": 0.75, "back": 0.2, "rounded": 0, "nasal": 1},
    "ɐ̃": {"open": 0.875, "back": 0.6, "rounded": 0, "nasal": 1}
}


def PDC(x1,x2):
    
    delta_p=abs(consonants[x1]["place"]-consonants[x2]["place"])
    if consonants[x1]["manner"]==consonants[x2]["manner"]:
        delta_m=0
    else:
        delta_m=1 
    delta_v = abs(consonants[x1]["voiced"]-consonants[x2]["voiced"])
    
    return (delta_m*(0.5/5) + delta_p*(4/5) + delta_v*(0.5/5))


def PDV(x1,x2):
    
    delta_o=abs(vowels[x1]["open"]-vowels[x2]["open"])
    delta_b=abs(vowels[x1]["back"]-vowels[x2]["back"])
    delta_r = abs(vowels[x1]["rounded"]-vowels[x2]["rounded"])
    delta_n = abs(vowels[x1]["nasal"]-vowels[x2]["nasal"])
    
    return (delta_o + delta_b)/3 + delta_r/6 + delta_n/6


def phonetic_difference(x1, x2):
    # Compute the raw phonetic difference
    if ("u" in [x1, x2] and "w" in [x1, x2]) or ("j" in [x1, x2] and "i" in [x1, x2]):
        raw_difference = 0.2
    elif x1 in consonants and x2 in consonants:
        raw_difference = PDC(x1, x2)
    elif x1 in vowels and x2 in vowels:
        raw_difference = PDV(x1, x2)
    else:
        raw_difference = 1
    
    # Apply quadratic weighting directly
    if raw_difference <= 0.5:
        return (2*(raw_difference ** 2))*10
    else:
        return (1 - (1 - raw_difference) ** 2)*10


# Create a list of consonant phonemes
cons_phonemes = list(consonants.keys())

# Initialize a dictionary to store distances
distance_matrix = {}

# Compute pairwise distances
for x1 in cons_phonemes:
    distance_matrix[x1] = {}
    for x2 in cons_phonemes:
        
        distance_matrix[x1][x2] = PDC(x1, x2)

# Convert the dictionary to a Pandas DataFrame for a table format
distance_table = pd.DataFrame(distance_matrix)

# Plot a heatmap using seaborn (without annotations)
plt.figure(figsize=(12, 10))
sns.heatmap(distance_table, cmap="YlGnBu", cbar=True, annot=False, xticklabels=cons_phonemes, yticklabels=cons_phonemes)
plt.title("Phonetic Distance Between Consonants")
plt.xlabel("Consonant 1")
plt.ylabel("Consonant 2")

# Save the heatmap as a PNG file
plt.savefig("phonetic_distance_heatmap_consonants.png", dpi=300, bbox_inches="tight")

vow_phonemes = list(vowels.keys())

# Initialize a dictionary to store distances
distance_matrix = {}

# Compute pairwise distances
for x1 in vow_phonemes:
    distance_matrix[x1] = {}
    for x2 in vow_phonemes:
        
        distance_matrix[x1][x2] = PDV(x1, x2)
 

# Convert the dictionary to a Pandas DataFrame for a table format
distance_table = pd.DataFrame(distance_matrix)

# Plot a heatmap using seaborn (without annotations)
plt.figure(figsize=(12, 10))
sns.heatmap(distance_table, cmap="YlGnBu", cbar=True, annot=False, xticklabels=vow_phonemes, yticklabels=vow_phonemes)
plt.title("Phonetic Distance Between Consonants")
plt.xlabel("Consonant 1")
plt.ylabel("Consonant 2")

# Save the heatmap as a PNG file
plt.savefig("phonetic_distance_heatmap_vowels.png", dpi=300, bbox_inches="tight")


def PED(source, target):
    # Get the lengths of the source and target strings
    s = len(source)
    t = len(target)
    
    # Base case: if either string is empty
    if min(s, t) == 0:
        return max(s, t)
    
    # Check if the last characters are the same
    if source[s - 1] == target[t - 1]:
        cost = 0
    else:
        # Recursive costs for insertion, deletion, and replacement
        ins_cost = PED(source[0:s-1], target) + 1
        del_cost = PED(source, target[0:t-1]) + 1
        rep_cost = PED(source[0:s-1], target[0:t-1]) + phonetic_difference(source[s - 1], target[t - 1])
        # Return the minimum of the three costs
        return min(ins_cost, del_cost, rep_cost)
    
    # If last characters match, return result of recursion
    return PED(source[0:s-1], target[0:t-1]) + cost

# Example Usage
source_ipa = "ak.sɑ̃/"
target_ipa = "atˈt͡ʃɛn.to"
def PED_DP(source, target):
    s, t = len(source), len(target)
    dp = [[0] * (t + 1) for _ in range(s + 1)]
    
    for i in range(s + 1):
        for j in range(t + 1):
            if i == 0:
                dp[i][j] = j * 0.5  # Cost of all insertions
            elif j == 0:
                dp[i][j] = i * 1  # Cost of all deletions
            else:
                cost = 0 if source[i - 1] == target[j - 1] else phonetic_difference(source[i - 1], target[j - 1])
                dp[i][j] = min(
                    dp[i - 1][j] + 1,        # Deletion
                    dp[i][j - 1] + 0.5,        # Insertion
                    dp[i - 1][j - 1] + cost    # Substitution
                )
    return dp[s][t]



import random
import Levenshtein

def find_minimal_pair_random(file1, file2, output_file, sample_size=100):
    """
    For a random sample of words from file1, finds the word in file2 with the minimal combined 
    Levenshtein distance and Phonetic Edit Distance (PED) and writes the results to a new file.
    """
    # Read the first file into a list of tuples (word, transcription)
    with open(file1, 'r', encoding='utf-8') as f1:
        words1 = [line.strip().split(' ', 1) for line in f1 if line.strip()]
    
    # Select a random sample of words from file1
    if len(words1) > sample_size:
        words1 = random.sample(words1, sample_size)
    
    # Read the second file into a list of tuples (word, transcription)
    with open(file2, 'r', encoding='utf-8') as f2:
        words2 = [line.strip().split(' ', 1) for line in f2 if line.strip()]
    
    # Open the output file for writing results
    with open(output_file, 'w', encoding='utf-8') as out:
        for word1, ipa1 in words1:
            min_distance = float('inf')
            best_match = None
            
            for word2, ipa2 in words2:
                # Compute Levenshtein distance between words
                word_distance = Levenshtein.distance(word1, word2)
                
                # Compute Phonetic Edit Distance (PED) between transcriptions
                ped = PED_DP(ipa1, ipa2)
                
                # Sum the distances
                total_distance = word_distance + 2*ped
                
                # Update the minimum distance and best match
                if total_distance < min_distance:
                    min_distance = total_distance
                    best_match = (word2, ipa2, total_distance)
            
            # Write the best match for the current word1 to the output file
            if best_match:
                out.write(f"{word1}\t{ipa1}\t{best_match[0]}\t{best_match[1]}\t{best_match[2]}\n")

# Example usage:
file1 = "./nouns/valencian_cat.txt"  # First file with words and transcriptions
file2 = "./nouns/italian.txt"      # Second file with words and transcriptions
output_file = "matches_italian_vcatalan1_insertion1_2iped_5.txt"  # Output file to store results

find_minimal_pair_random(file1, file2, output_file, sample_size=100)

