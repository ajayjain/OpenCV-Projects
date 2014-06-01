from __future__ import print_function
import requests
from StringIO import StringIO
from PIL import Image
import cv2
import numpy as np

def image_url(app_id):
	url = "http://itunes.apple.com/us/lookup?id={}".format(app_id)
	request = requests.get(url)
	return request.json()["results"][0]["artworkUrl60"]

def load_image(url):
	raw = StringIO(requests.get(url).content)
	raw.seek(0)
	source = Image.open(raw).convert("RGB")
	npimg = np.fromstring(source.tostring(), dtype=np.uint8)
	npimg = cv2.cvtColor(npimg, cv2.cv.CV_RGB2BGR)
	return npimg

def show_image(im, window_name):
	cv2.namedWindow(window_name)
	cv2.imshow(window_name, im)

def waitKey():
	cv2.waitKey(0)
	cv2.destroyAllWindows()

APP_ID = "598581396"
url = image_url(APP_ID)
im = load_image(url)
print(im)

show_image(im, "Original")
waitKey()