import numpy as np
from flag import Flag
import forms as formas
import matriz as matriz

'''
santa_lucia = Flag(1200, 675, (255, 210, 0))

santa_lucia.drawTriangle([(600, 10), (915, 665), (285, 665)], (255, 255, 255))

ponto_interno = np.array([[600, 10], [915, 665], [285, 665]], np.int32)
santa_lucia.fillPolygon([ponto_interno], (255, 255, 255)) #>> EXEMPLO PRA PREENCHER

santa_lucia.drawTriangle([(600, 100), (865, 665), (335, 665)], (0, 0, 0))

ponto_interno = np.array([[600, 10], [865, 665], [335, 665]], np.int32)
santa_lucia.fillPolygon([ponto_interno], (0, 0, 0)) #>> EXEMPLO PRA PREENCHER

santa_lucia.drawTriangle([(600, 337), (915, 665), (285, 665)], (0, 210, 255))

ponto_interno = np.array([[600, 337], [915, 665], [285, 665]], np.int32)
santa_lucia.fillPolygon([ponto_interno], (0, 210, 255)) #>> EXEMPLO PRA PREENCHER

#santa_lucia.escala(5, 5) #>> ESCALA DANDO ERRO - N SEI PQ
# santa_lucia.transl(30, 300)

santa_lucia.rotate(-15)

santa_lucia.showFlag()
'''
matriz.apply_transformation(10, 0, matriz.matriz_rotacao(360))