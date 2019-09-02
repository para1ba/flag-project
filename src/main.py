import numpy as np
from flag import Flag
import forms as formas
import matriz as matriz

santa_lucia = Flag(1200, 675, (255, 210, 0))

santa_lucia.drawTriangle([(600, 10), (915, 665), (285, 665)], (255, 255, 255))
#PREENCHIMENTO
santa_lucia.fillPolygon((380,511), (255, 255, 255)) 

santa_lucia.drawTriangle([(600, 100), (865, 665), (335, 665)], (0, 0, 0))
#PREENCHIMENTO
santa_lucia.fillPolygon((650,250), (0, 0, 0)) 

santa_lucia.drawTriangle([(600, 337), (915, 665), (285, 665)], (0, 210, 255))
#PREENCHIMENTO
santa_lucia.fillPolygon((650, 500), (0, 210, 255)) 
santa_lucia.fillPolygon((325, 645), (0, 210, 255))
santa_lucia.fillPolygon((875, 645), (0, 210, 255))

santa_lucia.scale(1, 2)
santa_lucia.translation(20, 20)

santa_lucia.rotate(15)

santa_lucia.showFlag()