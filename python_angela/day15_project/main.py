import os
import time

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
    import maintainer
    machine_on = True
    water = 100
    milk = 50
    coffee = 76
    money = 0.0
    while machine_on:
        time.sleep(2)
        os.system('cls')
        print("What's up my dear customer!")
        machine_prompt = input("What can I get for you? \tespresso:1 \tlatte:2 \tcappuccino:3\n")    
        if machine_prompt == "maintainer":
            machine_on = maintainer.maintainer(water, milk, coffee, money, machine_on)


if __name__ == '__main__':    
    main()
