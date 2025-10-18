
# 1. Inicio
# 2. Definir la clase Hanoi
# 3. Atributos: n, origen, destino, auxiliar
# 4. Método mover(n, o, d, a):
#    4.1. Si n == 1, imprimir "Mover disco de o a d"
#    4.2. Si no:
#        4.2.1. Llamar a self.mover(n-1, o, a, d)
#        4.2.2. Llamar a self.mover(1, o, d, a)
#        4.2.3. Llamar a self.mover(n-1, a, d, o)
# 5. Método imprimir():
#    5.1. Llamar a mover(self.n, self.origen, self.destino, self.auxiliar)
# 6. Crear un objeto de la clase con n = 3, origen = "A", destino = "C", auxiliar = "B"
# 7. Llamar al método imprimir()
# 8. Fin
class Hanoi:
    def __init__(self, n, origen, destino, auxiliar):
        self.n = n
        self.origen = origen
        self.destino = destino
        self.auxiliar = auxiliar

    def mover(self, n, o, d, a):
        if n == 1:
            print(f"Mover disco de {o} a {d}")
        else:
            self.mover(n - 1, o, a, d)
            self.mover(1, o, d, a)
            self.mover(n - 1, a, d, o)

    def imprimir(self):
        self.mover(self.n, self.origen, self.destino, self.auxiliar)

objHanoi = Hanoi(3, "A", "C", "B")
objHanoi.imprimir()