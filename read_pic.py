import cv2 as cv
import numpy as np

'''============================================ imagem =================================================='''

# img é uma instancioa de cv.imshow()

img = cv.imread('/home/mikael/scripts/python/svc/fotos/pessoas1.jpg')

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

matriz = np.zeros(shape=(pixels_y, pixels_x, color_channels), dtype='uint8')

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

'''============================================ circulo =================================================='''

matriz_circulo = matriz.copy()

x, y = matriz_circulo.shape[1] // 2, matriz_circulo.shape[0] // 2

centro = (x, y)

raio = 40 # pixels

cv.circle(img=matriz_circulo, center=centro, radius=raio, color=cor, thickness=1)

cv.imshow('circulo', matriz_circulo)

'''============================================ linha =================================================='''

cv.line(img=matriz_circulo, pt1=(0, 0), pt2=(x, y), color=(255, 255, 255), thickness=2)

cv.imshow('linha', matriz_circulo)

'''============================================ texto =================================================='''

texto = 'hello world'

cv.putText(img=matriz_circulo, text=texto, org=(x, y - 100), fontFace=cv.FONT_HERSHEY_COMPLEX, fontScale=1., color=(0, 0, 255), thickness=1)

cv.imshow('Texto na tela', matriz_circulo)

# fecha a janela "Cat" caso aperte qualquer botao do teclado

cv.waitKey(0)
