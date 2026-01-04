# original file archived
# A simple card and deck implementation (archived copy)


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

    def __init__(self, suit, rank):
        if suit not in Card.SUITS:
            raise ValueError(f"Invalid suit: {suit}")
        if rank not in Card.RANKS:
            raise ValueError(f"Invalid rank: {rank}")
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def __repr__(self):
        return f"Card(suit='{self.suit}', rank='{self.rank}')"


class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in Card.SUITS for rank in Card.RANKS]

    def shuffle(self):
        import random

        random.shuffle(self.cards)

    def deal(self, num_cards, num_players):
        if num_cards * num_players > len(self.cards):
            raise ValueError("Not enough cards in the deck to deal")
        hands = [[] for _ in range(num_players)]
        for i in range(num_cards):
            for j in range(num_players):
                hands[j].append(self.cards.pop())
        return hands

    def __str__(self):
        return ", ".join(str(card) for card in self.cards)
