import os
class ContaBancaria:
    def __init__(self,nome,numero,saldo):
        self.nome=nome
        self.numero=numero
        self.saldo=saldo
    def ConsultarSaldo(self):
        print("Saldo disponível: ",self.saldo," AKZ")
    def Levantamento(self,valor):
        self.valor=valor
        if self.saldo<self.valor:
            print("Nã0 é possível levantar o valor")
        elif self.saldo>=self.valor:
            self.saldo=self.saldo-self.valor
            print("levantamento de:",self.valor,"\nSaldo actual: ", self.saldo)

    def Deposito(self,quantidade):
        self.saldo+=quantidade
nome=str(input("digite o  nome do titular: "))
numero_conta=int(input("digite o numero da conta: "))
saldo=float(input("informe o saldo da conta: "))
Conta1=ContaBancaria(nome,numero_conta,saldo)
Conta1.ConsultarSaldo()
opcao=1
while opcao==1 or opcao==2:
    opcao=int(input("1- Levantamento\n2- Depósito\nEscolha uma opção=> "))
    if opcao==1:
        valor=float(input("Informe quanto deseja levantar: "))
        Conta1.Levantamento(valor)
        os.system("cls")
        Conta1.ConsultarSaldo()
    elif opcao==2:
        valor = float(input("Informe quanto deseja depositar: "))
        Conta1.Deposito(valor)
        os.system("cls")
        Conta1.ConsultarSaldo()
    else:
        print("Opção inválida.")