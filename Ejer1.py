#Algoritmo
# 1.Inicio
# 2.Definir la clase Factoriales
# 2.1. Atributo: n 
# 4.Método: calcular_factorial(num)
# 4.1 Si num es 0 o 1 → retornar 1 (caso base)
# 4.2 Si no → retornar num * calcular_factorial(num # 1) (llamada recursiva)
# 5.Método: imprimir() 
# 5.1 imprime el resultado de calcular_factorial(self.n)
# 6.Crear un objeto de la clase con el valor deseado
# 7.Llamar al método imprimir() para mostrar el resultado
# 8.Fin

class Factoriales:
    def __init__(self, n):
        self.n = n

    def calcular_factorial(self, num):
        if num == 1 or num == 0:
            return 1
        else:
            return num * self.calcular_factorial(num- 1)

    def imprimir(self):
        print(self.calcular_factorial(self.n))

objfac = Factoriales(5)
objfac.imprimir()
 
