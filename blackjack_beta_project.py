import random
faces = {"A": 11, "J": 10, "Q": 10, "K": 10} #cards with faces
card_list = []
class CARD (object): #initialize the class card
    

    def __init__(self, suit, rank): #constructor method
        self.suit = suit    #defining suit and rank from __init__ method
        self.rank = rank
    
        if self.rank in faces:            #if rank is in faces
            self.value = faces[self.rank]   #then self.value gets the "value" from the faces keys
            
        else:                           #if not, self.value is equal to self.rank
            self.value = int(self.rank)

    
    def __repr__(self): #method to print the object
        return f" suit: {self.suit} rank: {self.rank} value: {self.value} "

ranks = [str(i) for i in range(2, 11)] + list('JQKA')  #list of the ranks as a string from the number 2 to 11, with a sum of the ranks "jkqa"

for suit in "♠", "♥", "♦", "♣": #suit gets through the suits strings
    for rank in ranks: #rank gets through the list of ranks
        card_list.append(CARD(suit, rank)) #the card_list gets the elements from the CARD Class, using the properties of suit, and rank arguments.

class DECK(object):
    def __init__(self, card_list) -> None:
        self.card_list = card_list
    
    def draw (self):
        """draw_card = random.choice(self.card_list)
        return draw_card
        self.card_list.remove(draw_card) """
        return self.card_list.pop(0)


    def shuffle(self):
        random.shuffle(self.card_list)
        print("The deck is now shuffled!")
    
    def __repr__(self) -> str:
        return f"cards: {self.card_list}"



class PLAYER (object):
    def __init__(self, name, hand = None, coins = int) -> None:
        self.name = name
        self.hand = hand if hand else []
        self.coins = coins
    
    def user_name(self):
        self.name = input("Please insert your name!: ")
        return self.name
    
    def draw(self, deck, n=1):
        for _ in range(n):
            self.hand.append(deck.draw())

    def add_coins(self, amount = int):
        self.coins += amount 
        return self.coins
    
    def remove_coins (self, amount = int):
        self.coins -= amount
        return self.coins

    
    def __repr__(self) -> str:
        return f"player name: {self.name}, player hand: {self.hand} player coins {self.coins}"
    
class SCORE(object):
    def __init__(self, player_hand) -> None:
        self.player_hand = player_hand

    def points(self):
     
        aces_in_hand = len([card.rank for card in self.player_hand if card.rank == "A"])
        initial_score = sum([card.value for card in self.player_hand])
        if aces_in_hand and initial_score > 21:
            for xd in range(aces_in_hand):
                new_score = initial_score - ((xd + 1) * 10)
                if new_score <= 21:
                    return new_score
        return initial_score


while True:
    new_game = input("Welcome to the Blackjack text game!\nYou need to get 200 coins to win!\nPress (n)ew game to begin: ")
    if new_game == "n":
        user_name_input = input("Please enter your name!: ")
        user_name = PLAYER(user_name_input, None, 100)
        house_cpu = PLAYER("Dealer")
        while 0 < user_name.coins <= 200:
            try:
                coins_bet = int(input(f"You already have {user_name.coins} coins! How many do you want to bet?: "))
                if coins_bet <= 0 or coins_bet > user_name.coins:
                    print("Please input a valid bet amount")
                    continue  
            except ValueError:
                 print("Please input an integer!")
                 continue
            deck_1 = DECK(card_list) #link with the class
            deck_1.shuffle()
            user_name.draw(deck_1, 2)
            score_player = SCORE(user_name.hand)
            house_cpu.draw(deck_1, 1)
            score_dealer = SCORE(house_cpu.hand)
            print(f"Your hand is: {user_name.hand}. Its value sums = {score_player.points()}")
            print(f"The hand of the {house_cpu.name} is {house_cpu.hand} and have 1 card hidden!")
            draw_card = input("Do you want to draw another card? Press (y)es to draw or any other key to keep your current hand ")
            if draw_card == "y":
                user_name.draw(deck_1, 1)
                print(f"Your new hand is: {user_name.hand} Its value sums = {score_player.points()}")
                if score_player.points() >= 22:
                   user_name.remove_coins(coins_bet)
                   print(f"Busted! Your hand sums {score_player.points()} You lost {coins_bet} coins :c")
                   user_name.hand.clear()
                   house_cpu.hand.clear()
                else:
                    pass
            else:
                pass
            
            house_cpu.draw(deck_1, 1)
            if score_player.points() > score_dealer.points():
                print(f"{user_name.name} won! The hand of the {house_cpu.name} was:  {house_cpu.hand} and its values sums: {score_dealer.points()}")
                print(f"You also won {coins_bet} coins!")
                user_name.add_coins(coins_bet)
                user_name.hand.clear()
                house_cpu.hand.clear()
                continue
            elif score_player.points() == score_dealer.points():
                print("It's a draw!")
                user_name.hand.clear()
                house_cpu.hand.clear()
                continue
            else:
                print(f"I'm sorry {user_name.name} but the house has won with this hand: {house_cpu.hand} that sums {score_dealer.points()} ")
                user_name.remove_coins(coins_bet)
                user_name.hand.clear()
                house_cpu.hand.clear()
                continue
        if user_name.coins > 200:
            print("You won the game!")
            break
        else:
            print("You lost the game :c")
            break

    else:
        print("please enter a valid input!")
    




