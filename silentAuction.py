import os

bidders = {}

bids = []
maxBid = 0

def get_key(value):
    for k, v in bidders.items():
        if value == v:
            return k
print("\n\n\n=================================================")
print("Welcome to the secret auction program.")

while True:
    biddersNames = input("What is your name?: ")
    biddersAmt = int(input("What's your bid?: $"))
    bidders[biddersNames] = biddersAmt

    otherBidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if otherBidders == "yes":
        os.system('clear')
        continue
    elif otherBidders == "no":
        for amt in bidders:
            bids.append(bidders[amt])
        maxBid = max(bids)
        winner = get_key(maxBid)
        print(f"The winner is  {winner} with a bid of {bidders[winner]}")
        break
