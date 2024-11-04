from grafos.grafos import caminho_dfs, eh_subgrafo, encontrar_ciclo, existe_aresta_lista_adjacencia, gerar_grafo_a_partir_lista, gerar_grafo_a_partir_matriz, gerar_grafo_a_partir_matriz_incidencia, gerar_lista_adjacencia, gerar_matriz_adjacencia, gerar_matriz_incidencia, grau_vertice_lista_adjacencia, graus_grafo_lista_adjacencia, numero_arestas_lista_adjacencia, numero_vertices, vertices_adjacentes

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

# EX 3
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

# EX 4
matriz_incidencia = [
    [1, 1, 0, 0],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [0, 0, 1, 1]
]

print("Gerar grafo a partir matriz incidencia")
grafo = gerar_grafo_a_partir_matriz_incidencia(matriz_incidencia)
print(grafo)

# EX 5
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

print("Gerar lista adjacencia")
lista_adjacencia = gerar_lista_adjacencia(grafo)
print(lista_adjacencia)

# EX 6
lista_adjacencia = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

print("Gerar grafo a partir da lista")
grafo = gerar_grafo_a_partir_lista(lista_adjacencia)
print(grafo)

# EX 7
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


# -------------------------------------------------
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Função 1: Número de Vértices
print("Número de Vértices:", numero_vertices(grafo))

# Função 2: Número de Arestas
print("Número de Arestas:", numero_arestas_lista_adjacencia(grafo))

# Função 3: Vértices Adjacentes
print("Vértices adjacentes a 'B':", vertices_adjacentes(grafo, 'B'))

# Função 4: Existência de Aresta entre Dois Vértices

# Verificar se existe uma aresta entre 'A' e 'B'
print("Existe aresta entre 'A' e 'B'?:", existe_aresta_lista_adjacencia(grafo, 'A', 'B'))

# Verificar se existe uma aresta entre 'A' e 'D'
print("Existe aresta entre 'A' e 'D'?:", existe_aresta_lista_adjacencia(grafo, 'A', 'D'))

# Função 5: Grau de um Vértice
print("Grau do vértice 'B':", grau_vertice_lista_adjacencia(grafo, 'B'))

# Função 6: Grau de Todos os Vértices
print("Graus dos vértices:", graus_grafo_lista_adjacencia(grafo))

# Função 7: Caminho Simples entre Dois Vértices (DFS)
print("Caminho entre 'A' e 'F':", caminho_dfs(grafo, 'A', 'F'))

# Função 8: Encontrar um Ciclo contendo um Vértice Específico
print("Ciclo contendo 'C':", encontrar_ciclo(grafo, 'C'))

# Função 9: Verificar se um Grafo é Subgrafo de Outro

# Subgrafo de exemplo
subgrafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A'],
    'D': ['B']
}

# Verificar se 'subgrafo' é subgrafo de 'grafo'
print("subgrafo é subgrafo de grafo?:", eh_subgrafo(subgrafo, grafo))

# Verificar se 'grafo' é subgrafo de 'subgrafo'
print("grafo é subgrafo de subgrafo?:", eh_subgrafo(grafo, subgrafo))

