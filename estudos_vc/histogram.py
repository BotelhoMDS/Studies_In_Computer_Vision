import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

''' Trabalho com imagens cinzas'''
img = cv.imread(r'C:\Users\mathe\Programas\estudos_vc\imagens\Cinza.jpg')
#plt.imshow(img)
#plt.show()

#plt.hist(img.ravel(), 256, [0, 256]) # ravel() transforma a matriz em um vetor, 256 é o número de bins e [0, 256] é o intervalo.
#plt.show()

color_img = cv.imread(r'C:\Users\mathe\Programas\estudos_vc\imagens\colorida.jpg')
plt.imshow(color_img)
blue, green, red = cv.split(color_img)
#plt.show()
fig = plt.figure(figsize=(20,5))

ax1 = fig.add_subplot(131) # This method create a subplot, the first digit is the number of rows, 
# the second is the number of columns and the third is the index of the subplot.
ax1.hist(blue.ravel(), 256, [0, 256]) 
plt.title("Blue histogram channel")

ax2 = fig.add_subplot(132)
ax2.hist(green.ravel(), 256, [0, 256])
plt.title("Green histogram channel")

ax3 = fig.add_subplot(133) 
ax3.hist(red.ravel(), 256, [0, 256])
plt.title("Red histogram channel")

plt.show()


