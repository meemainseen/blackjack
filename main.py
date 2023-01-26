'''computer version of blackjack game'''

import random
import os
from art import logo

'''Rules
    The deck is unlimited in size. 
    There are no jokers. 
    The Jack/Queen/King all count as 10.
    The the Ace can count as 11 or 1.
    Uses the list as the deck of cards: cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    The cards in the list have equal probability of being drawn.
    Cards are not removed from the deck as they are drawn.
    The computer is the dealer.
'''
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#Ace = 11

def deal_card(hand):
    ''' deal a random card and append to the player's cards in hand'''
    deal = random.choice(cards)
    hand.append(deal)
    return hand

def calculate_score(hand):
    '''calculates the sum of the cards with the player with some conidtions'''
    # Checks if there's a blackjack and returns score as 0 if true. Only two cars in hand with one Ace and other 10 >> 11 + 10
    if len(hand) == 2 and sum(hand) == 11:
        return 0
    # if sum of the cards exceeds 21 and there's an ace in hand, replaced valued of ace with 1
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)
    # returns sum of cards in hand
    return sum(hand)

def compare_score(user_score, computer_score):
    '''Compares scores and announces win or lose based on the defined conditions'''
    # Checks for blackjact, first with computer, if not then with user
    if computer_score == 0:
        return "Opponent gets a blackjack. You lose 😥"
    elif user_score == 0:
        return "You win with a blackjack 😀"
    elif user_score == computer_score:
        return "It's a draw 🙃"
    elif user_score > 21:
        return "You wen over. You lose 😥"
    elif computer_score > 21:
        return "Opponent went over. You win 😀"
    elif computer_score > user_score:
        return "You lose 😥"
    else:
        return "You win! 😀"
    

'''Play game is defined as a function to be played in a while loop as long as user wishes to replay the game'''
def play_game():

    user_cards = []
    computer_cards = []
    game_over = False

    print(logo)
    # Game begins by drawing two random cards for each player. Computer hand only reveals first card in hand
    for _ in range(2):
        user_cards = deal_card(user_cards)
    for _ in range(2):
        computer_cards = deal_card(computer_cards)

    # User loop repeats till the time they choose to pass 
    while not game_over:
        # Calculate user and computer score.
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"    Your hand: {user_cards}, Current Score: {user_score}")
        # For computer only first card in hand is revealed
        print(f"    Computer's first card: {computer_cards[0]}")

        # At this point if either of the players get a blackjack or user scroe exceeds 21 game is over
        if computer_score == 0 or user_score == 0 or user_score > 21:
            game_over = True
        # If not game over it should ask user ot draw a card and repeat the calculation loop. If user chooses no for pass game is over
        else:
            cont = input("Draw another card? 'y' for yes or 'n' for pass: ")
            if cont == 'y':
                user_cards = deal_card(user_cards)
            else:
                game_over = True

    # The game enters in computer loop for drawing cards after user chooses no to pass
    # While it's not a blackjack for computer and score is less than 17 it will continue deal_card and update calculated score
    while computer_score != 0 and computer_score < 17:
        computer_cards = deal_card(computer_cards)
        computer_score = calculate_score(computer_cards)

    '''Printing out the result of the game towards the end'''
    # Final hand and scores for both players
    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
    # Outcome of the game
    print(compare_score(user_score, computer_score))

'''While loop based on user input to replay the game
    Clears the screen
    Invokes play_game() function
    Ends as user choosed n to pass the replay option'''
while input("Play a game of blackjack? 'y' for yes or 'n' to pass: ") == 'y':
    os.system('clear')
    play_game()