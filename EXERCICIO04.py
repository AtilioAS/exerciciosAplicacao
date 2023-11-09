class Aluno:
    def __init__(self,nome,matricula,n1,n2,n3):
        self.nome=nome
        self.matricula=matricula
        self.n1=n1
        self.n2=n2
        self.n3=n3
    def Media(self):
        media=(self.n1+self.n2+self.n3)/3
        print("Média de {} valores".format(media))
        if media>9:
            print("Aluno está aprovado!")
        elif media<=9:
            print("Este aluno está reprovado!")
aluno=str(input("digite oneme do aluno: "))
n1=float(input("digite a primeira nota do aluno: "))
n2=float(input("digite a segunda nota do aluno: "))
n3=float(input("digite a terceira nota do aluno: "))
matricula=int(input("digite o número de matrícula do estudante: "))
estudante=Aluno(aluno,matricula,n1,n2,n3)
estudante.Media()