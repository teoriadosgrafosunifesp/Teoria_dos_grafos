from grafos.grafos import gerar_grafo_a_partir_lista, gerar_grafo_a_partir_matriz, gerar_grafo_a_partir_matriz_incidencia, gerar_lista_adjacencia, gerar_matriz_adjacencia, gerar_matriz_incidencia

# EX 1

grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

print("Gerar matriz adjacencia")
matriz_adjacencia = gerar_matriz_adjacencia(grafo)
for linha in matriz_adjacencia:
    print(linha)

# EX 2

matriz_adjacencia = [
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [0, 1, 1, 0]
]

print("Gerar grafo a partir matriz adjacencia")
grafo = gerar_grafo_a_partir_matriz(matriz_adjacencia)
print(grafo)


grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

print("Gerar matriz incidencia")
matriz_incidencia = gerar_matriz_incidencia(grafo)
for linha in matriz_incidencia:
    print(linha)


matriz_incidencia = [
    [1, 1, 0, 0],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [0, 0, 1, 1]
]

print("Gerar grafo a partir matriz incidencia")
grafo = gerar_grafo_a_partir_matriz_incidencia(matriz_incidencia)
print(grafo)


grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

print("Gerar lista adjacencia")
lista_adjacencia = gerar_lista_adjacencia(grafo)
print(lista_adjacencia)


lista_adjacencia = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

print("Gerar grafo a partir da lista")
grafo = gerar_grafo_a_partir_lista(lista_adjacencia)
print(grafo)


grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

print("Matriz adjacencia")
matriz_adjacencia = gerar_matriz_adjacencia(grafo)
for linha in matriz_adjacencia:
    print(linha)

print("Matriz incidencia")
matriz_incidencia = gerar_matriz_incidencia(grafo)
for linha in matriz_incidencia:
    print(linha)

