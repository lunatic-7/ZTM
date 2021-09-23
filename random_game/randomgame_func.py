from random import randint


def run_guess(guess, answer):
    if 0 < guess < 11:
        # Check if no. is right guess otherwise ask again.
        if guess == answer:
            print("You are Genius!")
            return True
        else:
            print("you lost!")
    else:
        print("Hey dumbo! I said 1 to 10!")

# Generate a no. 1 to 10


if __name__ == '__main__':
    answer = randint(1, 10)

    # Take input from user!
    # Check that if input is a no. b/w 1 to 10
    while True:
        try:
            # print(answer) # Uncomment for cheating.
            guess = int(input("Guess a  b/w 1 to 10:  "))
            if run_guess(guess, answer):
                break
        except ValueError:
            print("Please enter a number!")
