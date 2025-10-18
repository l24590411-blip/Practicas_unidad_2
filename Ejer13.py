# 1. Inicio
# 2. Definir la clase Binario
# 3. Atributo: numero
# 4. Método convertir(n):
#    4.1. Si n == 0, retornar cadena vacía ''
#    4.2. Si no, retornar self.convertir(n // 2) + str(n % 2)
# 5. Método imprimir():
#    5.1. Imprimir el resultado de convertir(self.numero)
# 6. Crear un objeto de la clase con numero = 10
# 7. Llamar al método imprimir()
# 8. Fin
class Binario:
    def __init__(self, numero):
        self.numero = numero

    def convertir(self, n):
        if n == 0:
            return ''
        else:
            return self.convertir(n // 2) + str(n % 2)

    def imprimir(self):
        print(self.convertir(self.numero))

objBinario = Binario(10)
objBinario.imprimir()
