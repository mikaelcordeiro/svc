import cv2 as cv
import numpy as np

imagem = cv.imread(filename='/home/mikael/scripts/python/svc/fotos/pessoas2.jpg')

largura = imagem.shape[1]

altura = imagem.shape[0]

escala = .5

dimensao = (int(largura*escala), int(altura*escala))

imagem = cv.resize(src=imagem, dsize=dimensao, interpolation=cv.INTER_AREA)

cv.imshow(winname='Pessoas', mat=imagem)

'''============================================ escala de cinza =================================================='''

grayscale = cv.cvtColor(src=imagem, code=cv.COLOR_BGR2GRAY)

cv.imshow('Pessoas BW', grayscale)

'''============================================ blur =================================================='''

blur = cv.GaussianBlur(src=imagem, ksize=(7, 7), sigmaX=cv.BORDER_DEFAULT)

cv.imshow('Pessoas Blur', blur)

'''============================================ bordas "canny cascade" =================================================='''

bordas_canny = cv.Canny(image=imagem, threshold1=125, threshold2=175)

cv.imshow('Bordas com Canny Cascade', bordas_canny)

'''============================================ bordas de blur =================================================='''

bordas_blur = cv.Canny(image=blur, threshold1=125, threshold2=175)

cv.imshow('Bordas com Canny Cascade de uma imagem blur', bordas_blur)

'''============================================ bordas com Dileted =================================================='''

bordas_dilate = cv.dilate(src=bordas_blur, kernel=(7, 7), iterations=1)  # dá uma enhance nas bordas

cv.imshow('Bordas com Dilate', bordas_dilate)

'''============================================ bordas com Eroded =================================================='''

bordas_erode = cv.erode(src=bordas_blur, kernel=(7, 7), iterations=1)

cv.imshow('Bordas com Eroded', bordas_erode)

'''============================================ recortar imagem =================================================='''

pixel_y_inicial, pixel_y_final = 200, 400

pixel_x_inicial, pixel_x_final = 200, 400

cropped = imagem[pixel_y_inicial:pixel_y_final, pixel_x_inicial:pixel_x_final]

cv.imshow('imagem cortada', cropped)

'''============================================ translac imagem =================================================='''

x = 100  # positivo -> direita, negativo -> esquerda (em pixels)

y = 100  # positivo -> baixo, negativo -> cima (em pixels)

matriz_translac = np.float32([[1, 0, x], [0, 1, y]])

img_translac = cv.warpAffine(src=imagem, M=matriz_translac, dsize=(dimensao[1], dimensao[0]))

cv.imshow('imagem translacao', mat=img_translac)

'''============================================ rot imagem =================================================='''

ponto_rot = (dimensao[1]//2, dimensao[0]//2)  # centro da imagem sera o ponto de rot

angulo = 45  # positivo -> anti-clock, negativo -> clock (em graus)

matriz_rot = cv.getRotationMatrix2D(center=ponto_rot, angle=angulo, scale=1.)

img_rot = cv.warpAffine(src=imagem, M=matriz_rot, dsize=(dimensao[1], dimensao[0]))

cv.imshow('imagem rot', mat=img_rot)

matriz_rot_2 = cv.getRotationMatrix2D(center=ponto_rot, angle=-angulo, scale=1.)

img_rot_rot = cv.warpAffine(src=imagem, M=matriz_rot_2, dsize=(dimensao[1], dimensao[0]))

cv.imshow('imagem rotacionda da rotacao', mat=img_rot_rot)  # caso suma algum pedaco da imagem, e que foi perdido na 1 rotacao

'''============================================ flip imagem =================================================='''

codigo = -1 # 0 -> eixo "x", 1 -> eixo "y", -1 -> os dois 

img_flipped = cv.flip(src=imagem, flipCode=codigo)

cv.imshow('flip da imagem', mat=img_flipped)

cv.waitKey(0)
