
GuessCount = 3
SecretNumber = 7

print("Guess the secret number between 1 and 10: ")
while GuessCount > 0:
    UserGuess = int(input("Guess: "))
    GuessCount -= 1

    if UserGuess == SecretNumber:
        print("You win!")
        break
    else:
        print("Try again!\n")
else:
    print("\nSorry you lost!")


print("\nThank you for playing!")