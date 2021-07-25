import cv2 as cv

# img é uma instancioa de cv.imshow()

img = cv.imread('fotos/pessoas1.jpg')

# aqui, temos a largura de "img"

largura = img.shape[1]

# aqui, temos a altura de "img"

altura = img.shape[0]

# abre uma janela chamada "Cat" armazenada na instancia "img"

cv.imshow('pessoas', img)

# podemos mudar a escala de uma imagem/frame

escala = .25

# devem ser valores inteiros

dimensoes = int(largura*escala), int(altura*escala)

img_resized = cv.resize(src=img, dsize=dimensoes, interpolation=cv.INTER_AREA)

cv.imshow('pessoas menores', img_resized)

# fecha a janela "Cat" caso aperte qualquer botao do teclado

cv.waitKey(0)
