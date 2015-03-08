#image manipulation with pillow
#3.4 is call pillow
#2.x = image

from PIL import Image

img = Image.open('images/swirl.jpg')

#(300,250)
print (img.size)

#PNG
print(img.format)

#open the image
img.show()
