
# 1. Inicio
# 2. Definir la clase InversorCadena
# 3. Atributo: cadena
# 4. Método invertir(c):
#    4.1. Si la longitud de c es 0, retornar c
#    4.2. Si no, retornar c[-1] + self.invertir(c[:-1])
# 5. Método imprimir():
#    5.1. Imprimir el resultado de invertir(self.cadena)
# 6. Crear un objeto de la clase con la cadena "hola"
# 7. Llamar al método imprimir()
# 8. Fin
class InversorCadena:
    def __init__(self, cadena):
        self.cadena = cadena

    def invertir(self, c):
        if len(c) == 0:
            return c
        else:
            return c[-1] + self.invertir(c[:-1])

    def imprimir(self):
        print(self.invertir(self.cadena))

objCadena = InversorCadena("hola")
objCadena.imprimir()