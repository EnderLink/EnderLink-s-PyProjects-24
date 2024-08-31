import random
import art

play = True


#This function retrieves a random person and their data form game_data.py
def retrieve():
    main_item = random.choice(art.data)
    return main_item


# This is the beginning protocol and intro to the game and/or round.
def beginning(first_person, second_person, score_count_requirement):
    print(art.logo)
    print(f"Compare {first_person["name"]}, a {first_person["description"]}, who/which is in {first_person["country"]}")
    print(art.vs)
    print(f"With {second_person["name"]}, a {second_person["description"]}, who/which is in {second_person["country"]}")
    print(f"Current score: {score_count_requirement}\n")


# This checks any two values and the player guess to determine if the guess was correct.
def check(guess, second_person, first_person, follower_count_1, follower_count_2, past_usages, score_count):
    second_greater_than_first = False
    round_win = False

    a = first_person["name"].lower()
    b = second_person["name"].lower()

    if follower_count_2 < follower_count_1:
        second_greater_than_first = False
    elif follower_count_2 > follower_count_1:
        second_greater_than_first = True
    else:
        print("ha")

    if guess in b and second_greater_than_first:
        round_win = True
        past_usages.append(second_person)
    elif guess in a and second_greater_than_first:
        round_win = False
    elif guess in b and not second_greater_than_first:
        round_win = False
    elif guess in a and not second_greater_than_first:
        round_win = True
        past_usages.append(first_person)
    else:
        print("help")

    return round_win


# This is the comparison phase of the game
def compare(first_person, second_person, past_usages, score_count):

    #Question
    beginning(first_person, second_person, score_count)
    guess = input("Which person do you think have more followers? ")
    fc_1 = first_person["follower_count"]
    fc_2 = second_person["follower_count"]

    return check(guess, second_person, first_person, fc_1, fc_2, past_usages, score_count)


# This introduces the two people.
def answer(past_usages, score_count):

    #Variable Setup
    person_1 = retrieve()
    person_2 = retrieve()
    while person_2["follower_count"] == person_1["follower_count"]:
        person_2 = retrieve()
    good = compare(person_1, person_2, past_usages, score_count)

    while good:

        #Uses previous person if correct
        score_count = len(past_usages)
        if len(past_usages) == 0:
            person_1 = retrieve()
        else:
            person_1 = past_usages[-1]
            person_2 = retrieve()

        #Prevents repetition
        while person_2 in past_usages:
            person_2 = retrieve

        #Game continuation
        good = compare(person_1, person_2, past_usages, score_count)
        if good:
            print(" ")
        else:
            print("you failure")
            good = False


# Game Loop
while play:

    past_usages = []
    score_count = len(past_usages)
    answer(past_usages, score_count)

    is_it_the_end = input("Shall you continue? ")

    if "no" in is_it_the_end:
        play = False
    else:
        print("I think you said yes. I think...")
