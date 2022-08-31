machine_on = True
water = 100
milk = 50
coffee = 76
money = 0.0
while machine_on:
    machine_prompt= input("What would you like? \tespresso:1 \tlatte:2 \tcappuccino:3\n")    
    if machine_prompt == "maintainer":
        maintainer