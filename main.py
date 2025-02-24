from stats import word_count, character_count
import sys

def get_book_text(filepath_of_book: str) -> str:
    with open(filepath_of_book) as f:
        book_contents = f.read()
    return book_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    book_contents = get_book_text(book)
    total_words = word_count(book_contents)
    character_count_dictionary = character_count(book_contents)
    print(f"--- Begin report of {book} ---")
    print()
    print(f"{total_words} words found in the document")
    print()
    for c in character_count_dictionary:
        if c.isalpha():
            print(f"The '{c}' character was found {character_count_dictionary[c]} times")
    print()
    print("--- End report ---")

main()