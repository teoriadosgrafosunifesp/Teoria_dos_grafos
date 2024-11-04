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


# Funções para manipulação geral de grafos em diferentes representações

# 1) O número de vértices de um grafo
def numero_vertices(grafo):
    return len(grafo)

# 2) O número de arestas de um grafo
def numero_arestas_lista_adjacencia(grafo):
    return sum(len(vizinhos) for vizinhos in grafo.values()) // 2

def numero_arestas_matriz_adjacencia(matriz_adjacencia):
    return sum(sum(row) for row in matriz_adjacencia) // 2

def numero_arestas_matriz_incidencia(matriz_incidencia):
    return len(matriz_incidencia[0])

# 3) Dado um vértice específico, forneça seus vértices adjacentes
def vertices_adjacentes(grafo, vertice):
    return grafo.get(vertice, [])

# 4) Dados dois vértices, retorne se existe uma aresta que os une
def existe_aresta_lista_adjacencia(grafo, v1, v2):
    return v2 in grafo.get(v1, [])

def existe_aresta_matriz_adjacencia(matriz_adjacencia, v1, v2):
    return matriz_adjacencia[v1][v2] == 1

def existe_aresta_matriz_incidencia(matriz_incidencia, v1, v2):
    for j in range(len(matriz_incidencia[0])):
        if matriz_incidencia[v1][j] == 1 and matriz_incidencia[v2][j] == 1:
            return True
    return False

# 5) Dado um vértice, o seu grau
def grau_vertice_lista_adjacencia(grafo, vertice):
    return len(grafo.get(vertice, []))

def grau_vertice_matriz_adjacencia(matriz_adjacencia, vertice):
    return sum(matriz_adjacencia[vertice])

# 6) Dado um grafo, o grau associado a cada vértice
def graus_grafo_lista_adjacencia(grafo):
    return {vertice: len(vizinhos) for vertice, vizinhos in grafo.items()}

def graus_grafo_matriz_adjacencia(matriz_adjacencia):
    return {i: sum(row) for i, row in enumerate(matriz_adjacencia)}

# 7) Dado dois vértices específicos, retorne um caminho simples entre eles (usando DFS)
def caminho_dfs(grafo, inicio, destino, caminho=None):
    if caminho is None:
        caminho = []
    caminho = caminho + [inicio]
    
    if inicio == destino:
        return caminho
    if inicio not in grafo:
        return None
    
    for vizinho in grafo[inicio]:
        if vizinho not in caminho:
            novo_caminho = caminho_dfs(grafo, vizinho, destino, caminho)
            if novo_caminho:
                return novo_caminho
    return None

# 8) Dado um vértice, retorne, se existir, um ciclo no qual ele se situe (usando DFS)
def encontrar_ciclo(grafo, vertice, visitado=None, caminho=None):
    if visitado is None:
        visitado = set()
    if caminho is None:
        caminho = []
    
    visitado.add(vertice)
    caminho.append(vertice)
    
    for vizinho in grafo[vertice]:
        if vizinho in caminho and vizinho != caminho[-2]:
            return caminho + [vizinho]
        if vizinho not in visitado:
            ciclo = encontrar_ciclo(grafo, vizinho, visitado, caminho)
            if ciclo:
                return ciclo
    
    caminho.pop()
    return None

# 9) Verificar se G' é subgrafo de G ou vice-versa
def eh_subgrafo(grafo1, grafo2):
    # Verifica se todos os vértices e arestas de grafo1 estão em grafo2
    for vertice in grafo1:
        if vertice not in grafo2:
            return False
        for vizinho in grafo1[vertice]:
            if vizinho not in grafo2[vertice]:
                return False
    return True

def subgrafo_ou_vice_versa(grafo1, grafo2):
    if eh_subgrafo(grafo1, grafo2):
        return "Grafo1 é subgrafo de Grafo2"
    elif eh_subgrafo(grafo2, grafo1):
        return "Grafo2 é subgrafo de Grafo1"
    else:
        return "Nenhum é subgrafo do outro"
