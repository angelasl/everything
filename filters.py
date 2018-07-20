# Rename this file to be "filters.py"
# Add commands to import modules here.
# import PIL
from PIL import Image

img = Image.open('sky.jpg')
img.show()

whatImage = input("What image would you like?")
load_img(whatImage)
show_img(whatImage)

# Define your load_img() function here.
#       Parameters: The name of the file to be opened (string)
#       Returns: The image object with the opened file.
def load_img(anImage):
    Image.open(anImage)


# Define your show_img() function here.
#       Parameters: The image object to display.
#       Returns: nothing.
def show_img(theSameImage):
    theSameImage.show()

# Define your save_img() function here.
#       Parameters: The image object to save, the name to save the file as (string)
#       Returns: nothing.
def save_img():


# Define your obamicon() function here.
#       Parameters: The image object to apply the filter to.
#       Returns: A New Image object with the filter applied.
def obamicon(sky.jpg):
