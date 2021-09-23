from random import randint
import sys  # We are importing this to make sure we can run this in terminal as well, and we can
# customize game's difficulty according to us.

# Generate two numbers
answer = randint(int(sys.argv[1]), int(sys.argv[2]))
# Take input from user!

# Check that if input is a no. b/w those numbers
while True:
    try:
        # print(answer) # uncomment this for cheating.
        guess = int(input(f"Guess a no. b/w {sys.argv[1]} to {sys.argv[2]}:  "))
        if int(sys.argv[1]) <= guess <= int(sys.argv[2]):

            # Check if no. is right guess otherwise ask again.
            if guess == answer:
                print("You are Genius!")
                break
            else:
                print("you lost!")
        else:
            print(f"Hey dumbo! I said {sys.argv[1]} to {sys.argv[2]}!")
    except ValueError:
        print("Please enter a number!")
