import os
from logo import print_logo

def silent_auction():
    kepp_bid = False
    bids = {}
    while not kepp_bid:
        print_logo()
        name = input("Type your name: ")
        price = int(input("What's your bid? $"))
        bids[name] = price    
        question_users = input("There is someone else to bid? Type 'yes' or 'no'. ").lower()
        if question_users == "no":
            os.system('cls')
            print_logo()
            kepp_bid = True
            highest_bidder(bids)
        elif question_users == "yes":
            os.system('cls')

def highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")
    
silent_auction()
