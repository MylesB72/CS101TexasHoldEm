import random
from random import randint

class Card:
    #Generate a deck of cards
    def __init__(self):
        self.suits = ["Club","Spade","Heart","Diamond"]
        self.words = ["Ace","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King"]
        self.numb = list(range(0,14))
        self.numbValues = dict(zip(self.words,self.numb))
        self.usedCards = {}

        #create a complete dictionary of all the cards. This dictionary will have cards removed from it as the game goes on
        self.deck = {}
        for i in range(4):
            self.deck[self.suits[i]] = self.words
        

    def __repr__(self):
        return "This is a deck of 52 cards in the following suits: {}".format(self.suits)

    #remove the drawn card from the deck
    def updateDeck(self, suit, card):
        self.deck[suit].remove(card)

class MyHand:
    def __init__(self, name = "Player"):
        self.name = name
        self.numberOfCards = 0
        self.hand = []
        self.total = 0

    #displays players cards and score
    def __repr__(self):
        return "{} has {} cards. These cards are {}. \n Your total is {}".format(self.name,self.numberOfCards,self.hand, self.total)

    #draw a card and check to make sure that card hasn't already been drawn
    def drawNewCard(self,deck):
        drawn = False
        self.numberOfCards += 1
        #only draw cards that are currently in the deck, retries until it finds a card not drawn.
        while drawn != True:
            try:
                suit = deck.suits[randint(0,3)]
                card = deck.words[randint(0,13)]
                drawn = True
            except:
                drawn = False
        self.hand.append([card, suit])
        deck.updateDeck(suit,card)
        self.updateScore(deck)
        print(self)

    #draws 2 cards to begin game
    def startDraw(self, deck):
        for i in range(2):
            self.drawNewCard(deck)

    def updateScore(self,deck):
        print(deck.numbValues)
        for card in self.hand:
            pointWord = card[0]
            points = deck.numbValues[pointWord]
            self.total += points
            
        

            

    
deck = Card()
playerHand = MyHand()
playerHand.startDraw(deck)

