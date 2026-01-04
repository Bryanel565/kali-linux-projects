"""Classic Card and Deck implementation (moved from Python/DeckOfCards.py)"""

from __future__ import annotations
from typing import List


class Card:
    SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
    RANKS = [
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
        "Ace",
    ]

    def __init__(self, suit: str, rank: str):
        if suit not in Card.SUITS:
            raise ValueError(f"Invalid suit: {suit}")
        if rank not in Card.RANKS:
            raise ValueError(f"Invalid rank: {rank}")
        self.suit = suit
        self.rank = rank

    def __str__(self) -> str:
        return f"{self.rank} of {self.suit}"

    def __repr__(self) -> str:
        return f"Card(suit='{self.suit}', rank='{self.rank}')"


class Deck:
    def __init__(self):
        self.cards: List[Card] = [
            Card(suit, rank) for suit in Card.SUITS for rank in Card.RANKS
        ]

    def shuffle(self) -> None:
        import random

        random.shuffle(self.cards)

    def deal(self, num_cards: int, num_players: int):
        if num_cards * num_players > len(self.cards):
            raise ValueError("Not enough cards in the deck to deal")
        hands = [[] for _ in range(num_players)]
        for i in range(num_cards):
            for j in range(num_players):
                hands[j].append(self.cards.pop())
        return hands

    def __str__(self) -> str:
        return ", ".join(str(card) for card in self.cards)


def main() -> None:
    deck = Deck()
    print("Initial deck:")
    print(deck)

    deck.shuffle()
    print("\nShuffled deck:")
    print(deck)

    hands = deck.deal(5, 4)
    for i, hand in enumerate(hands):
        print(f"\nPlayer {i + 1}'s hand:")
        for card in hand:
            print(card)


if __name__ == "__main__":
    main()
