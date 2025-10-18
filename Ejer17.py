# 1. Inicio
# 2. Definir la clase Combinador
# 3. Atributo: cadena
# 4. Método generar(c, actual):
#    4.1. Si c es cadena vacía, imprimir actual
#    4.2. Si no:
#        4.2.1. Llamar a self.generar(c[1:], actual + c[0])
#        4.2.2. Llamar a self.generar(c[1:], actual)
# 5. Método imprimir():
#    5.1. Llamar a generar(self.cadena, "")
# 6. Crear un objeto de la clase con cadena = "ab"
# 7. Llamar al método imprimir()
# 8. Fin
class Combinador:
    def __init__(self, cadena):
        self.cadena = cadena

    def generar(self, c, actual):
        if c == "":
            print(actual)
        else:
            self.generar(c[1:], actual + c[0])
            self.generar(c[1:], actual)

    def imprimir(self):
        self.generar(self.cadena, "")

objComb = Combinador("ab")
objComb.imprimir()
