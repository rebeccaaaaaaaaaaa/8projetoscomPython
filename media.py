# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

class Notas:
  def __init__(self):
      self.nota1 = float(input('Digite a primeira nota'))
      self.nota2 = float(input('Digite a segunda nota'))
      self.nota3 = float(input('Digite a terceira nota'))
      self.nota4 = float(input('Digite a quarta nota'))
      
  def Media(self):
      self.media = (self.nota1 + self.nota2 + self.nota3 + self.nota4) / 4 
      print('A média das notas é',self.media)
      
      if self.media < 6:
          print('Voce está reprovado')
      else:
          print('Aprovado!')
      
mostarMedia = Notas()
mostarMedia.Media()