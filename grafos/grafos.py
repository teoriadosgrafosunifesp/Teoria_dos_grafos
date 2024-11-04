def gerar_matriz_adjacencia(grafo):
    # Extrai os vértices do grafo
    vertices = list(grafo.keys())
    n = len(vertices)
    
    # Inicializa a matriz de adjacência com zeros
    matriz_adjacencia = [[0] * n for _ in range(n)]
    
    # Cria um mapeamento entre vértices e índices
    indice_vertice = {vertice: i for i, vertice in enumerate(vertices)}
    
    # Preenche a matriz com base nas arestas
    for vertice, vizinhos in grafo.items():
        i = indice_vertice[vertice]
        for vizinho in vizinhos:
            j = indice_vertice[vizinho]
            matriz_adjacencia[i][j] = 1
    
    return matriz_adjacencia


def gerar_grafo_a_partir_matriz(matriz_adjacencia):
    # Número de vértices no grafo
    n = len(matriz_adjacencia)
    
    # Inicializa o grafo como um dicionário vazio
    grafo = {i: [] for i in range(n)}
    
    # Preenche o grafo com as conexões indicadas pela matriz
    for i in range(n):
        for j in range(n):
            if matriz_adjacencia[i][j] == 1:
                grafo[i].append(j)
    
    return grafo


def gerar_matriz_incidencia(grafo):
    # Lista de vértices e arestas únicas
    vertices = list(grafo.keys())
    arestas = []
    
    # Gera a lista de arestas (apenas uma direção para cada par de vértices)
    for v1 in grafo:
        for v2 in grafo[v1]:
            if (v2, v1) not in arestas:
                arestas.append((v1, v2))
    
    # Inicializa a matriz de incidência com zeros
    n = len(vertices)
    m = len(arestas)
    matriz_incidencia = [[0] * m for _ in range(n)]
    
    # Cria um mapeamento de vértices para índices
    indice_vertice = {vertice: i for i, vertice in enumerate(vertices)}
    
    # Preenche a matriz de incidência
    for j, (v1, v2) in enumerate(arestas):
        i1 = indice_vertice[v1]
        i2 = indice_vertice[v2]
        matriz_incidencia[i1][j] = 1
        matriz_incidencia[i2][j] = 1
    
    return matriz_incidencia


def gerar_grafo_a_partir_matriz_incidencia(matriz_incidencia):
    # Número de vértices e arestas
    n = len(matriz_incidencia)
    m = len(matriz_incidencia[0])
    
    # Inicializa o grafo como um dicionário vazio
    grafo = {i: [] for i in range(n)}
    
    # Percorre cada coluna (aresta) da matriz
    for j in range(m):
        # Encontra os vértices que estão conectados pela aresta `j`
        vertices_conectados = [i for i in range(n) if matriz_incidencia[i][j] == 1]
        
        # Se a aresta conecta dois vértices, adiciona a conexão entre eles
        if len(vertices_conectados) == 2:
            v1, v2 = vertices_conectados
            grafo[v1].append(v2)
            grafo[v2].append(v1)
    
    return grafo


def gerar_lista_adjacencia(grafo):
    # Inicializa a lista de adjacência
    lista_adjacencia = {}
    
    # Adiciona cada vértice e suas conexões
    for vertice, vizinhos in grafo.items():
        lista_adjacencia[vertice] = vizinhos[:]
    
    return lista_adjacencia


def gerar_grafo_a_partir_lista(lista_adjacencia):
    # Inicializa o grafo como um dicionário vazio
    grafo = {}
    
    # Copia a lista de adjacência para o grafo
    for vertice, vizinhos in lista_adjacencia.items():
        grafo[vertice] = vizinhos[:]
    
    return grafo

