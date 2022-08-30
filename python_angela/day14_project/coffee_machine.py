machine_on = True
water = 100
milk = 50
coffee = 76
money = 2.5
while machine_on:
    machine_prompt= input("What would you like? \tespresso:1 \tlatte:2\tcappuccino:3\n")
    if machine_prompt == "off":
        print("The Coffee Machine is Turning Off...")
        machine_on = False
    if machine_prompt == "report":
        print(f"\nThe resources availabe are: \nWater: {water}ml \nMilk: {milk}ml \nCoffee: {coffee}g \nMoney: ${money}\n")
    if machine_prompt == "maintain":
        refill = True
        while refill:
            more_refill = "yes"
            which_fill = input("Which one you want to refill: \t1:Water \t2:Milk \t3:Coffee")
            if which_fill == 1:
                water_refill = input("How much water in mililiters: ")
                water = water_refill
                more_refill = input("Refill another one? type 'yes' or 'no' ")
            elif which_fill == 2:
                milk_refill = input("How much milk in mililiters: ")
                milk = milk_refill
                more_refill = input("Refill another one? type 'yes' or 'no' ")
            elif which_fill == 3:
                coffee_refill = input("How much coffee in grams: ")
                coffee = coffee_refill
                more_refill = input("Refill another one? type 'yes' or 'no' ")
            else:
                print("ERROR, please type 1, 2 or 3")
            if more_refill == "no":
                refill = False