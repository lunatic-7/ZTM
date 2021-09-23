from random import randint

# Generate a no. 1 to 10
answer = randint(1, 10)
# Take input from user!

# Check that if input is a no. b/w 1 to 10
while True:
    try:
        # print(answer) # Uncomment for cheating.
        guess = int(input("Guess a no. b/w 1 to 10:  "))
        if 0 < guess < 11:

            # Check if no. is right guess otherwise ask again.
            if guess == answer:
                print("You are Genius!")
                break
            else:
                print("you lost!")
        else:
            print("Hey dumbo! I said 1 to 10!")
    except ValueError:
        print("Please enter a number!")
