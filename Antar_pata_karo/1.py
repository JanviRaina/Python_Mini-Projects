from PIL import Image,ImageChops

img1=Image.open("img1.png")
img2=Image.open("img2.png")
diff=ImageChops.difference(img1,img2)

if diff.getbbox():
    diff.show()