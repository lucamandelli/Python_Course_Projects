# espresso:
# 50ml water
# 18g coffee
# latte:
# 200ml water
# 24g coffee
# 150ml milk
# cappuccino:
# 250ml water
# 24g coffee
# 100ml milk



def main():
    import os
    import time
    import maintainer
    import coffee
    
    machine_on = True
    water = 1000
    milk = 1000
    coffee_resource = 200
    money = 0.0
    
    resources_list = [water, milk, coffee_resource, money]
    
    while machine_on:
        time.sleep(2)
        os.system('cls')
        print("What's up my dear customer!")
        machine_prompt = input("What can I get for you? espresso \tlatte \tcappuccino\n")    
        if machine_prompt == "maintainer":
            machine_on = maintainer.maintainer(resources_list, machine_on)
        if machine_prompt == "espresso":
            coffee.check_resources(machine_prompt, resources_list)
        if machine_prompt == "latte":
            coffee.check_resources(machine_prompt, resources_list)
        if machine_prompt == "cappuccino":
            coffee.check_resources(machine_prompt, resources_list)


if __name__ == '__main__':    
    main()
