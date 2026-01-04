import pytest
from deckofcards.classic import Deck as ClassicDeck
from deckofcards.collection import Deck as CollectionDeck


def test_classic_deal_too_many_raises():
    deck = ClassicDeck()
    with pytest.raises(ValueError):
        deck.deal(10, 6)  # 10*6=60 > 52


def test_collection_deal_partial_if_insufficient():
    # collection.Deck.deal_card deals until full_deck is empty and doesn't raise
    deck = CollectionDeck()
    hands = deck.deal_card(20, 3)  # request 60 cards but deck has 52
    # Some players may get fewer cards, but function should return dict
    assert isinstance(hands, dict)
    total_dealt = sum(len(v) for v in hands.values())
    assert total_dealt == 52


@pytest.mark.parametrize("num_cards,num_players", [(1, 1), (5, 4), (0, 3)])
def test_classic_various_deals(num_cards, num_players):
    deck = ClassicDeck()
    if num_cards * num_players > 52:
        with pytest.raises(ValueError):
            deck.deal(num_cards, num_players)
    else:
        hands = deck.deal(num_cards, num_players)
        assert len(hands) == num_players
