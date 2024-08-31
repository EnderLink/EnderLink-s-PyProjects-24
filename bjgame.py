# Time to do Expert level!
import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
game_loop = True
game_win = False
tie = False
blackjack = False

while game_loop:

    computer_cards = []
    player_cards = []

    computer_cards.append(random.choice(cards))
    computer_cards.append(random.choice(cards))

    player_cards.append(random.choice(cards))
    player_cards.append(random.choice(cards))

    print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n ")
    print(art.logo)
    print(
        f"Your cards: {player_cards}, current score: {player_cards[0] + player_cards[1]} \n   Computer's first card: {computer_cards[0]}")

    final_score_computer = computer_cards[0] + computer_cards[1]
    final_score_player = 0
    more_cards = True

    while more_cards:
        another_card = input("Would you like another card? ")
        if "y" in another_card:
            final_score_player = 0
            player_cards.append(random.choice(cards))
            for card in player_cards:
                final_score_player += card
        else:
            more_cards = False

    if final_score_computer < 17:
        final_score_computer += random.choice(cards)
        computer_cards.append(final_score_computer - (computer_cards[0] + computer_cards[1]))

    print(
        f"  Your cards: {player_cards}, final score: {final_score_player} \n   Computer's cards: {computer_cards}, final score: {final_score_computer}")

    if final_score_computer == final_score_player:
        tie = True
    elif final_score_player == 21:
        game_win = True
        blackjack = True
    elif final_score_computer == 21:
        game_win = False
    elif final_score_player > 21:
        game_win = False
    elif final_score_computer > 21:
        game_win = False
    elif final_score_computer > final_score_player:
        game_win = False
    elif final_score_computer < final_score_player:
        game_win = True

    if tie:
        print("Tie.")
    elif game_win:
        print("You win!")
    elif not game_win:
        print("You lost!")
    elif blackjack:
        print("You got Blackjack!")
    else:
        print("I dont know what happened.")

    continue_question = input("Would you like to play again? ")
    if "y" in continue_question:
        game_loop = True
    elif "n" in continue_question:
        game_loop = False
    else:
        print("Bug detecting line. AKA: something is very wrong!")

