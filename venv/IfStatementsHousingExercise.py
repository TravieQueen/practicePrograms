
price = 1000000
goodCredit = True
downpayment = .2
if goodCredit:
    print("You have good credit.")
    downpayment = .1*price
elif not goodCredit:
    print("You have bad credit.")
    downpayment = .2*price
print(f"Your price: ${downpayment}")