def espresso(resource_list):
    import time
    if resource_list[0] >= 50 and resource_list[2] >= 18:
        print("Espresso bein made...")
        time.sleep(4)
        print("Your espresso is ready! Have a great time!")
        resource_list[0] -= 50
        resource_list[2] -= 18
    else:
        print("The machine does not have enough resources...")

def latte(resource_list):
    import time
    if resource_list[0] >= 200 and resource_list[1] >= 150 and resource_list[2] >= 24:
        print("Latte bein made...")
        time.sleep(4)
        print("Your latte is ready! Have a great time!")
        resource_list[0] -= 200
        resource_list[1] -= 150
        resource_list[2] -= 24
    else:
        print("The machine does not have enough resources...")

def cappuccino(resource_list):
    import time
    if resource_list[0] >= 250 and resource_list[1] >= 100 and resource_list[2] >= 24:
        print("Cappuccino bein made...")
        time.sleep(4)
        print("Your cappuccino is ready! Have a great time!")
        resource_list[0] -= 250
        resource_list[1] -= 100
        resource_list[2] -= 24
    else:
        print("The machine does not have enough resources...")

def payment():
    print("Please insert coins.")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.1
    total += int(input("How many nickles? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total

# def successful_transaction(money_received, drinl_cost):
#     if money_received >= drinl_cost:


def check_resources(machine_prompt, resource_list):
    type_coffee = True
    while type_coffee:
        if machine_prompt == "espresso":
            espresso(resource_list)
            type_coffee = False
        elif machine_prompt == "latte":
            latte(resource_list)
            type_coffee = False
        elif machine_prompt == "cappuccino":
            cappuccino(resource_list)
            type_coffee = False
        else:
            print("Please select one of the options!")