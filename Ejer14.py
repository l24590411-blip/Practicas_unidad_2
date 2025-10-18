# 1. Inicio
# 2. Definir la clase ContadorCaracter
# 3. Atributos: cadena, caracter
# 4. Método contar(c, ch):
#    4.1. Si c es cadena vacía, retornar 0
#    4.2. Si c[0] == ch, retornar 1 + self.contar(c[1:], ch)
#    4.3. Si no, retornar self.contar(c[1:], ch)
# 5. Método imprimir():
#    5.1. Imprimir el resultado de contar(self.cadena, self.caracter)
# 6. Crear un objeto de la clase con cadena = "banana" y caracter = "a"
# 7. Llamar al método imprimir()
# 8. Fin
class ContadorCaracter:
    def __init__(self, cadena, caracter):
        self.cadena = cadena
        self.caracter = caracter

    def contar(self, c, ch):
        if c == "":
            return 0
        elif c[0] == ch:
            return 1 + self.contar(c[1:], ch)
        else:
            return self.contar(c[1:], ch)

    def imprimir(self):
        print(self.contar(self.cadena, self.caracter))

objContador = ContadorCaracter("banana", "a")
objContador.imprimir()
