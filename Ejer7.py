# 1. Inicio
# 2. Definir la clase SumaLista
# 3. Atributo: lista
# 4. Método sumar_elementos(l):
#    4.1. Si l está vacía, retornar 0
#    4.2. Si no, retornar l[0] + self.sumar_elementos(l[1:])
# 5. Método imprimir():
#    5.1. Imprimir el resultado de sumar_elementos(self.lista)
# 6. Crear un objeto de la clase con la lista [1, 2, 3, 4, 5]
# 7. Llamar al método imprimir()
# 8. Fin
class SumaLista:
    def __init__(self, lista):
        self.lista = lista

    def sumar_elementos(self, l):
        if not l:
            return 0
        else:
            return l[0] + self.sumar_elementos(l[1:])

    def imprimir(self):
        print(self.sumar_elementos(self.lista))

objSuma = SumaLista([1, 2, 3, 4, 5])
objSuma.imprimir()
