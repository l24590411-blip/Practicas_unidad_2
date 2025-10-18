#Algoritmo
# 1.Inicio
# 2.Definir la clase Contar
# 2.1. Atributo: n 
# 4.Método: Contar_digitos(num)
# 4.1 Si num <10 retornar 1
# 4.2 Si no  retornar 1 + llamar a metodo contar_digitos
# 5.Método: imprimir() 
# 5.1 imprime el resultado de conatr_digitos(self.n)
# 6.Crear un objeto de la clase con el valor 12345
# 7.Llamar al método imprimir() para mostrar el resultado
# 8.Fin
class Contar:
    def __init__(self,n):
        self.n=n
    def contar_digitos(self,num):
        if num < 10:
            return 1
        else:
            return 1 + self.contar_digitos(num // 10)
    def imprimir(self):
        print(self.contar_digitos(self.n))
objContar=Contar(12345)
objContar.imprimir()
