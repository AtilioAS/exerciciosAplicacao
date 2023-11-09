class Carro:
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
        self.velocidadeAtual=0
    def acelerar(self,valor_aceleracao):
        if self.velocidadeAtual+valor_aceleracao>300:
            print("Não é possível acelerar à esta velocidade pois excederá a velocidade limite")
        elif  valor_aceleracao<=300 and valor_aceleracao!=self.velocidadeAtual and valor_aceleracao>0:
            self.velocidadeAtual+=valor_aceleracao
            print("acelerando {} Kmh".format(valor_aceleracao))

        elif valor_aceleracao<0:
            print("aceleração não existente")
    def frear(self,Valor_Freo):
        if Valor_Freo<=self.velocidadeAtual and Valor_Freo>0:
            self.velocidadeAtual-=Valor_Freo
            print("Freando {} Kmh".format(Valor_Freo))
        elif Valor_Freo>self.velocidadeAtual:
            print("-----------------")
    def Velocidadeactual(self):
        print("velocidade do carro {} Kmh".format(self.velocidadeAtual))

carro=Carro("hyundai","i10")
carro.acelerar(-1)
carro.Velocidadeactual()
carro.frear(30)
carro.Velocidadeactual()

"""carro.acelerar(50)
carro.frear(80)
carro.Velocidadeactual()

carro.acelerar(20)
carro.acelerar(100)
carro.Velocidadeactual()

carro.frear(100)
carro.Velocidadeactual()"""