from clase_computadora.monitor import Monitor
from clase_computadora.raton import Raton
from clase_computadora.teclado import Teclado


class Computadora:
    contador_computadoras = 0
    def __init__(self, nombre,monitor,teclado,raton):
        Computadora.contador_computadoras += 1
        self.id_computadora = Computadora.contador_computadoras
        self.nombre = nombre
        self.monitor = monitor
        self.teclado = teclado
        self.raton = raton


    def __str__(self):
        return f'''
Id: {self.id_computadora}
Nombre: {self.nombre}
Monitor: {self.monitor}
Teclado: {self.teclado}
Raton: {self.raton}'''

if __name__ == '__main__':
    monitor = Monitor('Asus', '21 pulgadas')
    teclado = Teclado('Eagle', 'USB C')
    raton = Raton('Cougar', 'USB C')
    computadora1 = Computadora('Kaiju', monitor, teclado, raton)
    print(computadora1)
