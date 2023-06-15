class Cards:
    deck = []
    #cards made in value suit model eg 9Diamonds ASpades
    def add_deck(x):
        deck = x

    def __repr__(self):
        if "10" in self.value:
            return f"{self.value[0:2]} of {self.value[2:]}"
        return f"{self.value[0]} of {self.value[1:]}"
