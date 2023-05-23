#####################################################################################
# CREATE SOFTWARE FOR COFFEE MACHINE
# 3 hot flavors: Espresso, Latte, Cappuccino
# Espresso: 50ml water, 18g coffee => 1.50$
# Latte: 200ml water, 24g coffee, 150ml milk => 2.50$
# Cappuccino: 250ml water, 24g coffee, 100ml milk => 3.00$
# Coin operated: Penny (1 cent), Nickel (5 cent), Dime (10 cent), Quarter (25 cent)
# Program requirements
# 1. Print report on machine resources
# 2. Check that resources are sufficient when a customer orders a drink
# 3. Process coins
# 4. Check whether the transaction was successful
# 5. Make coffee and deduct resources
#####################################################################################

MENU = {
    'espresso': {
        'ingredients': {
            'water': 50,
            'coffee': 18
        },
        'cost': 1.5
    },
    'latte': {
        'ingredients': {
            'water': 200,
            'coffee': 24,
            'milk': 150
        },
        'cost': 2.5
    },
    'cappuccino': {
        'ingredients': {
            'water': 250,
            'coffee': 24,
            'milk': 100
        },
        'cost': 3.0
    }
}

profit = 0
resources = {
    'water': 500,
    'milk': 500,
    'coffee': 500
}

def process_coins():
    '''
    Calculates total dollar amounts from coins.
    '''
    quarters = int(input('Insert quarters:'))
    dimes = int(input('Insert dimes:'))
    nickles = int(input('Insert nickles:'))
    pennies = int(input('Insert quarters:'))
    return (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)

def enough_resources(order):
    '''
    Returns whether there are enough resources to fulfill the order.
    '''
    for name, amount in MENU[order]['ingredients'].items():
        if resources[name] < amount:
            print(f'Sorry there is not enough {name}.')
            return False
        return True

def enough_money(order, money):
    '''
    Returns whether client paid enough money to pay for their order.
    '''
    order_cost = MENU[order]['cost']
    diff = money - order_cost
    global profit
    if diff < 0:
        print('Sorry that\'s not enough money. Money refunded.')
        return False
    else:
        if diff > profit:
            continue_order = input('Not enough money to give change. Do you want to continue with your order? (y/n)')
            if continue_order == 'y':
                profit += money
                return True
            elif continue_order == 'n':
                print('Okay, money refunded.')
        else:
            print(f'Here is the ${round(diff, 2)} in change.')
            profit += order_cost
            return True

def make_coffee(order):
    '''
    Removes resources and prints coffee notification.
    '''
    for name, amount in MENU[order]['ingredients'].items():
        resources[name] -= amount
    print(f'Here is your {order}. Enjoy!')


# Coffee machine
is_on = True

while is_on:
    order = input('What would you like to order? (espresso/latte/cappuccino)')
    if order == 'report':
        for resource, remaining in resources.items():
            measure = 'g' if resource == 'coffee' else 'ml'
            print(f"{resource.capitalize()}: {remaining}{measure}")
        print(f"Money: ${profit}")
    elif order == 'off':
        is_on = False
    else:
        if enough_resources(order):
            money = process_coins()
            if enough_money(order, money):
                make_coffee(order)


