import cv2 as cv 
import numpy as np
import matplotlib.pyplot as plt

'''Equalizando histograma para torna-lo mais nitido e com mais contraste'''

img = cv.imread(r'estudos_vc\imagens\einstein.jpg', 0) # 0 para cinza, 1 para colorida, -1 para alpha channel

img_equalizada = cv.equalizeHist(img) #função para equalizar o histograma

fig = plt.figure(figsize=(20,5))
''''
ax1 = fig.add_subplot(121)
plt.imshow(img, cmap=plt.cm.gray)

ax2 = fig.add_subplot(122)
plt.imshow(img_equalizada, cmap=plt.cm.gray)

plt.show()

ax1 = fig.add_subplot(121)
plt.hist(img.ravel(), 256, [0, 256])

ax2 = fig.add_subplot(122)
plt.hist(img_equalizada.ravel(), 256, [0, 256])

plt.show()

'''
'''Desafio: equalizar o histograma de uma imagem colorida'''
img_color = cv.imread(r'C:\Users\mathe\Programas\estudos_vc\imagens\color_equalization.jpg',1)


blue,green,red = cv.split(img_color) #separando os canais de cores

green_equalizada = cv.equalizeHist(green)
red_equalizada = cv.equalizeHist(red)
blue_equalizada = cv.equalizeHist(blue)

img_color_equalizada = cv.merge((blue_equalizada, green_equalizada, red_equalizada)) #depois de processado, juntando os canais novamente para formar a imagem.

ax1 = fig.add_subplot(241)
plt.hist(blue_equalizada.ravel(), 256, [0, 256])

ax2 = fig.add_subplot(242)
plt.hist(green_equalizada.ravel(), 256, [0, 256])

ax3 = fig.add_subplot(243)
plt.hist(red_equalizada.ravel(), 256, [0, 256])

ax4 = fig.add_subplot(244)
plt.imshow(img_color_equalizada)

ax5 = fig.add_subplot(245)
plt.hist(blue.ravel(), 256, [0, 256])

ax6 = fig.add_subplot(246)
plt.hist(green.ravel(), 256, [0, 256])

ax7 = fig.add_subplot(247)
plt.hist(red.ravel(), 256, [0, 256])

ax3 = fig.add_subplot(248)
plt.imshow(img_color)

plt.show()



