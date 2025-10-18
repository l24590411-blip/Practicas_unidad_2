#Algoritmo
# 1.Inicio
# 2.Definir la clase  Fibonnacci
# 2.1. Atributo: n
# 4.Método: fibonacci(num)
# 4.1 if num == 0 or num == 1:  retornar num
# 4.2 Si no   self.fibonacci(num-1) + self.fibonacci(num-2)
# 5.Método: imprimir() 
# 5.1 imprime el resultado de fibonacci(self.n))
# 6.Crear un objeto de la clase con el valor 6
# 7.Llamar al método imprimir() para mostrar el resultado
# 8.Fin
class Fibonnacci:
    def __init__(self,n):
        self.n=n
    def fibonacci(self,num):
        if num == 0 or num == 1:
            return num
        else:
            return self.fibonacci(num-1) + self.fibonacci(num-2)
    def imprimir(self):
        print(self.fibonacci(self.n))
objFibo=Fibonnacci(6)
objFibo.imprimir()