class Triangulo:
    def __init__(self,cm_esquerda,cm_direita,base):
        self.cm_esquerda=cm_esquerda
        self.cm_direita=cm_direita
        self.base=base
    def VerificarTriangulo(self):
        if self.cm_esquerda==self.cm_direita and self.cm_esquerda!=self.base and self.cm_direita!=self.base:
            print("o triângulo é válido")
        else:
            print("o triângulo não é válido")
    def CalcularArea(self):
        if self.cm_esquerda == self.cm_direita and self.cm_esquerda != self.base and self.cm_direita != self.base:
            area=(self.cm_esquerda+self.cm_direita)/2*base/2
            print("Área ={} m^2".format(area))
        else:
            raise exec("Erro nas Medições")
cm_esquerda=float(input("digite o valor do comprimento a esquerda: "))
cm_direita=float(input("digite o valor do comprimento a direita:"))
base=float(input("digite o valor da base: "))
triangulo=Triangulo(cm_esquerda,cm_direita,base)
triangulo.VerificarTriangulo()
triangulo.CalcularArea()