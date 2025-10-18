import time
import tracemalloc

def imprimirParesHastaN(n):
    if type(n) != int or n < 1:
        raise Exception("n debe ser entero positivo")
    
    n -= n % 2  # Asegura que n sea par
    
    tracemalloc.start()
    inicio = time.perf_counter_ns()
    
    imprimirParesHastaNAux(n)
    
    fin = time.perf_counter_ns()
    memoria_actual, memoria_maxima = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    print()  # Salto de línea después de imprimir los pares
    print(f"Tiempo de ejecución: {fin - inicio} nanosegundos")
    print(f"Memoria actual usada: {memoria_actual} bytes")
    print(f"Memoria máxima usada: {memoria_maxima} bytes")

def imprimirParesHastaNAux(n):
    if n == 0:
        return
    else:
        imprimirParesHastaNAux(n - 2)
        print(n, end=" ")

# Ejemplo de uso
imprimirParesHastaN(10)
