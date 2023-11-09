class Livro:
    lot=10
    def __init__(self,autor,titulo,numero_paginas):
        self.autor = autor
        self.titulo=titulo
        self.numero_paginas=numero_paginas

    def Emprestar(self,livro):
        if livro in self.titulo:
            emprestados.append(livro)
            print("emprestando o livro: ",livro)
            self.titulo.remove(livro)
        elif livro not in self.titulo and livro in emprestados:
            print("Este livro foi emprestado.")
        else:
            print("O livro ",livro," não faz parte do estoque de livros.")
    def Devolver(self,livro):
        if livro in emprestados:
            self.titulo.append(livro)
            emprestados.remove(livro)
        else:
            print("este livro não foi emprestado")
    def Emprestados(self):
        print("Livros Emprestados {}".format(emprestados))
    def verificar_livros(self):
        print("livros disponíveis: {}".format(self.titulo))

autor=str(input("digite o nome do autor: "))
titulo=[]
numero_paginas=[]
emprestados=[]
cont=0
while cont<3:
    Titulo=str(input("digite o título do livro: "))
    titulo.append(Titulo)
    Numero_Paginas=int(input("informe o número de páginas do livro: "))
    numero_paginas.append(Numero_Paginas)
    cont+=1
livro=Livro(autor,titulo,numero_paginas)
livro.verificar_livros()
livro.Emprestar("ricos")
livro.Emprestar("pobres")
livro.verificar_livros()
livro.Emprestados()
livro.Emprestar("todo")
livro.Devolver("ricos")
livro.verificar_livros()