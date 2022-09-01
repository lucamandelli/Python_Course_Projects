def check_cards(user_total, cpu_total, user_deck, cpu_deck):
    if user_total > 21:
        print(f"Your cards: {user_deck}. You loose, the sum of your cards were over 21: {user_total} ")
    elif user_total <= 21 and user_total > cpu_total and cpu_total <= 21:
        print(f"Your cards: {user_deck} and CPU cards: {cpu_deck}. You win, the sum of your cards were: {user_total} and the CPU sum was: {cpu_total}")
    elif user_total <= 21 and user_total < cpu_total and cpu_total <= 21:
        print(f"Your cards: {user_deck} and CPU cards: {cpu_deck}. You loose, the sum of your cards were: {user_total} and the CPU sum was: {cpu_total}")
    elif user_total <= 21 and user_total == cpu_total and cpu_total <= 21:
        print(f"DRAW! Your cards: {user_deck} and CPU cards: {cpu_deck}. The sum of your cards were: {user_total} and the CPU sum was: {cpu_total}")
    elif user_total <= 21 and cpu_total > 21:
        print(f"Your cards: {user_deck} and CPU cards: {cpu_deck}. You win, the sum of your cards were: {user_total} and the CPU sum was over 21: {cpu_total}")
    else:
        print("ERROR")
