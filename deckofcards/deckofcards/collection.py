"""Alternative Deck implementation (moved from Python/DeckofCards2.py)"""

from __future__ import annotations
from typing import Dict
import random


class Cards:
    def __init__(self):
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        self.hearts = [f"{rank} of Hearts" for rank in ranks]
        self.diamonds = [f"{rank} of Diamonds" for rank in ranks]
        self.clubs = [f"{rank} of Clubs" for rank in ranks]
        self.spades = [f"{rank} of Spades" for rank in ranks]


class Deck:
    def __init__(self):
        # Initialize the deck with all cards from all suits
        self.cards = Cards()
        self.full_deck = (
            self.cards.hearts
            + self.cards.diamonds
            + self.cards.clubs
            + self.cards.spades
        )
        random.shuffle(self.full_deck)

    # Deal cards to players
    def deal_card(self, num_cards: int, num_players: int) -> Dict[str, list]:
        # Create a dictionary to hold each player's hand
        hands = {f"Player {i+1}": [] for i in range(num_players)}

        # Deal the specified number of cards to each player
        for _ in range(num_cards):
            # Deal one card to each player in turn
            for player in list(hands.keys()):
                if self.full_deck:
                    hands[player].append(self.full_deck.pop())
        return hands


def main() -> None:
    deck = Deck()
    hands = deck.deal_card(5, 4)  # Deal 5 cards to 4 players
    for player, cards in hands.items():
        print(f"{player}: {cards}")


if __name__ == "__main__":
    main()
