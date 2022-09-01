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

def check_resources(machine_prompt, resource_list):
    if machine_prompt == "espresso":
        espresso(resource_list)
