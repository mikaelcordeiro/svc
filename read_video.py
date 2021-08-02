import cv2 as cv

# se passada um path, le o arquivo
# se passado um inteiro 0, 1, 2 etc, le uma webcam
#video é uma instancia de cv.VideoCapture()

video = cv.VideoCapture('/home/mikael/scripts/python/svc/videos/carros1.mp4')

while True:

    '''============================================= video normal ====================================================='''

    # aqui dentro do loop, lemos a instancia "video" frame por frame com o video.read()
    # video.read() tem duas instancias: leu_certo e frame
    #   leu_certo: booleano que retorna se o frame foi lido certo ou errado
    #   frame: o frame da instancia "video" 

    leu_certo, frame = video.read()

    # cv.imshow('nome da janela', frame) mostra numa janela chamada "video" cada frame lido de "video" no loop

    cv.imshow('video', frame)

    '''============================================ video reescalado =================================================='''

    # aqui, temos a largura de "img"
    
    largura = frame.shape[1]

    # aqui, temos a altura de "img"

    altura = frame.shape[0]

    # podemos mudar a escala de uma imagem/frame

    escala = .75

    # devem ser valores inteiros

    dimensoes = int(largura*escala), int(altura*escala)

    # o video reescalado deve ser colocado num atributo, e esse atributo sera o frame reescalado
    # Funciona para videos, imagens e live videos

    frame_resized = cv.resize(src=frame, dsize=dimensoes, interpolation=cv.INTER_AREA)

    cv.imshow('video menor', frame_resized)

    # essa linha serve para parar o loop dentro da janela "video". Deve ter uma maneira mais fácil de se fazer

    if cv.waitKey(20) & 0xFF==ord('d'):

        break

# quebramos a instancia "video" de cv.VIdeoCapture()

video.release()

# aqui fechamos todas as janelas

cv.destroyAllWindows()

# caso o video nao seja pausado apertando a letra "d", o opencv vai rodar todo ele ate acabarem os frames
# só que, quando isso acontece, aparece um erro:
#   (-215:Assertion failed) size.width>0 && size.height>0 in function 'imshow'
#   ele aparece quando nao encontra o path do video, ou quando os frames do video acaba
