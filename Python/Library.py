# Backwards-compatible shim: the real implementation lives in the `library` package.
from library.Library import Book, Library  # type: ignore

__all__ = ["Book", "Library"]
