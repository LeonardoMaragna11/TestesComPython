from turtle import *


cor = '#fff'
fundo = '#000'
musica = False
desenho="";


def desenho(cor, musica):
    if(musica == True):
    speed(100)
    color(cor)
    bgcolor(fundo)
    b = 190
    while b > 0:
        left(b)
        forward(b * 3)
        b = b - 1
    else:
        speed(100)
        color(cor)
        bgcolor(fundo)
        b = 190
    while b > 0:
        left(b)
        forward(b * 3)
        b = b - 1


desenho('#000', False)
desenho('#0ff', True)
