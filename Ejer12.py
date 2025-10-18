
# 1. Inicio
# 2. Definir la clase Multiplicador
# 3. Atributos: a, b
# 4. Método multiplicar(x, y):
#    4.1. Si y == 0, retornar 0
#    4.2. Si no, retornar x + self.multiplicar(x, y - 1)
# 5. Método imprimir():
#    5.1. Imprimir el resultado de multiplicar(self.a, self.b)
# 6. Crear un objeto de la clase con a = 3 y b = 4
# 7. Llamar al método imprimir()
# 8. Fin
class Multiplicador:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def multiplicar(self, x, y):
        if y == 0:
            return 0
        else:
            return x + self.multiplicar(x, y - 1)

    def imprimir(self):
        print(self.multiplicar(self.a, self.b))

objMult = Multiplicador(3, 4)
objMult.imprimir()
