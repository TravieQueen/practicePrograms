
engine = False
moving = False
nonsenseCount = 0

while True:
    print(f"Engine = {engine}\nMoving = {moving}\n")
    UserInput = input("> ").lower()

    if UserInput == 'help':
        print("start - to start the car\nstop - to stop the car"
              "\nquit - to exit\ndrive - to move forward\n"
              "break  - to stop the car\n")
    elif UserInput == 'start':
        if not engine:
            print("You turn the engine on.")
            engine = True
        else: print("The engine is already on...")
    elif UserInput == 'stop':
        if not engine: print("The engine is already stopped...")
        elif moving: print("You must use the breaks first.")
        else:
            print("You turn off the engine")
            engine = False
    elif UserInput == 'drive':
        if moving: print("You are already moving...")
        elif not engine: print("You must turn on the engine first.")
        else:
            print("You are now moving forwards.")
            moving = True
    elif UserInput == 'break':
        if not moving: print("You are already stopped.")
        else:
            print("You stop the car.")
            moving = False
    elif UserInput == 'quit':
        break
    else:
        nonsenseCount += 1
        print(f"Not a valid command. \n+{nonsenseCount} nonsense.")
else:
    print("Thank you for playing!")