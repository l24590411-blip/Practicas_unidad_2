#Algoritmo
# 1.Inicio
# 2.Definir la clase Potencia
# 2.1. Atributo: a,b 
# 4.Método: potencia(x,y)
# 4.1 Si y== 0  retornar 1
# 4.2 Si no  retornar x * self.potencia(x, y-1)
# 5.Método: imprimir() 
# 5.1 imprime el resultado de potencia(self.a,self.b))
# 6.Crear un objeto de la clase con el valor 2,3
# 7.Llamar al método imprimir() para mostrar el resultado
# 8.Fin
class Potencia:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def potencia(self,x, y):
        if y == 0:
            return 1
        else:
            return x * self.potencia(x, y-1)
    def imprimir(self):
        print(self.potencia(self.a,self.b))
    
objPotencia=Potencia(2,3)
objPotencia.imprimir()