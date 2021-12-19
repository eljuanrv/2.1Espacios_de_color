# Juan Rivera Vargas

#Notas importantes del codigo
#1No pongan palabras reservadas
#en el nombre del archivo
#2No poner cosas como acentos o enies
#3Python no usa llaves, en su lugar
#se usan identaciones de 4 espacios
#4En TODO un archivo solo usar o
#tabulaciones o 4 espacios
#5Las fotos deben estar en la misma
#carpeta que el codigo

import cv2
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

#Cargar la imagen con openCV
imgBGR = cv2.imread('Satya.jpg')
#Cambiar esacio de color BGR a RGB
imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)
#BGR A HSV
imgHSV = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2HSV)
#BGR A CMYK
imgCMYK=Image.open('Satya.jpg')
imgCMYK=imgCMYK.convert('CMYK')
imgCMYK.save('Satya.tif')

#mostrar las imagenes
titles = ['BGR','RGB','HSV', 'CMYK']
images = [imgBGR, imgRGB, imgHSV, imgCMYK]
miArray = np.arange(4)
for i in miArray:
	plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
	plt.title(titles[i])
	plt.xticks([]),plt.yticks([])
 
plt.show()
