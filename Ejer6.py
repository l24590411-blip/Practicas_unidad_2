
#Algoritmo
# 1.Inicio
# 2.Definir la clase  Vocales
# 2.1. Atributo: cadena
# 4.Método: contar_vocales(c):
# 4.1 if c== ""retornar 0
# 4.2 Si no hacer si if c[0].lower() in 'aeiou': retornar 1 + self.contar_vocales(c[1:])
#   4.2.1 Sino retornar  self.contar_vocales(c[1:])
# 5.Método: imprimir() 
# 5.1 imprime el resultado de contar_vocales(self.cadena))
# 6.Crear un objeto de la clase con el valor "Recursividad"
# 7.Llamar al método imprimir() para mostrar el resultado
# 8.Fin
class Vocales:
    def __init__(self,cadena):
        self.cadena=cadena
    def contar_vocales(self,c):
        if c == "":
            return 0
        else:
            if c[0].lower() in 'aeiou':
                return 1 + self.contar_vocales(c[1:])
            else:
                return self.contar_vocales(c[1:])
    def imprimir(self):
        print(self.contar_vocales(self.cadena))
objFibo=Vocales("Recursividad")
objFibo.imprimir()
