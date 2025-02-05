def main():
    path_to_file = "books/frankenstein.txt"
    words = words_list(path_to_file)
    total_words = word_count(words)
    character_count_dictionary = character_count(words)
    print(f"--- Begin report of {path_to_file} ---")
    print()
    print(f"{total_words} words found in the document")
    print()
    for c in character_count_dictionary:
        if c.isalpha():
            print(f"The '{c}' character was found {character_count_dictionary[c]} times")
    print()
    print("--- End report ---")


def words_list(text_file):
    file_contents = ""
    with open(text_file) as f:
        file_contents = f.read()
    return file_contents

def word_count(words):
    return len(words.split())

def character_count(words):
    characters_counted = {}
    character = ""
    for c in words:
        character = c.lower()
        if character not in characters_counted:
            characters_counted[character] = 1
        else:
            characters_counted[character] += 1
    return characters_counted


main()