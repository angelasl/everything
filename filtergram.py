# This is where we'll call our class library
#and ask for files to filter!

from filter import *

filename= "sky.jpg"
filename2= "sky_filter.jpg"

original= load_img(filename)

newImg = angela(original)
save_img(newImg, filename2)
show_img(newImg)
