# 1. Inicio
# 2. Definir la clase Piramide
# 3. Atributo: nivel
# 4. Método construir(n):
#    4.1. Si n == 0, retornar
#    4.2. Llamar a self.construir(n - 1)
#    4.3. Imprimir '*' multiplicado por n
# 5. Método imprimir():
#    5.1. Llamar a construir(self.nivel)
# 6. Crear un objeto de la clase con nivel = 5
# 7. Llamar al método imprimir()
# 8. Fin
class Piramide:
    def __init__(self, nivel):
        self.nivel = nivel

    def construir(self, n):
        if n == 0:
            return
        self.construir(n - 1)
        print('*' * n)

    def imprimir(self):
        self.construir(self.nivel)

objPiramide = Piramide(5)
objPiramide.imprimir()