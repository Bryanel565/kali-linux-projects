from dataclasses import dataclass, asdict
from typing import List
import json
import csv
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@dataclass
class Book:
    genre: str
    title: str
    author: str
    year: int

    def __str__(self) -> str:
        return f"'{self.title}' by {self.author} ({self.year}) - Genre: {self.genre}"


class Library:
    def __init__(self):
        self.books: List[Book] = []

    def add_book(self, book: Book) -> None:
        logger.info("Adding book: %s", book)
        self.books.append(book)

    def remove_book(self, title: str) -> None:
        logger.info("Removing book by title: %s", title)
        self.books = [book for book in self.books if book.title != title]

    def find_books_by_genre(self, genre: str) -> List[str]:
        return [str(book) for book in self.books if book.genre == genre]

    def find_books_by_author(self, author: str) -> List[str]:
        return [str(book) for book in self.books if book.author == author]

    def find_books_by_title_substring(self, substring: str) -> List[str]:
        return [str(book) for book in self.books if substring.lower() in book.title.lower()]

    def list_books(self) -> List[str]:
        return [str(book) for book in self.books]

    def to_dicts(self) -> List[dict]:
        return [asdict(book) for book in self.books]

    def save_to_json(self, filename: str) -> None:
        logger.info("Saving library to JSON: %s", filename)
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.to_dicts(), f, ensure_ascii=False, indent=2)

    @classmethod
    def load_from_json(cls, filename: str) -> 'Library':
        logger.info("Loading library from JSON: %s", filename)
        lib = cls()
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            for item in data:
                lib.add_book(Book(**item))
        return lib

    def save_to_csv(self, filename: str) -> None:
        logger.info("Saving library to CSV: %s", filename)
        with open(filename, "w", newline='', encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["genre", "title", "author", "year"])
            writer.writeheader()
            for d in self.to_dicts():
                writer.writerow(d)

    @classmethod
    def load_from_csv(cls, filename: str) -> 'Library':
        logger.info("Loading library from CSV: %s", filename)
        lib = cls()
        with open(filename, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                # csv reads numbers as strings; convert year to int
                row['year'] = int(row['year'])
                lib.add_book(Book(**row))
        return lib


def _demo() -> None:
    lib = Library()
    lib.add_book(Book("Fiction", "1984", "George Orwell", 1949))
    lib.add_book(Book("Science Fiction", "Dune", "Frank Herbert", 1965))
    print(lib.list_books())


if __name__ == "__main__":
    _demo()
