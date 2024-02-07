
class CoffeeMachine:
    def __init__(self):
        self.resources = {"water": 300,
                            "milk": 200,
                            "coffee": 100}
        self.coin_list = {'quarters': .25,
                         'dimes': .10,
                         'nickles': .05,
                         'pennies': .01}
        self.money = 0
        self.MENU = {
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
        
    def run(self):
        while True:
            order = self.ask_drink_order()
            if order == 'off':
                return
            if order == 'report':
                self.print_report()
            if order in self.MENU.keys():
                drink = self.MENU[order]
                re_order = False
                for key, value in drink["ingredients"].items():
                    if self.resources[key] < value:
                        print(f"Sorry there is not enough {key}")
                        re_order = True
                        break
                if re_order:
                    continue
                print(f'Insert coins to purchase {order} for ${drink["cost"]}.')
                payment = self.retrieve_coins()
                if payment < drink['cost']:
                    print('Sorry thats not enough money. Money refunded.')
                    continue
                if payment > drink['cost']:
                    payment_change = payment - drink['cost']
                    print(f'Here is ${payment_change} in change.')
                self.decrement_drink(order)
                self.increment_money(order)
                print(f"Here is your {order}. Enjoy!")

    def decrement_drink(self, drink_key):
        for key, value in self.MENU[drink_key]['ingredients'].items():
            self.resources[key] -= value

    def increment_money(self, drink_key):
        self.money += self.MENU[drink_key]['cost']

    def retrieve_coins(self):
        sub_total = 0
        for key, value in self.coin_list.items():
            print(f"How many {key}?")
            sub_total += int(input()) * value
        return sub_total

    def ask_drink_order(self):
        print('What would you like? (espresso/latte/cappuccino):')
        response = input()
        return str(response)
    
    def print_report(self):
        for key, item in self.resources.items():
            print(f'{key}: {item}')
        print(f'Money: ${self.money}')
        
my_machine = CoffeeMachine()