from deck import CardDeck, PlayingCard

class CardHand:
    """
    A class that represents a hand of cards in a card game.
    The class determines the properties of the hand: flush, pair, or straight
    """
    def __init__(self, card_deck):
        """
        Initialize a hand with 5 cards dealt from the given deck.
        :param card_deck: An instance of the CardDeck class from which cards are dealt.
        """
        cards = []
        # card_deck.shuffle()
        for i in range(5):
            cards.append(card_deck.deal())
        self._cards = cards

    @property
    def cards(self):
        """
        Get the cards in the hand.
        :return: A list of PlayingCard objects representing the hand.
        """
        return self._cards

    @property
    def is_flush(self):
        """
        Check if the hand is a flush (all cards of the same suit).
        :return: True if all cards have the same suit, False otherwise.
        """
        for card in self.cards[1:]:
            if self.cards[0].suit != card.suit:
                return False
        return True

    @property
    def num_matches(self):
        """
        Count the total number of rank matches between cards in the hand. Used to determine what type of hand it is.
        :return: An integer representing the total matches.
        """
        matches = 0
        for i in range(5):
            for j in range(5):
                if i == j:
                    continue
                if self.cards[i].rank == self.cards[j].rank:
                    matches += 1
        return matches

    @property
    def is_pair(self):
        """
        Check if the hand contains exactly one pair.
        :return: True if the hand is a pair, False otherwise.
        """
        if self.num_matches == 2:
            return True
        return False

    @property
    def is_2_pair(self):
        """
        Check if the hand contains two pairs.
        :return: True if the hand is two pairs, False otherwise.
        """
        if self.num_matches == 4:
            return True
        return False

    @property
    def is_trips(self):
        """
        Check if the hand contains three cards of the same rank.
        :return: True if the hand is trips, False otherwise.
        """
        if self.num_matches == 6:
            return True
        return False

    @property
    def is_quads(self):
        """
        Check if the hand contains four cards of the same rank.
        :return: True if the hand is quads, False otherwise.
        """
        if self.num_matches == 12:
            return True
        return False

    @property
    def is_full_house(self):
        """
        Check if the hand is a full house (three of one rank and two of another rank).
        :return: True if the hand is a full house, False otherwise.
        """
        if self.num_matches == 8:
            return True
        return False

    @property
    def is_straight(self):
        """
        Check if the hand is a straight (five cards in sequence).
        :return: True if the hand is a straight, False otherwise.
        """
        if self.num_matches != 0:
            return False
        self.cards.sort()
        if PlayingCard.RANKS.index(self.cards[0].rank) + 4 == PlayingCard.RANKS.index(self.cards[4].rank):
            return True

    def __str__(self):
        """
        Get the string representation of the hand.
        :return: A string representing the hand.
        """
        return str(self._cards)

matches = 0
count = 0

while matches < 10000:
    card_deck = CardDeck()
    card_deck.shuffle()
    card_hand = CardHand(card_deck)
    count += 1
    if card_hand.is_straight:
        print(card_hand)
        matches += 1
        break

print(f"The probability of a straight is: {100*matches/count}%")