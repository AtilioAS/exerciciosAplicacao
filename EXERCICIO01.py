from math import pow
class Circulo:
    def CalcularArea (self, raio):
        #self.raio=raio
        Cal_Area = 3.14 * pow(raio, 2)
        print("Área= {:.1f} m^2".format(Cal_Area))
    def CacularPerimetro (self, raio):
        #self.raio = raio
        Cal_Per = 2 * 3.14 * raio
        print("Perímetro= {:.1f} m".format(Cal_Per))
r = float(input("Digite o valor do raio: "))
Calcular = Circulo()
print("Escolha uma das opções: ")
opcao = int(input("1- Calcular Área\n2- Calcular Perímetro\n"))
if opcao == 1:
    Calcular.CalcularArea(r)
elif opcao == 2:
    Calcular.CacularPerimetro(r)
else:
    raise exec("Opção Inválida")