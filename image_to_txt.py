import pdb
from PIL import Image
from pylab import *
from scipy.ndimage import filters
from numpy import *
from matplotlib.font_manager import FontProperties

im= array(Image.open('C:\\Users\\ZCWEIJJI\\Pictures\\photo.jpg').convert('L'))
im=(100.0/255)*im+100 #将高灰阶部分压低后可获得与Halcon的sobel一样的效果
imx=zeros(im.shape)
filters.sobel(im,1,imx)
imy=zeros(im.shape)
filters.sobel(im,0,imy)
magnitude=sqrt(imx**2+imy**2)
axis_x=magnitude.shape[1]
print(axis_x)
axis_y=magnitude.shape[0]
print(axis_y)
f = open('C:\\Users\\ZCWEIJJI\\Documents\\python\\image.txt','w')
for i in range(axis_y):
    for j in range(axis_x):
        if magnitude[i][j]>=50:
            f.write("O ")
        else:
            f.write("M ")
    f.write("\n")
f.close()

