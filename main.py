from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

on = True

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


while on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        on = False
    else:
        item = menu.find_drink(choice)
        if item:
            if coffee_maker.is_resource_sufficient(item):
                if money_machine.make_payment(item.cost):
                    coffee_maker.make_coffee(item)