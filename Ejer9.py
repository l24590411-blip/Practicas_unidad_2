
# 1. Inicio
# 2. Definir la clase Palindromo
# 3. Atributo: palabra
# 4. Método es_palindromo(p):
#    4.1. Si la longitud de p es menor o igual a 1, retornar True
#    4.2. Si p[0] es diferente de p[-1], retornar False
#    4.3. Si no, retornar self.es_palindromo(p[1:-1])
# 5. Método imprimir():
#    5.1. Imprimir el resultado de es_palindromo(self.palabra)
# 6. Crear un objeto de la clase con la palabra "anilina"
# 7. Llamar al método imprimir()
# 8. Fin
class Palindromo:
    def __init__(self, palabra):
        self.palabra = palabra

    def es_palindromo(self, p):
        if len(p) <= 1:
            return True
        elif p[0] != p[-1]:
            return False
        else:
            return self.es_palindromo(p[1:-1])

    def imprimir(self):
        print(self.es_palindromo(self.palabra))

objPalabra = Palindromo("anilina")
objPalabra.imprimir()