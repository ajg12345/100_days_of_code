"""
project requirements:
print a report of all coffee resources
    water
    milk
    coffee
    money
check resources sufficient when order is placed
process coins
    quarters
    dimes
    nickels
    pennies
check transaction successful
make coffee
    espresso
    latte
    cappuccino
"""

if __name__ == "__main__":
    from src.coffeemachine import my_machine
    my_machine.run()