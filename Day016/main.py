from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


machine_active = True
while machine_active:
    item = input(f"What would you like? ({machine_menu.get_items()}): ")

    if item == 'off':
      machine_active = False
    elif item == 'report':
      coffee_maker.report()
      money_machine.report()
    else:
        menu_item = machine_menu.find_drink(item)
        if menu_item is not None:
            if coffee_maker.is_resource_sufficient(menu_item):
              if money_machine.make_payment(menu_item.cost):
                coffee_maker.make_coffee(menu_item)
