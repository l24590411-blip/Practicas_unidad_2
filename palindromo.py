def es_palindromo(s: str) -> bool:
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return es_palindromo(s[1:-1])

def es_palindromo_normalizado(s: str) -> bool:

    t = "".join(ch.lower() for ch in s if ch.isalnum())
    return es_palindromo(t)

# Pruebas
print(es_palindromo_normalizado("anilina"))
print(es_palindromo_normalizado("A man a plan a canal Panama"))
print(es_palindromo_normalizado("hola"))