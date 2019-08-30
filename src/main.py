from flag import Flag
import forms as formas

santa_lucia = Flag(1200, 675, (255, 210, 0))
santa_lucia.drawTriangle([(600, 10), (915, 665), (285, 665)], (255, 255, 255))
# santa_lucia.fillPolygon(ponto_interno, (255, 255, 255)) >> EXEMPLO PRA PREENCHER
santa_lucia.drawTriangle([(600, 100), (865, 665), (335, 665)], (0, 0, 0))
# santa_lucia.fillPolygon(ponto_interno, (0, 0, 0))
santa_lucia.drawTriangle([(600, 337), (915, 665), (285, 665)], (0, 210, 255))
# santa_lucia.fillPolygon(ponto_interno, (0, 210, 255))
santa_lucia.showFlag()