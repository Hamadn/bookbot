import sys

from stats import get_book_text, get_num_char, get_num_words, get_report


def main():
    if sys.argv[1:]:
        book = sys.argv[1]
        book_text = get_book_text(book)
        book_words = get_num_words(book_text)
        book_chars = get_num_char(book_text)
        report = get_report(book_chars)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book}...")
        print("----------- Word Count ----------")
        print(book_words)
        print("--------- Character Count -------")
        for item in report:
            ch = item["char"]
            count = item["num"]
            if ch.isalpha():
                print(f"{ch}: {count}")
            else:
                continue
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


main()
