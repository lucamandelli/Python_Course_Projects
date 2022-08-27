import random

def pypassword_gen():
    print("Welcome to PyPassword Generator!!")
    print("Let's create a safer password for you")

    letters = int(input("How many letters would you like to have in your password? "))
    symbols = int(input("How many symbols would you like? "))
    numbers = int(input("How many numbers would you like? "))

    num_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    sym_list = ["!", "@", "#", "$", "%", "&", "*"]
    lett_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
               'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
               'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
               'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    password_list = []
    
    for i in range(1, letters + 1):
        password_list.append(random.choice(lett_list))
    
    for i in range(1, symbols + 1):
        password_list.append(random.choice(sym_list))
    
    for i in range(1, numbers + 1):
        password_list.append(random.choice(num_list))
    
    random.shuffle(password_list)
    
    password = ""
    for char in password_list:
        password += char
    
    print(f"The generated password is: {password}")

pypassword_gen()
