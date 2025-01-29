import os
import json

def build_chord_vocabulary(folder_path, chord_vocab_file="chord_vocab.json"):
    """
    Builds a vocabulary of unique Roman numerals (chords) with unique IDs.
    Keys are assumed to already be numbered 0-11 and are not included in the vocabulary.

    Parameters:
        folder_path (str): Path to the folder containing expanded files.
        chord_vocab_file (str): File name to save chord vocabulary.
    """
    chord_vocab = {}  # To store unique chords
    chord_id = 0

    # Process each file in the folder
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".txt"):
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, "r") as file:
                for line in file:
                    parts = line.strip().split()
                    if len(parts) >= 7:
                        # Extract chord (Roman numeral)
                        roman_numeral = parts[2]

                        # Add chord to chord vocabulary
                        if roman_numeral not in chord_vocab:
                            chord_vocab[roman_numeral] = chord_id
                            chord_id += 1

    # Save chord vocabulary to JSON
    with open(chord_vocab_file, "w") as json_file:
        json.dump(chord_vocab, json_file, indent=4)

    print(f"Chord vocabulary saved to {chord_vocab_file} ({len(chord_vocab)} unique chords).")

# Example Usage
folder_path = "expandedv0"  # Replace with your folder containing expanded files
build_chord_vocabulary(folder_path)