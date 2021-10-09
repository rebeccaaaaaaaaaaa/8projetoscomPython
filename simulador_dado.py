# simulador de dado
# simular o uso de um dado gerando um valor de 1 até 6

import random

class SimuladorDeDado:
    # definir o comportamento inicial da nossa classe
    def __init__(self):
        self.valor_min = 1
        self.valor_max = 6
        self.mensagem = "Voce gostaria de gerar um novo valor para o dado?"
        
    def Iniciar(self):
        resposta = input(self.mensagem)
        
        try:
            if resposta == 'sim'  or resposta == 's':
                self.GerarValorDoDado()   
            elif resposta == 'nao' or resposta == 'n':
                print('Ok, obrigado')
            else:
                print('Favor digitar sim ou não')
                
        except:
            print('Ocorreu um erro ao receber sua resposta')
            
    def GerarValorDoDado(self):
        print(random.randint(self.valor_min,self.valor_max))
        
simulador = SimuladorDeDado()
simulador.Iniciar()