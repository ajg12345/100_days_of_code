from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

if __name__ == "__main__":
    my_coffee_maker = CoffeeMaker()
    my_menu = Menu()
    my_money_machine = MoneyMachine()
    while True:
        print(f"What would you like? ({my_menu.get_items()})")
        order = input()
        if order == "off":
            break
        if order == "report":
            my_coffee_maker.report()
            my_money_machine.report()
            continue
        drink = my_menu.find_drink(order)
        if not drink:
            continue
        if my_coffee_maker.is_resource_sufficient(drink) and my_money_machine.make_payment(drink.cost):
            my_coffee_maker.make_coffee(drink)