class Card:
    def __init__(self):
        self.suits = ["Club","Spade","Heart","Diamond"]
        self.words = ["Ace","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King"]
        self.numb = list(range(0,14))
        self.wordWithValues = dict(zip(self.words, self.numb))




class MyHand:
    def __init__(self, name):
        self.name = name
        numberOfCards = 0

deck = Card()
print(deck.wordWithValues)     