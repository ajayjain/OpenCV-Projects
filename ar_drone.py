from __future__ import print_function
from SimpleCV import Image, Color

im = Image("img/ardrone.jpg")
# im = im.erode()
im = im.crop(2000, 1500, 2000, 2000, centered=True)
# im = im.erode()
# blobs = im.findBlobs()
# blobs.draw()

only_orange = im - im.colorDistance(Color.ORANGE)
only_black 	= im - im.colorDistance(Color.BLACK)
only_drone  = only_orange + only_black


body.save("img/ardrone2.jpg")
# raw_input("Hit enter to quit: ")
# window.quit()