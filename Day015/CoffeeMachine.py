"""

Andrew Dale

Subject/Class:
100 Days of Code: The Complete Python Pro Bootcamp for 2023 by Dr. Angela Yu

Day:
15

Project:
Coffee Machine

"""

import menu 


def get_selection():
    valid_input = False
    types = [x for x in menu.MENU.keys()]
    while not valid_input:
        selection = input("What type of coffee would you like? (espresso/latte/cappuccino): ")
        if selection.lower() == 'off' or selection == 'report' or selection in types:
            return selection
        else:
            print("Invalid input. Please try again.")

def process_change():
    # Since it's a mock coffee machine I'll work under the assumption
    # that it only has numerical buttons and not error handle this
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    return quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01

def print_report():
    for resource in menu.resources:
        if resource == 'water' or resource == 'milk':
            print(f"{resource}: {menu.resources[resource]}ml")
        elif resource == 'coffee':
            print(f"{resource}: {menu.resources[resource]}g")
        else:
            print(f"{resource}: " + "${:.2f}".format(menu.resources[resource]))
            

    
    
def coffee_maker_loop():
    machine_active = True
    while machine_active:
        selection = get_selection()
        if selection == 'off':
            print("Goodbye!")
            machine_active = False
        elif selection == 'report':
            print_report()
        else:
            have_resources = True
            for resource in menu.resources:
                if resource in menu.MENU[selection]['ingredients']:
                    if menu.resources[resource] < menu.MENU[selection]['ingredients'][resource]:
                        print(f"Sorry, there is not enough {resource}.")
                        have_resources = False
            if have_resources:
                money = process_change()
                cost = menu.MENU[selection]['cost']
                if money >= cost:
                    change = money - cost
                    ingredient_list = menu.MENU[selection]['ingredients']
                    for resource in menu.resources:
                        if resource in ingredient_list:
                            menu.resources[resource] -= ingredient_list[resource]
                    menu.resources['money'] += cost
                    if change > 0:
                        print("Here is ${:.2f} dollars in change.".format(change))
                    print(f"Here is your {selection}. Enjoy!")
                else:
                    print("Sorry, that's not enough money. Money refunded.")
            
            
                    








