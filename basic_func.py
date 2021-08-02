import cv2 as cv

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

cv.waitKey(0)
