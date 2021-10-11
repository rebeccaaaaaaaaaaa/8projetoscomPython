# Faça um Programa que converta metros para centímetros.

class Initial():
    def __init__(self):
        self.metro = float(input('Digite o valor de metros'))
        
    def Converter(self):
        self.centimetro = self.metro * 100
        print('O valor',self.metro,'corresponde a',self.centimetro)

mostrarResultado = Initial()
mostrarResultado.Converter()