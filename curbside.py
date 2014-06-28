#!/usr/bin/env python

# /media/ajay/5056EE7956EE5EEA/Users/Ajay/Desktop/gopro/DCIM/100GOPRO/repaired

from __future__ import print_function
from SimpleCV import Image, Color, VirtualCamera, Display
import SimpleCV as scv

# # video = VirtualCamera('', 'video')
# display = Display()

# while display.isNotDone():
# 	img = video.getImage()
# 	try:
# 		dist = img - img.colorDistance(Color.RED)
# 		dist.show()
# 	except KeyboardInterrupt:
# 		display.done = True
# 	if display.mouseRight:
# 		display.done = True
# display.quit()

img = Image('img/curb.JPG')
img = img.crop(0, 2*img.height/3, img.width, 5*img.height/6)
print(img.meanColor())
# img = img.binarize()
# img.findBlobs().draw()
# ls = img.findLines()
# for l in ls:
	# l.draw()
# img.findBlobs().draw()
# img = img.colorDistance(Color.RED)

img.save('img/curb_processed.jpg')