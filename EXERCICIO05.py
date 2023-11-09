class Funcionario:
    def __init__(self,nome,salario,cargo):
        self.nome=nome
        self.salario=salario
        self.cargo=cargo
    def SalarioLiquido (self,imposto,beneficios):
        salario_liquido=self.salario-imposto-beneficios
        print("o salário líquido do Sr {} é de {} AKZ".format(self.nome,salario_liquido))
Nome=str(input("Digite o nome do do funcionário: "))
Cargo=str(input("Digite o cargo do do funcionário: "))
Salario=float(input("Digite o salário do do funcionário: "))
funcionário=Funcionario(Nome,Salario,Cargo)
Imposto=float(input("Digite o valor total de imposto do funcionário: "))
Beneficios=float(input("Digite o valor total de benefícios do funcionário: "))
funcionário.SalarioLiquido(Imposto,Beneficios)