# GUI (Exercise)

# Display the image below where the 0 is going to be ' ', 
# and the 1 is going to be '*'. This will reveal an image!
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

# So, what is the plan,
# We have to iterate over picture.
# if 0 --> ' '
# if 1 --> *

for row in picture:
    for pixel in row:
        if (pixel == 1):
            print('*', end='') # This end='' prevents our loop from going to new line 
        else:                  # after every 0 and 1.
            print(" ", end='')
    print('') # Remember, this print will simply give a new line. 

# To print without a new line in Python 3 add an extra argument to your print function
# telling the program that you don't want your next string to be on a new line.
# Here's an example: print("Hello there!", end = '')
# The next print function will be on the same line.

name = 'wasif'
for _ in name:
    print(_, end=',') # Just an example (IMPORTANT concept)