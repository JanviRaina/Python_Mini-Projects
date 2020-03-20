import numpy as np
import imageio 
import scipy.ndimage
import cv2

# imread() - read an image from the specified uri
# https://stackoverflow.com/questions/12201577/how-can-i-convert-an-rgb-image-into-grayscale-in-python
def grayscale(rgb):
    # 0.2989 R + 0.5870 G + 0.1140 B
    # from PIL import Image
    # img = Image.open('image.png').convert('LA')
    # img.save('greyscale.png')
    return np.dot(rgb[...,:3],[0.289,0.587,0.114])

# this will convert into sketch by taking grayscale image and the blurred image as parameters
def dodge(front,back):
    result=front*255/(255-back)
    result[result>255]=255
    result[back==255]=255
    return result.astype('uint8')
    # uint8	Unsigned integer (0 to 255)
    # astype shows in that type
    # OPEN CV USED FOR reading,writing images,face recog etc

img='photo_1.jpg'
s=imageio.imread(img)
g=grayscale(s)
# inverting image
i=255-g
# for darkest image 0,0,0
# fo rwhite image 255,255,255
# On increasing sigma clarity increases but run time also

b=scipy.ndimage.filters.gaussian_filter(i,sigma=1000)
# sigma tells about the blurrednss
r=dodge(b,g)
cv2.imwrite('1.png',r)

