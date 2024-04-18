
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


def print_report():
    for key in resources:
        if key == "water" or key == "milk":
            print(f"{key.capitalize()}: {resources[key]}ml")
        elif key == "coffee":
            print(f"{key.capitalize()}: {resources[key]}g")
        elif key == "money":
            print(f"Money: ${resources[key]}")


def check_resources(drink):
    drink_resources = list(drink.values())[0]
    for resource in drink_resources:
        resource_value = drink_resources[resource]
        if resources[resource] - resource_value < 0:
            print(f"Sorry there is not enough {resource}.")
            return False
    return True


def process_coins():
    print("Please insert coins.")
    quarters = float(input("how many quarters?: "))
    dimes = float(input("how many quarters?: "))
    nickles = float(input("how many quarters?: "))
    pennies = float(input("how many quarters?: "))
    return (0.01 * pennies) + (0.05 * nickles) + (0.10 * dimes) + (0.25 * quarters)


def is_successful(given_sum,drink_cost):
    if given_sum >= drink_cost:
        change = (given_sum - drink_cost).__round__(2)
        print(f"Here is ${change} in change.")
        resources["money"] += drink_cost
        return True
    elif given_sum < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffe(drink):
    drink_resources = list(drink.values())[0]
    for drink_resource in drink_resources:
        drink_resource_value = drink_resources[drink_resource]
        resources[drink_resource] -= drink_resource_value


def coffee_machine():
    done = False
    while not done:
        todo = input("  What would you like? (espresso/latte/cappuccino): ")
        if todo == "report":
            print_report()
        elif todo == "off":
            done = True
        else:
            drink = MENU[todo]
            if check_resources(drink):
                given_sum = process_coins()
                drink_cost = list(drink.values())[1]
                success = is_successful(given_sum, drink_cost)
                if success:
                    make_coffe(drink)
                    print(f"Here is your {todo}. Enjoy!")


coffee_machine()