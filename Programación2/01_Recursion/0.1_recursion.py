def replicar(lista, cantidad):
    print(f"REPLICAR: {lista}, {cantidad}")
    # caso base
    if lista == []:
        print("CASO BASE")
        return []

    elemento = lista[0]

    # recursion
    resto = replicar(lista[1:], cantidad)

    resultado = [elemento] * cantidad + resto
    print(f"RETORNAMOS RESULTADO: {resultado} [de la llamada {lista}, {cantidad}]")
    return resultado

replicar([1, 2, 3, 4], 2) # [1, 1, 2, 2, 3, 3, 4, 4]

def indexof(string, sub, index = 0): # podemos trabajarlo en un parametro
    # caso base
    if string == "":
        return -1
    
    # caso feliz :)
    if string.startswith(sub):
        return index
    
    # caso triste :(
    return indexof(string[1:], sub, index + 1)

print(indexof("Un tete a tete y Tete", "te")) # 3

# nunca vamos a calcular 0 ** 0
def _potencia(b, n):
    # caso base
    if n == 0:
        return 1
    
    # caso recursivo asumiendo n positivo
    return b * _potencia(b, n - 1)

# b ** -n === 1 / (b ** n)
def potencia(b, n):
    # introduzco una guarda inicial con el n negativo
    if n < 0:
        return 1 / _potencia(b, -n)
    else:
        return _potencia(b, n)

print(potencia(2, -3)) # 0.125 (1/8)