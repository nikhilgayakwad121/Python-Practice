

from turtle import clear


bids={}
bidding_finished = False
winner = ""
def find_highest_bidders(bidding_record):
    highest_bid = 0
    # bidding_record = {"Angela": 123, "James":321}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winnner is ${winner} with a bid of ${highest_bid}")


while not bidding_finished:
    name = input("What is your name?")
    price = int(input("What is your bid?$"))
    bids[name] = price
    should_continue=input("Are there any others biddders? Type 'yes or 'no' .")
    if should_continue == "no":
        bidding_finished =True
        find_highest_bidders(bids)
    elif should_continue=="yes":
        clear()
