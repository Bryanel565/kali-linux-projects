from deckofcards.classic import Deck as ClassicDeck
from deckofcards.collection import Deck as CollectionDeck


def test_classic_deck_deal():
    deck = ClassicDeck()
    assert len(deck.cards) == 52
    deck.shuffle()
    hands = deck.deal(5, 4)
    assert len(hands) == 4
    assert all(len(hand) == 5 for hand in hands)
    # After dealing 20 cards, deck should have 32 left
    assert len(deck.cards) == 32


def test_package_helper_all_classes():
    # Import directly from the package submodule to avoid import path issues in some environments
    from deckofcards.deckofcards import all_classes

    data = all_classes()
    assert isinstance(data, dict)
    assert "Card" in data and "ClassicDeck" in data


def test_collection_deck_deal():
    deck = CollectionDeck()
    # full_deck should initially have 52 cards
    assert len(deck.full_deck) == 52
    hands = deck.deal_card(5, 4)
    assert len(hands) == 4
    assert all(len(cards) == 5 for cards in hands.values())
    # After dealing 20 cards, full_deck should have 32 left
    assert len(deck.full_deck) == 32
