# Library (Python package)

This repository contains the **Library** learning project — a small Python package that implements a `Book` and `Library` class with serialization, search, and a simple CLI (`libman`).

Quick start
-----------

Install for development (editable):

```bash
# from repo root
pip install -e .
```

Run tests:

```bash
pytest -q
```

CLI usage
---------

After installing, use the `libman` console script (provided by the `library` package):

```bash
# list books (empty by default)
libman list

# add a book
libman add Fiction "Dune" "Frank Herbert" 1965

# save the library to JSON
libman save-json library.json

# load and print saved library
libman load-json library.json
```

Project layout
--------------

- `library/` — the package (exporting `Book` and `Library`) and `cli` support
- `deckofcards/` — an independent learning project (deck of cards) kept in the repo

Release notes & publishing
--------------------------

- Version and packaging metadata are in `pyproject.toml` and `setup.cfg`.
- To build release artifacts (sdist + wheel):

```bash
# in your venv
python -m pip install --upgrade build
python -m build
```

- To publish to PyPI (example steps):

```bash
python -m pip install --upgrade twine
python -m twine upload dist/*
```

If you'd like, I can (pick one):
- Add a `CHANGELOG.md` and bump the package version for a new release, then build artifacts.
- Clean leftover references to the old `Python` package name across the repo.
- Prepare a GitHub release tag and optionally publish to PyPI for you.
