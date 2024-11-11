from grafos.grafos import caminho_dfs, eh_subgrafo, encontrar_ciclo, existe_aresta_lista_adjacencia, gerar_grafo_a_partir_lista, gerar_grafo_a_partir_matriz, gerar_grafo_a_partir_matriz_incidencia, gerar_lista_adjacencia, gerar_matriz_adjacencia, gerar_matriz_incidencia, grau_vertice_lista_adjacencia, graus_grafo_lista_adjacencia, numero_arestas_lista_adjacencia, numero_vertices, vertices_adjacentes

G_materias = {'AED I': ['LP', 'AED II', 'BD', 'Computacao Grafica', 'IA', 'Prog OO', 'SO'], 
              'LP': ['AED I', 'AOC', 'Embarcados', 'LFA', 'Otimizacao Linear', 'Otimizacao nao-linear'], 
              'AED II': ['AED I', 'PAA'], 
              'AL Comp': ['CN'], 
              'CN': ['AL Comp', 'GA', 'Metodos Numericos para Eq Dif.', 'Otimizacao nao-linear'], 
              'AL I': ['GA', 'AL II', 'EDO', 'Espacos Metricos', 'Metodos Numericos para Eq Dif.'], 
              'GA': ['AL I', 'CN', 'CVV', 'MecG', 'Otimizacao Linear'], 
              'AL II': ['AL I'], 
              'Analise de Sinais': ['Series e EDO'], 
              'Series e EDO': ['Analise de Sinais', 'ED Parciais', 'EDO', 'FA', 'Metodos Numericos para Eq Dif.', 'CUV'], 
              'AOC': ['LP', 'CD', 'Lab de AOC'], 
              'CD': ['AOC', 'Embarcados', 'Lab de CD'], 
              'AR I': ['CUV', 'AR II'], 
              'CUV': ['AR I', 'ED Parciais', 'FA', 'Prob', 'Series e EDO'], 
              'AR II': ['AR I'], 
              'BD': ['AED I', 'PEC'], 
              'CE I': ['CE II', 'Lab de CE'], 
              'CE II': ['CE I', 'FenMag', 'CSD'], 
              'FenMag': ['CE II', 'FenMan Exp', 'Intro aos Materiais Eletricos'], 
              'Compiladores': ['LFA'], 
              'LFA': ['Compiladores', 'MD', 'LP'], 
              'Computacao Grafica': ['AED I'], 
              'CSD': ['CE II', 'Lab de Controle'], 
              'CTS': [], 
              'CTSA': [], 
              'CVV': ['GA', 'Espacos Metricos', 'Intro GD'], 
              'Desenho Tecnico': [], 
              'ED Parciais': ['Series e EDO', 'CUV'], 
              'EDO': ['AL I', 'Series e EDO'], 
              'Elem. De Alg.': [], 
              'Embarcados': ['LP', 'CD'], 
              'Engenharia de Software': ['Prog OO', 'PEC'], 
              'Prog OO': ['Engenharia de Software', 'IHC e UX', 'AED I', 'Proj OO', 'Redes'], 
              'Espacos Metricos': ['CVV', 'AL I'], 
              'FA': ['Series e EDO', 'CUV'], 
              'FBM': [], 
              'FeCont': [], 
              'FenMan Exp': ['FenMag'], 
              'FenMec': ['MecG'], 
              'Fund. De Adm.': [], 
              'Fund. Elet. Aplicada': ['Intro aos Materiais Eletricos'], 
              'Intro aos Materiais Eletricos': ['Fund. Elet. Aplicada', 'FenMag'], 
              'IA': ['AED I'], 
              'IHC e UX': ['Prog OO'], 
              'Inferencia e Analise de Regressao': ['Prob e Estatistica'], 
              'Prob e Estatistica': ['Inferencia e Analise de Regressao', 'Prob'], 
              'Intro a Economi': [], 
              'Intro GD': ['CVV'], 
              'Lab de AOC': ['AOC', 'Lab de CD', 'Lab de Eng. De Sist.'], 
              'Lab de CD': ['Lab de AOC', 'CD'], 
              'Lab de CE': ['CE I'], 
              'Lab de Comp': ['Lab de Eng. De Sist.', 'Lab de SO'], 
              'Lab de Eng. De Sist.': ['Lab de Comp', 'Lab de AOC'], 
              'Lab de Comunic. Dig.': ['Lab de SO'], 
              'Lab de SO': ['Lab de Comunic. Dig.', 'SO', 'Lab de Comp'], 
              'Lab de Controle': ['CSD'], 
              'SO': ['Lab de SO', 'PCD', 'Seguranca da Info', 'AED I'], 
              'MD': ['LFA', 'PAA', 'TNC'], 'MecG': ['FenMec', 'GA'], 
              'Metodos Numericos para Eq Dif.': ['AL I', 'CN', 'Series e EDO'], 
              'Otimizacao Inteira': ['Otimizacao Linear'], 
              'Otimizacao Linear': ['Otimizacao Inteira', 'GA', 'LP'], 
              'Otimizacao nao-linear': ['CN', 'LP'], 
              'PAA': ['MD', 'AED II', 'Teoria dos Grafos'], 
              'PCD': ['SO'], 
              'PEC': ['BD', 'Engenharia de Software', 'TCC I'], 
              'Prob': ['Prob e Estatistica', 'CUV'], 
              'Proj OO': ['Prog OO'], 'QG': [], 
              'Redes': ['Prog OO'], 
              'Seguranca da Info': ['SO'], 
              'TCC I': ['PEC', 'TCC II'], 
              'TCC II': ['TCC I'], 
              'Teoria dos Grafos': ['PAA'], 
              'TNC': ['MD']
              }

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

