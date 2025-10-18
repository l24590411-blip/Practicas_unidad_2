import time
import tracemalloc

def sumarDigitos(n):
    if type(n) != int or n < 0:
        raise Exception("n debe ser entero no negativo.")
    
    tracemalloc.start()
    inicio = time.perf_counter_ns()
    
    resultado = sumarDigitosAux(n)
    
    fin = time.perf_counter_ns()
    memoria_actual, memoria_maxima = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    print(f"Tiempo de ejecución: {fin - inicio} nanosegundos")
    print(f"Memoria actual usada: {memoria_actual} bytes")
    print(f"Memoria máxima usada: {memoria_maxima} bytes")
    
    return resultado

def sumarDigitosAux(n):
    if n < 10:
        return n
    else:
        return sumarDigitosAux(n // 10) + n % 10

# Ejemplo de uso
print("Resultado:", sumarDigitos(123456789))