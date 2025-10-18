
# 1. Inicio
# 2. Definir la clase MCD
# 3. Atributos: a, b
# 4. Método calcular_mcd(x, y):
#    4.1. Si y == 0, retornar x
#    4.2. Si no, retornar self.calcular_mcd(y, x % y)
# 5. Método imprimir():
#    5.1. Imprimir el resultado de calcular_mcd(self.a, self.b)
# 6. Crear un objeto de la clase con los valores a = 48 y b = 18
# 7. Llamar al método imprimir()
# 8. Fin
class MCD:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calcular_mcd(self, x, y):
        if y == 0:
            return x
        else:
            return self.calcular_mcd(y, x % y)

    def imprimir(self):
        print(self.calcular_mcd(self.a, self.b))

objMCD = MCD(48, 18)
objMCD.imprimir()