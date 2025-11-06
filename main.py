import sys
from stats import get_book_text, counted, specific_number, sorter, report_printer


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        print("Path to book is books/*.txt")
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)
    number = counted(text)
    amounts = specific_number(text)
    listed_letters = sorter(amounts)
    report_printer(path, number, listed_letters)


main()

