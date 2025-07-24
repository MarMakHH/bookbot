import sys
from stats import get_word_count, get_char_count, get_sorted_chars

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    text = get_book_text(filepath)
    wordcount= get_word_count(text)
    charcount = get_char_count(text)
    sorted_chars = get_sorted_chars(charcount)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {wordcount} total words")
    print("--------- Character Count -------")
    for dict in sorted_chars:
        print(f"{dict["char"]}: {dict["num"]}")
    print("============= END ===============")

def get_book_text(filepath: str):
    with open(filepath) as f:
        return f.read()

main()