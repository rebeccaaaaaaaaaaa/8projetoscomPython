# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

class AreaQuadrado:
    def __init__(self):
        self.valorLado = int(input('Digite o valor do lado do quadrado'))
        
    
    def CalcularArea(self):
         self.area =  self.valorLado ** 2
         
         
    def DobroArea(self):
        self.dobro = self.area * 2
        print('o valor da area do quadro é ', self.area, 'e o dobro da area é',self.dobro)
        
mostrarResultado = AreaQuadrado()
mostrarResultado.CalcularArea()
mostrarResultado.DobroArea()