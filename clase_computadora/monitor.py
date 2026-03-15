


class Monitor:
    contador_monitores = 0 #atributo de clase
    def __init__(self, marca,tamano):
        Monitor.contador_monitores += 1
        self.id = Monitor.contador_monitores
        self.marca = marca
        self.tamano = tamano

    def __str__(self):
        return f'ID {self.id}, Marca: {self.marca}, Tamano: {self.tamano}'

if __name__ == '__main__':
    monitor1 = Monitor('Asus', '21 pulgadas')
    print(monitor1)
