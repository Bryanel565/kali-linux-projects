"""deckofcards package

Exports:
- classic: Card, Deck implementation
- collection: alternative Deck implementation
"""

from .classic import Card, Deck as ClassicDeck
from .collection import Cards, Deck as CollectionDeck

__all__ = ["Card", "ClassicDeck", "Cards", "CollectionDeck", "all_classes"]


# Package-level helpers for demo & simple test coverage
def all_classes() -> dict:
    """Return simple registry of exported classes for demo or quick introspection."""
    return {
        "Card": ClassicDeck.__module__ + ":Card",
        "ClassicDeck": ClassicDeck.__module__ + ":Deck",
        "Cards": CollectionDeck.__module__ + ":Cards",
        "CollectionDeck": CollectionDeck.__module__ + ":Deck",
    }
