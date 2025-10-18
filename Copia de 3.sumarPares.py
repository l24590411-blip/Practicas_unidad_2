import time
import tracemalloc

def sumarPares(n):
    if type(n) != int or n < 3:
        raise Exception("n debe ser entero mayor que 2")
    
    n -= n % 2  # Asegura que n sea par
    
    tracemalloc.start()
    inicio = time.perf_counter_ns()
    
    resultado = sumarParesAux(n)
    
    fin = time.perf_counter_ns()
    memoria_actual, memoria_maxima = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    print(f"Tiempo de ejecución: {fin - inicio} nanosegundos")
    print(f"Memoria actual usada: {memoria_actual} bytes")
    print(f"Memoria máxima usada: {memoria_maxima} bytes")
    
    return resultado

def sumarParesAux(n):
    if n == 0:
        return 0
    else:
        return sumarParesAux(n - 2) + n

# Ejemplo de uso
print("Suma de pares:", sumarPares(20))