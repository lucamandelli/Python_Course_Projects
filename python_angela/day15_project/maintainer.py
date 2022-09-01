import os


def maintainer(resources_list, machine_on):
    os.system('cls')
    right_passwd = False
    password = input("Please type the password for maintainer: ")
    while not right_passwd:            
        if password == "987654321":                
            print("Hello maintainer")                                
            machine_prompt= int(input("What are you looking for? 1:Report \t2:Refill \t3:Shut Down \t4:Leave\n"))                 
            if machine_prompt == 1:
                print(f"\nThe resources availabe are: \nWater: {resources_list[0]}ml \nMilk: {resources_list[1]}ml \nCoffee: {resources_list[2]}g \nMoney: ${resources_list[3]}\n")
            elif machine_prompt == 2:
                refill = True
                while refill:
                    more_refill = "yes"
                    which_fill = input("Which one you want to refill: \t1:Water \t2:Milk \t3:Coffee\n")
                    if which_fill == "1":
                        water_refill = int(input("How much water in mililiters: "))
                        resources_list[0] += water_refill
                        more_refill = input("Refill another one? type 'yes' or 'no' ")
                    elif which_fill == "2":
                        milk_refill = int(input("How much milk in mililiters: "))
                        resources_list[1] += milk_refill
                        more_refill = input("Refill another one? type 'yes' or 'no' ")
                    elif which_fill == "3":
                        coffee_refill = int(input("How much coffee in grams: "))
                        resources_list[2] += coffee_refill
                        more_refill = input("Refill another one? type 'yes' or 'no' ")
                    else:
                        print("ERROR, please type 1, 2 or 3")
                    if more_refill == "no":
                        os.system('cls')
                        refill = False
            elif machine_prompt == 3:
                right_passwd = True
                print("The Coffee Machine is Turning Off...")    
                machine_on = False            
                return machine_on
            elif machine_prompt == 4:
                print("Leaving maintainer terminal...")
                right_passwd = True
                machine_on = True
                os.system('cls')
                return machine_on
        else:
            print("\nWrong Password\n")
            right_passwd = True
            machine_on = True
            return machine_on

