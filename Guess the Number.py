import random
playing = True

"""These are the functions that will be in the game loop. They provide the actions of the game."""


# Makes the number to be chosen.
def generate_random_number():
    random_number = random.randint(0, 100)
    return random_number


# Creates the difficulty
def difficulty(question):
    if "hard" in question:
        return 5
    elif "easy" in question:
        return 10
    else:
        return 12220


# The guessing protocol (uses functions above)
def game_guessing_protocol():
    round_over = False

    while not round_over:

        round_over = False
        difficulty_of_game = input("What is the difficulty? Easy or hard? ").lower()
        lives = difficulty(difficulty_of_game)
        number_to_be_picked = generate_random_number()
        guessing = True

        while guessing:
            guess = int(input("Make a guess: "))
            incorrect_guesses = []

            if guess in incorrect_guesses:
                print("Please pick another number.")
            elif guess > number_to_be_picked:
                print("Too High!")
                lives -= 1
                incorrect_guesses.append(guess)
            elif guess < number_to_be_picked:
                print("Too Low!")
                lives -= 1
                incorrect_guesses.append(guess)
            elif guess == number_to_be_picked:
                print(f"You got it! The number was {number_to_be_picked}")
                round_over = True
                guessing = False
            else:
                print("i dunno")

            print(f"{lives} lives left.")
            print("\n \n \n")

            if lives == 0:
                print("Game Over!")
                print(f"You lost... The number was {number_to_be_picked}")
                round_over = True
                guessing = False

while playing:
    print("Welcome to Guess That Number!\nI am thinking of a number between 1 and 100.")
    game_guessing_protocol()

    player_continue = input("Will you play again? ")
    if "y" in player_continue:
        playing = True
    else:
        playing = False