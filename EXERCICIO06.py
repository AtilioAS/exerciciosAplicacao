class Produto:
    def __init__(self,nome,preco,quantidade):
        self.nome=nome
        self.preco=preco
        self.quantidade=quantidade
    def Valor_EM_Estoque(self):
        cont=0
        aux=0
        Soma_estoque=0
        while cont<(len(self.quantidade)) and cont<(len(self.preco)):
            M_Q_P = self.preco[aux]*self.quantidade[aux]
            Soma_estoque = M_Q_P+Soma_estoque
            aux+=1
            cont+=1
        print("a quantidade em estoque é de: ",Soma_estoque)
    def verificar(self,produto):
        if produto in self.nome:
            print("produto disponível")
        else:
            print("produto não disponível")


cont=0
p_produto=[]
n_pro=[]
q_produto =[]
while cont<2:
    Nome_produto=str(input("Digite o nome do produto: "))
    n_pro.insert(cont,Nome_produto)
    preco_produto = float(input("Digite o preço do produto: "))
    p_produto.insert(cont,preco_produto)
    quantidade_produto = int(input("Digite a quantidade do produto: "))
    q_produto.insert(cont,quantidade_produto)
    cont=cont+1
Produtos = Produto(n_pro, p_produto, q_produto)
Produtos.Valor_EM_Estoque()
nomeproduto=str(input("digite o nome do produto: "))
Produtos.verificar(nomeproduto)