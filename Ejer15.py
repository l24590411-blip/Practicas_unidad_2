# 1. Inicio
# 2. Definir la clase SumaDigitos
# 3. Atributo: numero
# 4. Método sumar(n):
#    4.1. Si n == 0, retornar 0
#    4.2. Si no, retornar n % 10 + self.sumar(n // 10)
# 5. Método imprimir():
#    5.1. Imprimir el resultado de sumar(self.numero)
# 6. Crear un objeto de la clase con numero = 1234
# 7. Llamar al método imprimir()
# 8. Fin
class SumaDigitos:
    def __init__(self, numero):
        self.numero = numero

    def sumar(self, n):
        if n == 0:
            return 0
        else:
            return n % 10 + self.sumar(n // 10)

    def imprimir(self):
        print(self.sumar(self.numero))

objSuma = SumaDigitos(1234)
objSuma.imprimir()