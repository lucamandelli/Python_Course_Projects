def tip_calculator():
    print("Welcome to the bill calculator.")
    bill_value = input("What was the total bill? $")
    num_persons = input("How many people to split the bill? ")
    tip_percentage = input("What tip percentage would you like to give? 10, 12 or 15? ")
    print(f"Each person should pay: ${operator(bill_value,tip_percentage,num_persons)}")
    

def operator(bill, tip, person):
    result = ((float(bill) * ((float(tip) / 100) + 1)) / int(person))
    return round(result, 2)

tip_calculator()
