import time
import tracemalloc

def contarDigitos(n):
    if type(n) != int or n < 0:
        raise Exception("n debe ser entero no negativo.")
    return contarDigitosAux(n)

def contarDigitosAux(n):
    if n < 10:
        return 1
    else:
        return contarDigitosAux(n // 10) + 1

def invertirEntero(n):
    if type(n) != int or n < 1:
        raise Exception("n debe ser entero positivo.")
    
    tracemalloc.start()
    inicio = time.perf_counter_ns()
    
    resultado = invertirEnteroAux(n)
    
    fin = time.perf_counter_ns()
    memoria_actual, memoria_maxima = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    print(f"Tiempo de ejecución: {fin - inicio} nanosegundos")
    print(f"Memoria actual usada: {memoria_actual} bytes")
    print(f"Memoria máxima usada: {memoria_maxima} bytes")
    
    return resultado

def invertirEnteroAux(n):
    if n < 10:
        return n
    else:
        return (n % 10) * 10**contarDigitos(n // 10) + invertirEnteroAux(n // 10)

print("Número invertido:", invertirEntero(123456789))