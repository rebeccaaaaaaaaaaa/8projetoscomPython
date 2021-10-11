# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

import math

class Programa:
    def __init__(self):
        self.raio = float(input('Entre com o valor do raio, para obter a área: '))
        
    
    def CalcularArea(self):
        self.area = round((math.pi * self.raio**2),2)
        print("A área do círculo: {:.2f}".format(self.area))
        

mostrarResultado = Programa()
mostrarResultado.CalcularArea()