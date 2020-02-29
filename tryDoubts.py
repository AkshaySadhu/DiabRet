from  PIL import Image
import numpy as np
import cv2
imgpath = "1ae3c58759fb.png"
img = Image.open(imgpath)

im = np.array(img.getdata()).reshape((512,512,3))
print(im)
