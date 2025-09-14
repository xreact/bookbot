from stats import count_words, count_caract, sort_caract_count
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def print_report(book_location,word_count,caract_count):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_location}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for caract in caract_count:
        if caract['char'].isalpha():
            print(f"{caract['char']}: {caract['num']}")
    print("============= END ===============")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    caracter_counts = count_caract(book_text)
    sorted_caracter_counts = sort_caract_count(caracter_counts)
    print_report(book_path,count_words(book_text),sorted_caracter_counts)

main()

