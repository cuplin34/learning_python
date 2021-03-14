from random import shuffle as suff
class Cards():
    #deck = []
    #cards made in value suit model eg 9Diamonds ASpades
    def __init__(self, value):
        self.value = value
    def add_deck(x):
        deck = x

    def __repr__(self):
        m = 0
        n = []
        while m < len(self.value):
            if "10" in self.value[m]:
                n.append(f"{self.value[m][0:2]} of {self.value[m][2:]}")
            else:
                n.append(f"{self.value[m][0]} of {self.value[m][1:]}")
            m += 1
        return str(n)
        

class Deck:
    y = []
    
    for x in ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]:
        y.append(f"{x}Diamond")
        y.append(f"{x}Spade")
        y.append(f"{x}Heart")
        y.append(f"{x}Clubs")
    Cards.add_deck(y)
    
    def __init__(self):
        self.deck = Deck.y

    def __repr__(self):
        return f"Deck of {len(self.deck)} cards"

    def _deal(self, x):
        popers = []
        if x > len(self.deck):
            while x-1 > len(self.deck):
                    popers.append(self.deck.pop())
                    x -= 1
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
#y = Cards(x.y)
x.shuffle()
x.shuffle()
hand_1 = x.deal_hand(52)
print(hand_1)