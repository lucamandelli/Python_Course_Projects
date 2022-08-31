import os


def add(n1, n2):
    return n1 + n2

def subtract(n1 ,n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

stop_operation = False
next_operation = True
while not stop_operation:
    num1 = float(input("What's the first number? "))
    for key in operations:
        print(key)
    operation_symbol = input("Pick an operation from the line above: ")
    num2 = float(input("What's the second number? "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    keep_calculating = input("Do you want to make another operation? type 'y' or 'n': ")    
    if keep_calculating == "n":
        stop_operation = True
    elif keep_calculating == "y":
        os.system('cls')
        while next_operation:
            same_calculation = input(f"Do you want to make another operation with the {answer}? type 'y' or 'n': ")
            if same_calculation == "y":
                for key in operations:
                    print(key)
                operation_symbol = input("Pick an operation from the line above: ")
                next_number = float(input("Pick another number: "))
                last_calculation = answer
                answer = 0
                calculation_function = operations[operation_symbol]
                answer = calculation_function(last_calculation, next_number)
                print(f"{last_calculation} {operation_symbol} {next_number} = {answer}")
                keep_calculating = input("Do you want to make another operation? type 'y' or 'n': ")
                if keep_calculating == "n":
                    next_operation = False
                    leave_program = input("Do you want to leave the program? type 'y' or 'n': ")
                    if leave_program == "y":
                        stop_operation = True
                    else:
                        os.system('cls')
                if keep_calculating == "y":
                    os.system('cls')
        next_operation = True
    else:
        print("Please type 'y' or 'n': ")
