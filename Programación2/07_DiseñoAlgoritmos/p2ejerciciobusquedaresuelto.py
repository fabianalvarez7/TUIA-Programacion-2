S = 10


def es_solucion(xs):
    return sum(xs) >= S


def candidatos_correctos(xs):
    # Primero generamos todas las sublistas de longitud 1, luego todas las de
    # longitud 2 y asi:
    n = len(xs)
    for longitud_de_sublista in range(1, n + 1):
        for punto_de_inicio in range(0, n - longitud_de_sublista + 1):
            yield xs[punto_de_inicio : punto_de_inicio + longitud_de_sublista]


def medir(xs):
    return sum(xs)


def resolver(lista):
    mejor_solucion = None
    # infinito - tambien sirve un numero muy muy grande
    mejor_costo_solucion = float("inf")
    for intento in candidatos_correctos(lista):
        if es_solucion(intento):
            costo = medir(intento)
            if costo < mejor_costo_solucion:
                mejor_solucion = intento
                mejor_costo_solucion = costo
    return mejor_solucion


print(resolver([1, 7, 4, 5, 3, 7]))
