import time
import tracemalloc
def imprimirImparesEntreMyN(m, n):
    if type(m) != int or m < 0:
        raise Exception("m debe ser entero positivo")
    if type(n) != int or n <= m:
        raise Exception("n debe ser entero mayor que m")
    
    m = m + 1 if m % 2 == 0 else m + 2
    n = n - 1 if n % 2 == 0 else n - 2

    tracemalloc.start()
    inicio = time.perf_counter_ns()
    
    imprimirImparesEntreMyNAux(m, n)
    
    fin = time.perf_counter_ns()
    memoria_actual, memoria_maxima = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    print()  # Salto de línea después de imprimir los impares
    print(f"Tiempo de ejecución: {fin - inicio} nanosegundos")
    print(f"Memoria actual usada: {memoria_actual} bytes")
    print(f"Memoria máxima usada: {memoria_maxima} bytes")

def imprimirImparesEntreMyNAux(m, n):
    if m > n:
        return
    else:
        print(m, end=" ")
        imprimirImparesEntreMyNAux(m + 2, n)

# Ejemplo de uso
imprimirImparesEntreMyN(3, 10)