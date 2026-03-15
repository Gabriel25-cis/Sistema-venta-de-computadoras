from clase_computadora.monitor import Monitor
from clase_computadora.raton import Raton
from clase_computadora.teclado import Teclado


class Computadora:
    contador_computadoras = 0
    def __init__(self, nombre):

        self.nombre = nombre
        monitor = Monitor('Asus', '21 pulgadas')
        teclado = Teclado('Eagle', 'USB C')
        raton = Raton('Cougar', 'USB C')
        self.monitor = monitor.marca
        self.teclado = teclado.marca
        self.raton = raton.marca


    def __str__(self):
        return f'''
Nombre: {self.nombre}
Monitor: {self.monitor}
Teclado: {self.teclado}
Raton: {self.raton}'''

if __name__ == '__main__':
    computadora1 = Computadora('Kaiju')
    print(computadora1)
