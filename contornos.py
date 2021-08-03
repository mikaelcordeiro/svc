import cv2 as cv
import numpy as np

imagem = cv.imread(filename='/home/mikael/scripts/python/svc/fotos/ferramentas.jpg')

imagem_gray = cv.cvtColor(src=imagem, code=cv.COLOR_BGR2GRAY)  # diminui levemente o ruido

cv.imshow(winname='ferramentas gray', mat=imagem_gray)

'''============================================ blur =================================================='''

imagem_blur = cv.GaussianBlur(src=imagem_gray, ksize=(3, 3), sigmaX=cv.BORDER_DEFAULT)

'''============================================ canny Cascade =================================================='''

contorno_canny_gray = cv.Canny(image=imagem_blur, 
                                threshold1=5, 
                                threshold2=255,
                                apertureSize=3,
                                L2gradient=True)

cv.imshow(winname='contorno canny cascade gray', mat=contorno_canny_gray)

'''============================================ func threshold =================================================='''

ret, thresh = cv.threshold()


'''============================================ func findContours =================================================='''

contornos, hierarquia = cv.findContours(image=contorno_canny_gray,
                                        mode=cv.RETR_EXTERNAL,
                                        method=cv.CHAIN_APPROX_SIMPLE)

# instancias:
#   contornos -> python list com todas as coordenadas dos contornos encontrados
#   hierarquia -> numpy array (1, contornos, ??) representacao hierarquica dos contornos

# parametros:
#   image -> matriz que se deseja os contornos
#   mode -> como os contornos sao encontrados
#       cv.RETR_LIST: retorna TODOS contornos encontrados na imagem
#       cv.RETR_EXTERNAL: retorna os contornos mais externos
#   method -> metodo de aproximacao dos contornos
#       cv.CHAIN_APPROX_NONE: retorna todos os contornos
#       cv.CHAIN_APPROX_SIMPLE: comprime contornos em 1, de maneira que faca sentido

print(hierarquia.shape)

cv.waitKey(0)
