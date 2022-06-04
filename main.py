from ctypes.wintypes import HACCEL
import random
from random import randint
from re import S

class Card:
    #Generate a deck of cards
    def __init__(self):
        self.suits = ["Club","Spade","Heart","Diamond"]
        self.words = ["Ace","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King"]
        self.numb = list(range(1,14))
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
    def __init__(self, name = "Player", computer = False):
        self.name = name
        self.numberOfCards = 0
        self.hand = []
        self.total = 0
        self.computer = computer
        self.endTurn = False
        self.risk = 17


    #displays players cards and score
    def __repr__(self):
        return "{} has {} cards. These cards are {}. \nYour total is {}".format(self.name,self.numberOfCards,self.hand, self.total)

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
        self.endTurn = self.checkLose()
        self.displayHand()
        if self.computer == True:
            self.computerTurn(deck)
        else:
            if self.endTurn == False:
                self.turn(deck)
            else:
                print("You were {} more than 21".format(self.total-21))

    def displayHand(self):
        if self.computer == False:
            print("You currently have: ")
            for card in self.hand:
                print("{} of {}s".format(card[0],card[1]))
            print("Your score is {}".format(self.total))

    def checkLose(self):
        if self.total > 21:
            if self.computer == False:
                print("You have gone bust")
                return True
            else:
                print("The computer has gone bust")
                return True
        else:
            return False
            
            
    def computerTurn(self, deck):
        if self.total < self.risk and self.endTurn == False:
            self.drawNewCard(deck)
        elif self.total > self.risk and self.endTurn == False:
            print("The computer total is {}".format(self.total))
            print("The computer was {} away from 21".format(21-self.total))
        elif self.total == 21:
            print("The computer got 21")
        else:
            print("The computer is {} more than 21".format(self.total-21))
            print("The turn is over")

    def turn(self,deck):
        choice = input("Choose to H (hit), or S (stick) \n> ").upper()
        if "H" in choice and self.endTurn == False:
            self.drawNewCard(deck)
        elif "S" in choice and self.endTurn == False:
            print("Your total is {}".format(self.total))
            print("You were {} away from 21".format(21-self.total))
        else: 
            print("The turn is over")
            
    #draws 2 cards to begin game
    def startDraw(self, deck):
        self.drawNewCard(deck)

    #This function is currently adding the first card twice adding both values from the dict the second time. Remove the for loop and make it work on the last index of the list
    def updateScore(self,deck):
        card = self.hand[-1]
        pointWord = card[0]
        points = deck.numbValues[pointWord]
        self.total += points
 
def winner(player, computer):
    if player.total > computer.total:
        print("Player wins")
    else:
        print("Computer wins")

deck = Card()
print(deck)
print("***\n\n\nPlayer's turn \n\n\n***")
playerHand = MyHand()
playerHand.drawNewCard(deck)
print("***\n\n\nComputer's turn\n\n\n***")
computerHand = MyHand(computer = True)
computerHand.drawNewCard(deck)
winner(playerHand,computerHand)
