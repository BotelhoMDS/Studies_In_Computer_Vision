import cv2 as cv 
import numpy as np
import matplotlib.pyplot as plt


img = cv.imread(r'C:\Users\mathe\Programas\estudos_vc\imagens\einstein.jpg', 0) #read the image in grayscale

rows, colums = img.shape #get the number of rows and columns of the image

mat_rot = cv.getRotationMatrix2D((colums/2, rows/2),45 , 1) #get the rotation matrix, the first parameter is the center of the image, the second is the angle and the third is the scale

#the warpAffine function is used to apply a matrix transformation to an image, in this case, a rotation
img_rotated = cv.warpAffine(img,mat_rot,(colums,rows)) #first parameter is the image, the second is the rotation matrix (Mask) and the third is the size of the image

fig = plt.figure(figsize=(20,5)) 
plt.imshow(img_rotated, cmap=plt.cm.gray)
#plt.show()

#now we create a matrix for make translations, move the image in the x and y axis
mat_trans = np.float32([[1,0,100],[0,1,100]]) #get the translation matrix, the first parameter is the x axis translation, the second is the y axis translation and the third is the z axis translation

img_translated = cv.warpAffine(img,mat_trans,(colums,rows)) #first parameter is the image, the second is the translation matrix (Mask) and the third is the size of the image
plt.imshow(img_translated, cmap=plt.cm.gray)
plt.show()


#Nnow we go resize the image 

img_resized = cv.resize(img,None,fx=0.5, fy=0.5, interpolation = cv.INTER_CUBIC) #first parameter is the image, the second is the image out, the third is the x axis scale, the fourth is the y axis scale and the fifth is the interpolation method

cv.imshow('Original image of Einstein',img)
cv.imshow('Resized image of Einstein',img_resized)
cv.waitKey(0)
cv.destroyAllWindows()