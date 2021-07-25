import cv2 as cv
import numpy as np

'''============================================ imagem =================================================='''

# img é uma instancioa de cv.imshow()

img = cv.imread('fotos/pessoas1.jpg')

# aqui, temos a largura de "img"

largura = img.shape[1]

# aqui, temos a altura de "img"

altura = img.shape[0]

# abre uma janela chamada "Cat" armazenada na instancia "img"

cv.imshow('pessoas', img)

'''============================================ imagem reescalado =================================================='''

# podemos mudar a escala de uma imagem/frame

escala = .25

# devem ser valores inteiros

dimensoes = int(largura*escala), int(altura*escala)

# a imagem reescalada deve ser colocada num atributo
# Funciona para videos, imagens e live videos

img_resized = cv.resize(src=img, dsize=dimensoes, interpolation=cv.INTER_AREA)

cv.imshow('pessoas menores', img_resized)

'''============================================ dummy image preenhida =================================================='''

pixels_x, pixels_y, color_channels = 500, 500, 3

matriz = np.zeros(shape=(pixels_x, pixels_y, color_channels), dtype='uint8')

b, g, r = 255, 0, 0

cor = b, g, r

area_matriz = matriz.copy()

pixels_x_inicial, pixels_x_final = 300, 400

pixels_y_inicial, pixels_y_final = 300, 400

area_matriz[pixels_y_inicial:pixels_y_final, pixels_x_inicial:pixels_x_final] = cor

cv.imshow('dumy img',area_matriz)

'''============================================ retangulo =================================================='''

ponto_1 = (0, 0)

ponto_2 = (250, 250)

cv.rectangle(img=matriz, pt1=ponto_1, pt2=ponto_2, color=cor, thickness=1)

cv.imshow('retangulo', matriz)

'''============================================ dummy image preenhida 2 =================================================='''

area_matriz_2 = matriz.copy()

cv.rectangle(img=area_matriz_2, pt1=ponto_1, pt2=ponto_2, color=cor, thickness=cv.FILLED)

cv.imshow('area preenchida facil', area_matriz_2)

cv.rectangle(img=area_matriz_2, pt1=ponto_1, pt2=(area_matriz_2.shape[1] // 2, area_matriz_2.shape[0] // 2), color=cor, thickness=-1)

cv.imshow('area preenchida facil 2', area_matriz_2)

# fecha a janela "Cat" caso aperte qualquer botao do teclado

cv.waitKey(0)
