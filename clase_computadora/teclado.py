from clase_computadora.dispositivo_entrada import DispositivoEntrada


class Teclado(DispositivoEntrada):
    contador_teclados = 0 #atributo de clase

    def __init__(self, marca, tipo_entrada):
        Teclado.contador_teclados += 1
        self.id = Teclado.contador_teclados #variable creada en esta clase
        super().__init__(marca, tipo_entrada) #inicializa con los atributos de la clase padre
                                              #Dispositivo_entrada

    def __str__(self):
        return f'''\t\tID: {self.id} 
        Marca: {self.marca}
        Tipo entrada: {self.tipo_entrada}'''

#codigo de prueba
teclado1 = Teclado('juanwei', 'Inalambrico')
print(teclado1)
