# JPG to PNG converter  (Exercise)

import sys
import os  # It is used to check for a path.
from PIL import Image

# Grab first and second argument.
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# Check if new exists if not then create.
if not os.path.exists(output_folder):  # Like this we check if a folder already exists or not.
    os.makedirs(output_folder)  # .makedirs is used to make new directories.
# loop through Pokedex
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]  # This splitext is necessary here, to give proper names to images,
    # if not, it will come out like pikachu.jpg.png, So, split method splits the name like this ('pikachu', '.jpg')
    # and by [0], we take its first character only.

    # convert images to PNG
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print('all done')
