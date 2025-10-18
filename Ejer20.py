# 1. Inicio
# 2. Definir la clase Permutador
# 3. Atributo: lista
# 4. Método generar_permutaciones(l, inicio):
#    4.1. Si inicio == len(l) - 1, imprimir l
#    4.2. Si no:
#        4.2.1. Para i desde inicio hasta len(l) - 1:
#            4.2.1.1. Intercambiar l[inicio] con l[i]
#            4.2.1.2. Llamar a self.generar_permutaciones(l, inicio + 1)
#            4.2.1.3. Revertir el intercambio
# 5. Método imprimir():
#    5.1. Llamar a generar_permutaciones(self.lista, 0)
# 6. Crear un objeto de la clase con lista = [1, 2, 3]
# 7. Llamar al método imprimir()
# 8. Fin
class Permutador:
    def __init__(self, lista):
        self.lista = lista

    def generar_permutaciones(self, l, inicio):
        if inicio == len(l) - 1:
            print(l)
        else:
            for i in range(inicio, len(l)):
                l[inicio], l[i] = l[i], l[inicio]
                self.generar_permutaciones(l, inicio + 1)
                l[inicio], l[i] = l[i], l[inicio]  # revertir

    def imprimir(self):
        self.generar_permutaciones(self.lista, 0)

objPerm = Permutador([1, 2, 3])
objPerm.imprimir()