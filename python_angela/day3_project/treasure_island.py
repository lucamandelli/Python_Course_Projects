def treasure_island():
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")
    choice1 = input("Do you want to go left or right? ").lower()
    
    if "left" in choice1:
        print("\nVery nice, you made the right choice!")
        print("But now you must choose again!")
        choice2 = input("Do you want to wait on a rock that's near a lava river or swim in a very dangerous swamp????? ").lower()
        
        if "wait" in choice2:
            print("\nThank's god you made a wise choice!")  
            print("But you're not safe yet!")  
            print("You thought it was time to run, and after 10 miles running, you stumbled against 3 doors!!")  
            print("Each of them have 3 different colours")  
            choice3 = input("Which door you want to get in? Red, Yellow or Blue? ").lower()
            
            if "yellow" in choice3:
                print("\nLET'S GOOOOOOOOOOOOOOOOOOOO, YOU WON!!!")
                print("Congratulations, you're the best!!!!")
                print("Thank's for playing")
            elif "blue" in choice3:
                print("\nNOOOOOOOOOO, you were almost there!")
                print("There were FIVE beasts there, and they teared you apart :(")
                print("GAME OVER")
                return
            else:
                print("\nNOOOOOOOOOO, you were almost there!")
                print("A HUGE bucket of lava was on top of the door, and fell on you! You were burnt and died :(")
                print("GAME OVER")
                return
        else:
            print("\nYou chose to swim, and a VERY big TROUT came by and attacked you")
            print("You're dead... poor guy...")
            print("GAME OVER")
            return
    else:
        print("\nREAAAALY???? You picked the wrong decision in the first one???")
        print("Look's like you did... you started running to the right and fell into a hole.")
        print("GAME OVER")
        return
        
treasure_island()