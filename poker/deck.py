import cards
from random import shuffle as suff
class Deck:
    y = []
    
    for x in ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]:
        y.append(f"{x}Diamond")
        y.append(f"{x}Spade")
        y.append(f"{x}Heart")
        y.append(f"{x}Clubs")
    cards.Cards.add_deck(y)
    
    def __init__(self):
        self.deck = Deck.y

    def __repr__(self):
        return f"Deck of {len(self.deck)} cards"

    def _deal(self, x):
        popers = []
        if x > len(self.deck):
            self.y = []
            raise ValueError("All cards have been dealt")
        else:
            while x > 0:
                popers.append(self.deck.pop())
                x -= 1
            return popers

    def shuffle(self):
        if len(self.deck) < 52:
            raise ValueError("Only full decks can be shuffled")
        else:
            return suff(self.deck)

    def deal_card(self):
        return self._deal(1)

    def deal_hand(self,x):
        return self._deal(x)



    def count(self):
        return len(self.deck)
    #print(deck)
    
x = Deck()
x.shuffle()
print(x.count())
x._deal(3)
print(x.count())
x.deal_card()
print(x.count())
print(x.deal_card())
print(x.deal_hand(3))