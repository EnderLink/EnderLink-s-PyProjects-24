#Note: I incorporated the lack of pennies due to the future cut of minting pennies.
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


#This is for people who don't like orders or rules
def dont_be_a_dummy(question, possible_answers, condition):
    if question not in possible_answers:
        print("For God's sake, do what I said. \nActually, I'm ending this. You are too bad of a person for me.")
        condition = False
    return condition


#Money and Coin Managing System
def payment(item, total_money, starting_values, can_create):
    #Checks if you can pay
    if MENU[item]["ingredients"]["water"] > starting_values["water"]:
        can_create = False
    elif MENU[item]["ingredients"]["milk"] > starting_values["milk"]:
        can_create = False
    elif MENU[item]["ingredients"]["coffee"] > starting_values["coffee"]:
        can_create = False
    else:
        can_create = True

    money_paid = 0
    cost = MENU[item]["cost"]

    #If you haven't paid full price yet.
    if not can_create:
        print("You are out of resources!")
    else:
        while money_paid < cost:
            quarters = int(input("How many quarters? ")) * 0.25
            dimes = int(input("How many dimes? ")) * 0.10
            nickels = int(input("How many nickels? ")) * 0.05
            money_paid = quarters + dimes + nickels

            if money_paid < cost:
                print(f"Your ${money_paid} has been refunded. Please order again.")

        print(f"Thank you! Enjoy your {item}!")

        total_money += cost

    #Taking away from current tanks
    starting_values["water"] -= MENU[item]["ingredients"]["water"]
    starting_values["milk"] -= MENU[item]["ingredients"]["milk"]
    starting_values["coffee"] -= MENU[item]["ingredients"]["coffee"]

    if money_paid > cost:
        print(f"You have ${round((money_paid - cost), 2)} in change. Here you go.")

    return total_money


#Asks what to order
def ask(starting_money, starting_values, has_ordered):
    asking = True
    possible_answers = ["espresso", "cappuccino", "report", "latte", "refill", "off"]

    #To stop repetition
    if has_ordered:
        drink = str(input(
            "Welcome to the PyCoffee Machine! What would you like to order?\n"
            + "We have espressos, cappuccinos, and lattes. ")).lower()
        has_ordered = False
    else:
        drink = str(input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nWhat would you like?" +
                          "\nOur items are espressos, cappuccinos, and lattes.\nIf we are out of resources, " +
                          "please enter 'refill' to refill them: ")).lower()

    #Determines course of action based off response.
    if "off" in drink:
        return True
    elif drink in "report":
        print(f"Water: {starting_values["water"]}ml")
        print(f"Milk: {starting_values["milk"]}ml")
        print(f"Coffee: {starting_values["coffee"]}g")
        print(f"Money: ${starting_money}")
    elif drink in "refill":
        starting_values["water"] = 300
        starting_values["milk"] = 200
        starting_values["coffee"] = 100
    elif drink != "report" or "resources":
        print(f"Please insert coins. This drink costs ${MENU[drink]["cost"]}")
        starting_money += payment(drink, starting_money, starting_values, asking)
    elif drink not in possible_answers:
        return print("Bad Person!")

    if starting_money != 0:
        return starting_money


def game():
    starting_values = {"water": 300,
                       "milk": 200,
                       "coffee": 100}
    ordering = True
    record = True
    money = 0

    #Game loop
    while ordering:

        record = ask(money, starting_values, record)

        if type(record) == float:
            money += record

        record = False

        if record:
            return

        continue_ordering = input("Would you like to order again? ").lower()

        if "ye" in continue_ordering:
            ordering = True
        elif "no" in continue_ordering:
            ordering = False
        else:
            print("Really? You should have ordered...")
            ordering = False


game()
