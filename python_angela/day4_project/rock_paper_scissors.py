import random


def rock_paper_scissors():
    print("Welcome to the rock, paper and scissors game!")
    player = int(input("Choose 0 for rock, 1 for paper and 2 for scissors: "))
    cpu = random.randint(0,2)
    
    options_list = ["Rock", "Paper", "Scissors"]
    ascii_list = ["""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """, """
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """, """
       _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """]
    
    if player == cpu:
        print(f"\nYou picked {options_list[player]}\n{ascii_list[player]}\nand CPU picked {options_list[cpu]}\n{ascii_list[cpu]}")
        print("That's a draw!")
    elif player == 0 and cpu == 1:
        print(f"\nYou picked {options_list[player]}\n{ascii_list[player]}\nand CPU picked {options_list[cpu]}\n{ascii_list[cpu]}")
        print("CPU wins! You lost :(")
    elif player == 0 and cpu == 2:
        print(f"\nYou picked {options_list[player]}\n{ascii_list[player]}\nand CPU picked {options_list[cpu]}\n{ascii_list[cpu]}")
        print("You win! Congratulations!!")
    elif player == 1 and cpu == 0:
        print(f"\nYou picked {options_list[player]}\n{ascii_list[player]}\nand CPU picked {options_list[cpu]}\n{ascii_list[cpu]}")
        print("You win! Congratulations!")
    elif player == 1 and cpu == 2:
        print(f"\nYou picked {options_list[player]}\n{ascii_list[player]}\nand CPU picked {options_list[cpu]}\n{ascii_list[cpu]}")
        print("CPU wins! You lost :(")
    elif player == 2 and cpu == 0:
        print(f"\nYou picked {options_list[player]}\n{ascii_list[player]}\nand CPU picked {options_list[cpu]}\n{ascii_list[cpu]}")
        print("CPU wins! You lost :(")
    elif player == 2 and cpu == 1:
        print(f"\nYou picked {options_list[player]}\n{ascii_list[player]}\nand CPU picked {options_list[cpu]}\n{ascii_list[cpu]}")
        print("You win! Congratulations!")  


rock_paper_scissors()
