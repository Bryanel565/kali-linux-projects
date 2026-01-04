import argparse
from .Library import Library, Book


def main():
    parser = argparse.ArgumentParser(description="Simple Library CLI")
    subparsers = parser.add_subparsers(dest="command")

    list_parser = subparsers.add_parser("list", help="List books")

    add_parser = subparsers.add_parser("add", help="Add a book")
    add_parser.add_argument("genre")
    add_parser.add_argument("title")
    add_parser.add_argument("author")
    add_parser.add_argument("year", type=int)

    save_parser = subparsers.add_parser("save-json", help="Save library to JSON")
    save_parser.add_argument("filename")

    load_parser = subparsers.add_parser("load-json", help="Load library from JSON")
    load_parser.add_argument("filename")

    args = parser.parse_args()

    lib = Library()

    if args.command == "list":
        for b in lib.list_books():
            print(b)
    elif args.command == "add":
        book = Book(args.genre, args.title, args.author, args.year)
        lib.add_book(book)
        print("Added:", book)
    elif args.command == "save-json":
        lib.save_to_json(args.filename)
        print("Saved to", args.filename)
    elif args.command == "load-json":
        lib = Library.load_from_json(args.filename)
        for b in lib.list_books():
            print(b)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
