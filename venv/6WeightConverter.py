
measurement = input("(L)bs or (K)g: ").lower()
weight = int(input("Please enter your weight: "))

if measurement == 'k':
    converted = weight*2.20462
    print(f"Your weight in lbs is: {converted}")
if measurement == 'l':
    converted = weight*0.453591830542594
    print(f"Your weight in kilograms is: {converted}")