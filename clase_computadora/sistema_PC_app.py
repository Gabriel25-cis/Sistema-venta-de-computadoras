from clase_computadora.Computadora import Computadora
from clase_computadora.Orden_compra import Orden
from clase_computadora.monitor import Monitor
from clase_computadora.raton import Raton
from clase_computadora.teclado import Teclado

print('*** Sistema de Computadoras ***')

teclado1 = Teclado('juanwei', 'Inalambrico')
teclado2 = Teclado('Cougar', 'USB')

raton1 = Raton('lenovo', 'USB C')
raton2 = Raton('xbox', 'Bluetooth')

monitor1 = Monitor('Asus', '21 pulgadas')
monitor2 = Monitor('Samsung', '17 pulgadas')

computadora1 = Computadora('Kaiju', monitor1, teclado1, raton1)
computadora2 = Computadora('Ranger', monitor2, teclado2, raton2)


orden1 = Orden()
orden1.agregar_computadora(computadora1)
orden1.agregar_computadora(computadora2)
print(orden1)





