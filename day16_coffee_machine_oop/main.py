# Recreate coffee machine but using object oriented programming
# The files coffee_maker, menu and money_machine are provided within the course

from day16_coffee_machine_oop.menu import Menu, MenuItem
from day16_coffee_machine_oop.coffee_maker import CoffeeMaker
from day16_coffee_machine_oop.money_machine import MoneyMachine

is_on = True

while is_on:
    coffee_machine = CoffeeMaker()
    money_machine = MoneyMachine()
    menu = Menu()
    order_name = input(f'What would you like to order? ({menu.get_items()})')
    if order_name == 'report':
        coffee_machine.report()
        money_machine.report()
    elif order_name == 'off':
        is_on = False
    else:
        drink = menu.find_drink(order_name)
        if drink is not None:
            cost = drink.cost
            payment = money_machine.make_payment(cost)
            coffee_machine.make_coffee(drink)