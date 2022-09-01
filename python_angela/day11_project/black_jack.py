import os
import random
import check_cards
import art

def main():  
    
    game_over = False
    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_deck = []
    cpu_deck = []
    play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if play_game == "y":
        game_over = True
    while game_over:
        os.system('cls')
        print(art.logo)
        random.shuffle(deck)
        for i in range(0, 2):
            user_deck.append(random.choice(deck))
            cpu_deck.append(random.choice(deck))
        cpu_total = 0
        for i in cpu_deck:
            cpu_total += i
        if cpu_total < 17:
            cpu_deck.append(random.choice(deck))
            for i in cpu_deck:
                cpu_total += i
        user_total = 0
        for i in user_deck:
            user_total += i
        print(f"Your cards: {user_deck}, current score: {user_total}")
        print(f"Cpu card: {cpu_deck[0]}\n")
        wrong_aswer = False
        more_cards = input("Do you want to pick another card? Typer 'y' or 'n': ")
        while not wrong_aswer:
            if more_cards == "y":
                user_deck.append(random.choice(deck))
                for i in user_deck:
                    user_total += i
                check_cards.check_cards(user_total,cpu_total,user_deck,cpu_deck)
                wrong_aswer = True
                game_over = False
            elif more_cards == "n":                
                check_cards.check_cards(user_total,cpu_total,user_deck,cpu_deck)
                wrong_aswer = True
                game_over = False

main()
