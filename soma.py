# Faça um Programa que peça dois números e imprima a soma.

class Soma:
    def __init__(self):
        self.valor_1 = int(input('Digite um numero para somar'))
        self.valor_2 = int(input('Digite um outro numero para somar'))
    
    def Somar(self):
        resultado = self.valor_1 + self.valor_2
        print(resultado)
        
resultado = Soma()
resultado.Somar()