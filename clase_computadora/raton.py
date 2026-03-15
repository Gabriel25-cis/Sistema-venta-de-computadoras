from clase_computadora.dispositivo_entrada import DispositivoEntrada


class Raton(DispositivoEntrada):
    contador_ratones = 0

    def __init__(self, marca, tipo_entrada):
        Raton.contador_ratones += 1
        self.id = Raton.contador_ratones
        #self.marca = marca
        #self.tipo_entrada = tipo_entrada
        super().__init__(marca, tipo_entrada)

    def __str__(self):
        return f'''\t\tID: {self.id} 
        Marca: {self.marca}
        Tipo entrada: {self.tipo_entrada}'''
    #mandamos llamar los atributos ya definidos en la clase padre

'''dispositivo1=DispositivoEntrada('Lenovo', 'USB C')'''
#Incorrecto, no genera error. Pero inicializamos desde el objeto raton, ya que este manda
#llamar el inicializador de dispositivo entrada y por lo tanto le pasa los atributos
if __name__ == '__main__':
    raton1= Raton('lenovo', 'USB C')
    print(raton1)
