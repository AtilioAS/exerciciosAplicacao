class estacionamento:
    def __init__(self,lotacao):
        self.lotacao=lotacao
    def entrar(self,num_carros):
        self.entrada=num_carros
        if self.lotacao==0:
            print("Estacionamento Lotado")
        elif self.entrada<=self.lotacao and self.entrada>0:
            self.lotacao-=self.entrada
            print(self.entrada," carros entraram no estacionamento")
        elif self.entrada>self.lotacao:
            print("A lotação não permite entrar esse número de carros")
        elif self.entrada==0:
            print("Você não informou quantos carros devem entrar")
        else:
            raise exec("você não pode inserir um número negativo como entrada!")
    def sair(self,num_carros):
        self.saida=num_carros
        if self.entrada>self.lotacao:
            print("---------------")
        elif self.saida<=self.entrada:
            self.lotacao+=self.saida
            self.entrada-=self.saida
            print(self.saida," carros saíram do estacionamento")
        elif self.saida>self.entrada and self.saida>self.lotacao:
            print("---------------")
    def lugares(self):
        print("Há {} espaços livres".format(self.lotacao))
lotacao=10
veiculos=estacionamento(lotacao)
veiculos.entrar(5)
veiculos.sair(3)
veiculos.lugares()