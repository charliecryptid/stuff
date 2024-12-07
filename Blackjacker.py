#!/usr/bin/env python
# coding: utf-8

# In[97]:


import random

class Card:
    def __init__(self, num, suit):
        self.suit = suit
        self.num = num

    def display(self):
        print(f"{self.num} of {self.suit}")
        

class Game:
    def __init__(self, playdol, dealdol): #playerdollar and dealerdollar
        self.playdol = playdol
        self.dealdol = dealdol
        self.round = 0

    def display(self):
        print(f"Player: ${self.playdol}")
        print(f"Dealer: ${self.dealdol}")
        print(f"Rounds: {self.round}")

def handTotal(hand):
    sum = 0
    aces = 0
    for card in hand:
        if card.num in ['J', 'Q', 'K']:
            sum += 10
        elif card.num == 'A': #dealing with softhands
            aces += 1
        else:
            sum += card.num

    while aces > 0:
        if sum < 10:
            sum += 11
        else:
            sum += 1
        aces -= 1
            
    return sum

class Round:
    def __init__(self, game, bet):
        self.game = game
        self.bet = bet
        self.deck = []
        for suit in ['hearts', 'diamonds', 'clubs', 'spades']:
            for num in ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']:
                self.deck.append(Card(num, suit))
        self.playhand = []
        self.dealhand = []
        self.dealplay = False

    def draw(self, hand):
        cardnum = random.randint(0, len(self.deck) - 1)
        hand.append(self.deck[cardnum])
        del self.deck[cardnum]

    def deal(self):
        self.draw(self.playhand)
        self.draw(self.playhand)
        self.draw(self.dealhand)
        self.draw(self.dealhand)

    def displayHands(self):
        print("Dealer Hand")
        self.dealhand[0].display()
        if self.dealplay == False:
            print("face down card")
            print("Total: ?")
        else: 
            for i in range(1, len(self.dealhand)):
                self.dealhand[i].display()
            print(f"Total: {handTotal(self.dealhand)}")
        
        print()
        print("Player Hand")
        for card in round.playhand:
            card.display()
        print(f"Total: {handTotal(self.playhand)}")
        
# thedeck = Deck()
# for card in thedeck.deck:
#     card.display()




# In[108]:


sep = "-" * 40
print("let's play blackjack")
amount = int(input("How much would you like to start with?: "))

print(sep)
game = Game(amount, amount)
print("let's begin")

while True:
    if game.playdol <= 0 or game.dealdol <= 0:
        if game.playdol <= 0:
            print("you lose...")
        elif game.dealdol <= 0:
            print("you win!")
        game.display()
        break
    game.round += 1
    game.display()
    #betting
    while True:
        bet = int(input("how much would you like to bet?: "))
        if bet > game.playdol:
            print("not enough money")
        else:
            break
    
    #dealing
    round = Round(game, bet)
    print("dealing hands...")
    round.deal()
    
    #natural blackjacks
    if round.dealhand[0].num == 10 or round.dealhand[0].num == 'A':
        print("checking for naturals...")
        if handTotal(round.dealhand) == 21 and handTotal(round.playhand) == 21:
            print("tied blackjack")
            continue
        elif handTotal(round.dealhand) == 21:
            print("dealer blackjack")
            game.dealdol += round.bet
            game.playdol -= round.bet
            continue
        else:
            print("no naturals")
        
            
    if handTotal(round.playhand) == 21:
        print("player blackjack")
        game.dealdol -= round.bet * 1.5
        game.playdol += round.bet * 1.5
        continue
    
    #player play
    while True:
        print(sep)
        round.displayHands()
        print()
        if handTotal(round.playhand) > 21:
            print("player busted!")
            break
        print("hit or stand?")
        print("1. hit")
        print("2. stand")
        choice = int(input())
    
        if choice == 1:
            round.draw(round.playhand)
        elif choice == 2:
            break
    if handTotal(round.playhand) > 21:
        game.dealdol += round.bet
        game.playdol -= round.bet
        continue
    
    #dealer play
    print(sep)
    round.dealplay = True
    print("dealer play")
    
    while True:
        print(sep)
        tot = handTotal(round.dealhand)
        round.displayHands()
        if tot > 21:
            print("dealer busted!")
            break
            
        if tot >= 17:
            print("stand")
            break
        else:
            print("hit")
            round.draw(round.dealhand)
    if handTotal(round.dealhand) > 21:
        game.dealdol -= round.bet
        game.playdol += round.bet
        continue

    if handTotal(round.dealhand) > handTotal(round.playhand):
        print("dealer wins round")
        game.dealdol += round.bet
        game.playdol -= round.bet
    elif handTotal(round.dealhand) < handTotal(round.playhand):
        print("player wins round")
        game.dealdol -= round.bet
        game.playdol += round.bet
    else: 
        print("tie")

