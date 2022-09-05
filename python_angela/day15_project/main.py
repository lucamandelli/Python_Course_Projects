
def main():
    import os
    import time
    import maintainer
    import coffee
    
    machine_on = True
    water = 10
    milk = 100
    coffee_resource = 200
    money = 0.0
    
    resources_list = [water, milk, coffee_resource, money]
    
    while machine_on:
        time.sleep(2)
        os.system('cls')
        print("What's up my dear customer!")
        machine_prompt = input("What can I get for you? espresso $1.5 \tlatte $2.5  \tcappuccino $3\n")    
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
