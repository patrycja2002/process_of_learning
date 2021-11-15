# Classes Challenge 37: Casino Black Jack App
import random
import time


class Card:
    def __init__(self, rank, value, suit):
        self.rank = rank
        self.value = value
        self.suit = suit

    def display_card(self):
        print(self.rank + " of " + self.suit)


class Deck:
    def __init__(self):
        self.cards = []

    def build_deck(self):
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        ranks = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10,
                 "A": 11, }
        for suit in suits:
            for rank, value in ranks.items():
                card = Card(rank, value, suit)
                self.cards.append(card)

    def shuffle_deck(self):
        random.shuffle(self.cards)

    def deal_card(self):
        card = self.cards.pop()
        return card


class Player:
    def __init__(self):
        self.hand = []
        self.hand_value = 0
        self.playing_hand = True

    def draw_hand(self, deck):
        for x in range(2):
            card = deck.deal_card()
            self.hand.append(card)

    def display_hand(self):
        print("\nPlayer's Hand: ")
        for card in self.hand:
            card.display_card()

    def hit(self, deck):
        card = deck.deal_card()
        self.hand.append(card)

    def get_hand_value(self):
        self.hand_value = 0
        ace_in_hand = 0
        for card in self.hand:
            self.hand_value += card.value
            if card.rank == "A":
                ace_in_hand = True
        if self.hand_value > 21 and ace_in_hand:
            self.hand_value -= 10
        print("Total value: " + str(self.hand_value))

    def update_hand(self, deck):
        if self.hand_value < 21:
            choice = input("Would you like to hit (y/n):").lower()
            if choice == "y":
                self.hit(deck)
            else:
                self.playing_hand = False

        else:
            self.playing_hand = False


class Dealer:
    def __init__(self):
        self.hand = []
        self.hand_value = 0
        self.playing_hand = True

    def draw_hand(self, deck):
        for x in range(2):
            card = deck.deal_card()
            self.hand.append(card)

    def display_hand(self):
        input("\nPress enter to reveal the dealer's hand. ")
        for card in self.hand:
            card.display_card()
            time.sleep(1)

    def hit(self, deck):
        self.get_hand_value()
        while self.hand_value < 17:
            card = deck.deal_card()
            self.hand.append(card)
            self.get_hand_value()
        print("\nDealer is set with a total of " + str(len(self.hand)) + " cards.")

    def get_hand_value(self):
        self.hand_value = 0
        ace_in_hand = False
        for card in self.hand:
            self.hand_value += card.value
            if card.rank == "A":
                ace_in_hand = True
        if self.hand_value > 21 and ace_in_hand:
            self.hand_value -= 10


class Game:
    def __init__(self, money):
        self.money = int(money)
        self.bet = 20
        self.winner = " "

    def set_bet(self):
        betting = True
        while betting:
            bet = int(input("What would you like to bet (minimum bet of 20): "))
            if bet < 20:
                bet = 20
            elif bet > self.money:
                print("")
            else:
                self.bet = bet
                betting = False

    def scoring(self, player_value, dealer_value):
        if player_value == 21:
            print("You got BLACK JACK!!! You win!")
            self.winner = "p"
        elif dealer_value == 21:
            print("The dealer got black jack...You loose!")
            self.winner = "d"
        elif player_value > 21:
            print("You went over 21...You loose!")
            self.winner = "d"
        elif dealer_value > 21:
            print("Dealer went over 21! You win!")
            self.winner = "p"
        else:
            if dealer_value > player_value:
                print("Dealer gets " + str(dealer_value) + ". You loose.")
                self.winner = "d"
            elif dealer_value < player_value:
                print("Dealer gets " + str(dealer_value) + ". You win!")
                self.winner = "p"
            else:
                print("Dealer gets " + str(dealer_value) + ". It's a push...")
                self.winner = 'tie'

    def payout(self):
        if self.winner == "p":
            self.money += self.bet
        elif self.winner == 'd':
            self.money -= self.bet

    def display_money(self):
        print("\nCurrent Money: $" + str(self.money))

    def display_money_and_bet(self):
        print("\nCurrent Money: $" + str(self.money) + "\t\tCurrent Bet: $" + str(self.bet))


print("Welcome to the Casino Blackjack App")
print("The minimum bet at this table is $20.")

money = int(input("\nHow much money are you willing to play with today: "))
game = Game(money)

playing = True
while playing:
    game_deck = Deck()
    game_deck.build_deck()
    game_deck.shuffle_deck()

    player = Player()
    dealer = Dealer()

    game.display_money()
    game.set_bet()

    player.draw_hand(game_deck)
    dealer.draw_hand(game_deck)

    game.display_money_and_bet()
    print("The dealer is showing a " + dealer.hand[0].rank + " of " + dealer.hand[0].suit + ".")
    while player.playing_hand:
        player.display_hand()
        player.get_hand_value()
        player.update_hand(game_deck)

    dealer.hit(game_deck)
    dealer.display_hand()

    game.scoring(player.hand_value, dealer.hand_value)
    game.payout()

    if game.money < 20:
        playing = False
        print("Sorry, you ran out of money. Please try again.")
