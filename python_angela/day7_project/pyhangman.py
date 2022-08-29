import random
from hangman_text import word_list
from hangman_art import logo,stages


def pyhangman():
    print(f"{logo}\n\n\n\n")
    lives = 6
    chosen_word = random.choice(word_list)
    chosen_list = []
    
    for i in range(len(chosen_word)):
        chosen_list += "_"
    
    end_game = False
    
    while not end_game:
        print(f"{' '.join(chosen_list)}")
        guess = input("\n\nGuess a letter: ").lower() 
        
        if guess in chosen_list:
            print(f"You've already guessed {guess}")
        
        for i in range(len(chosen_word)):        
            if chosen_word[i] == guess:            
                chosen_list[i] = guess
            
        if guess not in chosen_word:
            lives -=1
            print(f"You guessed {guess}, that's not in the word. You lose a life")
            print(f"You have only {lives} left")
            print(stages[lives])
            
        if lives == 0:
            print(stages[lives])
            print(f"\nThe word was {chosen_word}")
            print("\nGAME OVER")
            end_game = True

        if "_" not in chosen_list:
            end_game = True
            print("\nYOU WON")


pyhangman()
