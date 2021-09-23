# What is image processing?

# Image processing is cropping, compressing, adding filters etc. with an image, to
# make it suitable for our use. eg. When we upload an image on instagram. We upload an
# image of few (2-3 mb)s but, instagram processes it crops it compresses it, to
# make it in a few kilobytes (kbs). It does so to save money and to not to put
# a lot of load on the server.

# I have installed a library called Pillow. which will be used in this file further,
# for image processing.

from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')

filtered_img = img.filter(ImageFilter.BLUR)  # We can have, SMOOTH, SHARPEN and a lot more with ImageFilter.
filtered_img2 = img.convert('L')  # This 'L' method is to make image grey.
right_angled = filtered_img.rotate(90)  # .rotate to rotate img, 90 means, rotate to 90deg here.
small = img.resize((300, 300))  # To resize img, to 300, 300. remember resize accepts a tuple.
box = (100, 100, 400, 400)
region = img.crop(box)  # To get a cropped img, of given size in the box variable.

filtered_img.save('blur_pikachu.png', 'png')  # The reason I have converted this img, to png format bc,
# ImageFilter supports png, you might get an error if you try to leave it in jpeg.
right_angled.save('right_blurred_pikachu.png', 'png')
filtered_img2.save('grey_pikachu.png', 'png')  # .save is used to save images.
small.save('resized_pikachu.png', 'png')
region.save('cropped_pikachu.png', 'png')

print(img)  # This will simply give the info, of img, like format, size etc.
print(img.format)  # It will give format of image, which is JPEG here,
print(img.size)   # It will give (640, 640) which is img's size here.
print(img.mode)  # It will tell it's coloring, which is in RGB here.

# filtered_img.show()  # .show will simply open up the img, and show us.

astro = Image.open('astro.jpg')

print(astro.size)  # So, we can see that this img is of massive size. So, let's resize it.

resized_image = astro.resize((400, 200))  # We can notice here that the image is resized but it lost it's aspect ratio,
resized_image.save('resized_astro.jpg')  # and looks squished (chipki hui), which is bad, so to maintain it's
# aspect ratio, we are gonna use thumbnail method instead of resize.

# thumbnail = astro.thumbnail((400, 200))  # will give an error, bc thumbnail method changes image in place.
# thumbnail.save('thumbnail_astro.jpg')

astro.thumbnail((400, 200))  # This maintains its aspect ratio as well, remember, thumbnail, might not give exact
astro.save('thumbnail_astro.jpg')  # size you told, but it will try it's best to be close to the size given.
