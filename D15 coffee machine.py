MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
    "money": 0
}


def report():
    return resources


def resource_check():
    global resources
    for i in resources:
        if resources[i] < 0:
            var = 0
        else:
            var = 1
        return var


def coin_check(quarter, dimes, nickles, pennies, order):
    global MENU
    global money_given
    global money_req
    money_given = 0.25 * quarter + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
    money_req = MENU[order]["cost"]
    if money_req == money_given:
        return 0
    elif money_given < money_req:
        return -1
    else:
        return money_req


def code():
    global MENU
    global resources
    order = input("What would you like to have? cappuccino, latte or espresso\n")
    if order == "off":
        exit()
    elif order == "report":
        print(resources)
    elif order == "cappuccino":
        requirement = MENU['cappuccino']['ingredients']
        for i in requirement:
            resources[i] = resources[i] - requirement[i]
        if resource_check() == 1:
            print("Insert coins")
            quarter = int(input('Quarters ='))
            dimes = int(input('Dimes ='))
            nickles = int(input('Nickles ='))
            pennies = int(input('Pennies ='))
            coin_cal = coin_check(quarter, dimes, nickles, pennies, order)
            if coin_cal == -1:
                print("Sorry that's not enough money. Money refunded.")
            elif coin_cal == 0:
                print("Here's your drink")
                resources["money"] += money_req
            else:
                print("Here's your drink")
                print(f"Here's your change of {money_given - money_req}")
                resources["money"] += money_req
    elif order == "latte":
        requirement = MENU['latte']['ingredients']
        for i in requirement:
            resources[i] = resources[i] - requirement[i]
        if resource_check() == 1:
            print("Insert coins")
            quarter = int(input('Quarters ='))
            dimes = int(input('Dimes ='))
            nickles = int(input('Nickles ='))
            pennies = int(input('Pennies ='))
            coin_cal = coin_check(quarter, dimes, nickles, pennies, order)
            if coin_cal == -1:
                print("Sorry that's not enough money. Money refunded.")
            elif coin_cal == 0:
                print("Here's your drink")
                resources["money"] += money_req
            else:
                print("Here's your drink")
                print(f"Here's your change of {money_given - money_req}")
                resources["money"] += money_req
    elif order == "espresso":
        requirement = MENU['espresso']['ingredients']
        for i in requirement:
            resources[i] = resources[i] - requirement[i]
        if resource_check() == 1:
            print("Insert coins")
            quarter = int(input('Quarters ='))
            dimes = int(input('Dimes ='))
            nickles = int(input('Nickles ='))
            pennies = int(input('Pennies ='))
            coin_cal = coin_check(quarter, dimes, nickles, pennies, order)
            if coin_cal == -1:
                print("Sorry that's not enough money. Money refunded.")
            elif coin_cal == 0:
                print("Here's your drink")
                resources["money"] += money_req
            else:
                print("Here's your drink")
                print(f"Here's your change of {money_given - money_req}")
                resources["money"] += money_req
    code()


code()
