
import time
import tracemalloc

def contarDigitos(n):
    if type(n) != int or n < 0:
        raise Exception("n debe ser entero no negativo.")
    
    tracemalloc.start()
    inicio = time.perf_counter_ns()
    
    resultado = contarDigitosAux(n)
    
    fin = time.perf_counter_ns()
    memoria_actual, memoria_maxima = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    print(f"Tiempo de ejecución: {fin - inicio} nanosegundos")
    print(f"Memoria actual usada: {memoria_actual} bytes")
    print(f"Memoria máxima usada: {memoria_maxima} bytes")
    
    return resultado

def contarDigitosAux(n):
    if n < 10:
        return 1
    else:
        return contarDigitosAux(n // 10) + 1

# Ejemplo de uso
print("Cantidad de dígitos:", contarDigitos(9876543210))