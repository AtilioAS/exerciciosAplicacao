class Paciente:
    def __init__(self,nome, idade, consultas):
        self.nome=nome
        self.idade=idade
        self.consultas=consultas
    def Nova_Consulta(self,tipo):
        self.consultas.append(tipo)
        print("Consuta de {} realizada com sucesso!".format(tipo))
    def histórico_Consultas(self):
        print("CONSULTAS REALIZADAS DO PACIENTE {}".format(self.nome))
        print(self.consultas)
Nomes=[]
Idades=[]
Consultas=[]
nome_paciente=str(input("Digite o nome do paciente: "))
Nomes.append(nome_paciente)
idade_paciente=int(input("digite a idade do paciente: "))
Idades.append(idade_paciente)
cont=0
while cont<2:
    consulta_paciente=str(input("informe o tipo da consulta: "))
    Consultas.append(consulta_paciente)
    cont+=1

paciente=Paciente(Nomes,Idades,Consultas)
paciente.histórico_Consultas()
nova_consulta=str(input("informe a nova consulta a ser realizada: "))
paciente.Nova_Consulta(nova_consulta)
paciente.histórico_Consultas()