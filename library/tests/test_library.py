from library.Library import Book, Library


def test_add_and_list_books():
    lib = Library()
    b1 = Book("Fiction", "1984", "George Orwell", 1949)
    b2 = Book("Non-Fiction", "Sapiens", "Yuval Noah Harari", 2011)
    lib.add_book(b1)
    lib.add_book(b2)
    titles = [b for b in lib.list_books()]
    assert any("1984" in t for t in titles)
    assert any("Sapiens" in t for t in titles)


def test_find_by_genre_and_author_and_substring():
    lib = Library()
    b1 = Book("Fiction", "Dune", "Frank Herbert", 1965)
    b2 = Book("Fiction", "To Kill a Mockingbird", "Harper Lee", 1960)
    lib.add_book(b1)
    lib.add_book(b2)

    fiction_books = lib.find_books_by_genre("Fiction")
    assert len(fiction_books) == 2

    frank_books = lib.find_books_by_author("Frank Herbert")
    assert len(frank_books) == 1

    dune_substring = lib.find_books_by_title_substring("dune")
    assert len(dune_substring) == 1


def test_remove_book():
    lib = Library()
    b1 = Book("Fiction", "1984", "George Orwell", 1949)
    lib.add_book(b1)
    lib.remove_book("1984")
    assert len(lib.list_books()) == 0


def test_save_and_load_json(tmp_path):
    lib = Library()
    lib.add_book(Book("Fiction", "1984", "George Orwell", 1949))
    lib.add_book(Book("Non-Fiction", "Sapiens", "Yuval Noah Harari", 2011))

    json_file = tmp_path / "library.json"
    lib.save_to_json(str(json_file))

    loaded = Library.load_from_json(str(json_file))
    assert len(loaded.list_books()) == 2


def test_save_and_load_csv(tmp_path):
    lib = Library()
    lib.add_book(Book("Fiction", "1984", "George Orwell", 1949))
    lib.add_book(Book("Non-Fiction", "Sapiens", "Yuval Noah Harari", 2011))

    csv_file = tmp_path / "library.csv"
    lib.save_to_csv(str(csv_file))

    loaded = Library.load_from_csv(str(csv_file))
    assert len(loaded.list_books()) == 2
