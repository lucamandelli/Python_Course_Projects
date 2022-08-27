import random


def rich_sorting_game():
    names = input("Give me everebody's names, separated by a comma:  ")
    names_list = names.split(", ")
    
    print(f"\n{random.choice(names_list)} is going to pay for the meal today!")

rich_sorting_game()
