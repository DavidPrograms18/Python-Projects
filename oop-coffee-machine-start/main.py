from random import choices

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

on = True


my_coffee = CoffeeMaker()
my_menu = Menu()
my_money = MoneyMachine()



while on:
    choice = input(f"What would you lke? {my_menu.get_items()}: ")
    if choice ==  "off":
        on = False
    elif choice == "report":
        my_coffee.report()
        my_money.report()
    else:
       drinks = my_menu.find_drink(choice)
       if my_coffee.is_resource_sufficient(drinks):
          if my_money.make_payment(drinks.cost):
              my_coffee.make_coffee(drinks)

