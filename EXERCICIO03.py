class Retangulo:
    def __init__(self,largura,altura):
        self.largura=largura
        self.altura=altura
    def CalcularArea(self):
        cal_area=self.largura*self.altura
        print("Área= {} m^2".format(cal_area))
    def CalcularPerimetro(self):
        cal_perimetro=2*(self.largura+self.altura)
        print("Prímetro= {} m".format(cal_perimetro))
A=float(input("digite o valor da altura do Retângulo: "))
B=float(input("digite o valor da largura do Retângulo: "))
Calcular=Retangulo(B,A)
Calcular.CalcularArea()
Calcular.CalcularPerimetro()