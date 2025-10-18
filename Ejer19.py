# 1. Inicio
# 2. Definir la clase Primo
# 3. Atributo: numero
# 4. Método es_primo(n, divisor):
#    4.1. Si n <= 2, retornar n == 2
#    4.2. Si n % divisor == 0, retornar False
#    4.3. Si divisor * divisor > n, retornar True
#    4.4. Si no, retornar self.es_primo(n, divisor + 1)
# 5. Método imprimir():
#    5.1. Imprimir el resultado de es_primo(self.numero, 2)
# 6. Crear un objeto de la clase con numero = 13
# 7. Llamar al método imprimir()
# 8. Fin
class Primo:
    def __init__(self, numero):
        self.numero = numero

    def es_primo(self, n, divisor=2):
        if n <= 2:
            return n == 2
        if n % divisor == 0:
            return False
        if divisor * divisor > n:
            return True
        return self.es_primo(n, divisor + 1)

    def imprimir(self):
        print(self.es_primo(self.numero))

objPrimo = Primo(13)
objPrimo.imprimir()