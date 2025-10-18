#Algoritmo
# 1.Inicio
# 2.Definir la clase Suma
# 2.1. Atributo: n 
# 4.Método: Suma_natural(num)
# 4.1 Si num =1 retornar 1
# 4.2 Si no  retornar num + llamar a metodo suma_natural
# 5.Método: imprimir() 
# 5.1 imprime el resultado de suma_natural(self.n)
# 6.Crear un objeto de la clase con el valor 5
# 7.Llamar al método imprimir() para mostrar el resultado
# 8.Fin
class Suma():
    def __init__(self,n):
        self.n=n
    def suma_natural(self,num):
        if num == 1:
            return 1
        else:
            return num + self.suma_natural(num-1)
    def imprimir(self):
        print(self.suma_natural(self.n))
objSuma=Suma(5)
objSuma.imprimir()
