
name = 'Travis'
length = len(name)
if length < 3:
    print("Name must be at least 3 characters.")
elif length > 50:
    print("Name cannot be longer than 50 characters.")
else:
    print("Name looks good!")