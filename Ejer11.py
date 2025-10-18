

# 1. Inicio
# 2. Definir la clase BuscadorElemento
# 3. Atributos: lista, elemento
# 4. Método buscar(l, e):
#    4.1. Si l está vacía, retornar False
#    4.2. Si l[0] == e, retornar True
#    4.3. Si no, retornar self.buscar(l[1:], e)
# 5. Método imprimir():
#    5.1. Imprimir el resultado de buscar(self.lista, self.elemento)
# 6. Crear un objeto de la clase con lista = [1, 3, 5, 7] y elemento = 5
# 7. Llamar al método imprimir()
# 8. Fin
class BuscadorElemento:
    def __init__(self, lista, elemento):
        self.lista = lista
        self.elemento = elemento

    def buscar(self, l, e):
        if not l:
            return False
        elif l[0] == e:
            return True
        else:
            return self.buscar(l[1:], e)

    def imprimir(self):
        print(self.buscar(self.lista, self.elemento))

objBusqueda = BuscadorElemento([1, 3, 5, 7], 5)
objBusqueda.imprimir()
