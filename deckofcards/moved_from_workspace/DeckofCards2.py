# original file archived
# Alternative implementation (archived copy)


class Cards:
    def __init__(self):
        self.hearts = [
            f"{rank} of Hearts"
            for rank in [
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "10",
                "J",
                "Q",
                "K",
                "A",
            ]
        ]
        self.diamonds = [
            f"{rank} of Diamonds"
            for rank in [
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "10",
                "J",
                "Q",
                "K",
                "A",
            ]
        ]
        self.clubs = [
            f"{rank} of Clubs"
            for rank in [
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "10",
                "J",
                "Q",
                "K",
                "A",
            ]
        ]
        self.spades = [
            f"{rank} of Spades"
            for rank in [
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "10",
                "J",
                "Q",
                "K",
                "A",
            ]
        ]


class Deck:
    def __init__(self):
        import random

        self.cards = Cards()
        self.full_deck = (
            self.cards.hearts
            + self.cards.diamonds
            + self.cards.clubs
            + self.cards.spades
        )
        random.shuffle(self.full_deck)

    def deal_card(self, num_cards, num_players):
        hands = {f"Player {i+1}": [] for i in range(num_players)}
        for _ in range(num_cards):
            for player in hands:
                if self.full_deck:
                    hands[player].append(self.full_deck.pop())
        return hands
