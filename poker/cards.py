class Cards:
    deck = []
    #cards made in value suit model eg 9Diamonds ASpades
    #def __init__(self, value):
    #    self.value = value
    def add_deck(x):
        deck = x

    def __repr__(self):
        if "10" in self.value:
            return f"{self.value[0:2]} of {self.value[2:]}"
        return f"{self.value[0]} of {self.value[1:]}"

#deck = []
#for x in ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]:
#    print(Cards((f"{x}Diamond")))
#    print(Cards((f"{x}Spade")))
#    print(Cards((f"{x}Heart")))
#    print(Cards((f"{x}Clubs")))