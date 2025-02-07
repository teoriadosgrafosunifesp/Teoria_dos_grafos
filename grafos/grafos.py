
from collections import defaultdict, deque
import random

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

# 8) Dado um vértice, retorne, se existir, um ciclo no qual ele se situe
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


def calcular_graus(grafo):
    graus = {no: len(vizinhos) for no, vizinhos in grafo.items()}
    maior_grau = max(graus.values())
    menor_grau = min(graus.values())
    return maior_grau, menor_grau

def verificar_subgrafo(grafo, subgrafo):
    for no, vizinhos in subgrafo.items():
        if no not in grafo:
            return False
        for vizinho in vizinhos:
            if vizinho not in grafo[no]:
                return False
    return True

def prim_mst(graph, vertices):
    """Gera uma árvore de abrangência mínima (MST) usando o algoritmo de Prim sem considerar pesos."""
    mst = []
    visited = set([vertices[0]])
    edges = [(u, v) for u, adj in graph.items() for v in adj if u in visited and v not in visited]
    
    while len(visited) < len(vertices):
        edges.sort(key=lambda x: (x[0], x[1]))  # Ordena as arestas (sem peso)
        for u, v in edges:
            if v not in visited:
                mst.append((u, v))
                visited.add(v)
                edges.extend([(v, w) for w in graph[v] if w not in visited])
                break
    
    return mst

def get_fundamental_cycle(tree, new_edge):
    """Encontra o ciclo fundamental formado ao adicionar uma aresta a uma árvore."""
    u, v = new_edge
    parent = {u: None}
    stack = [u]
    
    while stack:
        node = stack.pop()
        for adj in tree.get(node, {}):
            if adj not in parent:
                parent[adj] = node
                stack.append(adj)
                if adj == v:
                    break
    
    if v not in parent:
        return []  # Retorna um ciclo vazio se não encontrar um caminho válido
    
    cycle = []
    while v is not None:
        cycle.append((parent[v], v))
        v = parent[v]
    
    return cycle[1:]

def generate_spanning_trees(graph, vertices, k):
    """Gera uma árvore de abrangência e encontra k outras árvores por trocas cíclicas."""
    tree_edges = prim_mst(graph, vertices)
    tree = {u: set() for u in vertices}
    for u, v in tree_edges:
        tree[u].add(v)
        tree[v].add(u)
    
    trees = [tree.copy()]
    all_edges = [(u, v) for u in graph for v in graph[u] if u < v]
    
    for _ in range(k):
        non_tree_edges = [e for e in all_edges if e[:2] not in [(x, y) for x in tree for y in tree[x]]]
        if not non_tree_edges:
            break
        
        new_edge = random.choice(non_tree_edges)
        cycle = get_fundamental_cycle(tree, new_edge)
        
        removable_edges = [e for e in cycle if e != new_edge]
        if removable_edges:
            remove_edge = random.choice(removable_edges)
            if remove_edge[0] in tree and remove_edge[1] in tree[remove_edge[0]]:
                tree[remove_edge[0]].remove(remove_edge[1])
            if remove_edge[1] in tree and remove_edge[0] in tree[remove_edge[1]]:
                tree[remove_edge[1]].remove(remove_edge[0])
            
            tree[new_edge[0]].add(new_edge[1])
            tree[new_edge[1]].add(new_edge[0])
            trees.append(tree.copy())
    
    return trees


def calcular_distancia_arvores(A1, A2):
    # Inicializa o contador de distância
    distancia = 0
    
    # Verifica arestas em A1 que não estão em A2
    for aresta in A1:
        # Considera arestas não direcionadas, ou seja, (u, v) é igual a (v, u)
        if aresta not in A2 and (aresta[1], aresta[0]) not in A2:
            distancia += 1
    
    # Verifica arestas em A2 que não estão em A1
    for aresta in A2:
        # Considera arestas não direcionadas, ou seja, (u, v) é igual a (v, u)
        if aresta not in A1 and (aresta[1], aresta[0]) not in A1:
            distancia += 1
    
    return distancia


def bfs(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        
        for neighbor in graph[node]:
            if distances[neighbor] == float('inf'):  # Se o nó não foi visitado
                distances[neighbor] = distances[node] + 1
                queue.append(neighbor)
    
    return distances

# Função para encontrar o nó central
def find_center(graph):
    # Calcula as distâncias de cada nó
    max_distances = {}
    for node in graph:
        distances = bfs(graph, node)
        max_distances[node] = max(distances.values())  # Maior distância até qualquer outro nó
    
    # O nó central será aquele com a menor maior distância
    center = min(max_distances, key=max_distances.get)
    
    return center

# Função para construir a árvore geradora central a partir do nó central
def build_central_tree(graph, center):
    distances = bfs(graph, center)
    tree = defaultdict(list)
    
    # Para reconstruir a árvore, rastreia os pais a partir das distâncias
    for node in graph:
        if node != center:
            for neighbor in graph[node]:
                if distances[neighbor] == distances[node] - 1:
                    tree[node].append(neighbor)
                    tree[neighbor].append(node)
    
    return tree

def find_center_tree(graph):
    # Encontrar o nó central
    center = find_center(graph)

    # Construir a árvore geradora central a partir do nó central
    central_tree = build_central_tree(graph, center)
    return center, central_tree

# Função para verificar se o grafo é conexo
def is_connected(graph, n):
    visited = [False] * n
    
    def dfs(v):
        visited[v] = True
        for neighbor in graph[v]:
            if not visited[neighbor]:
                dfs(neighbor)
    
    # Iniciar DFS a partir do primeiro vértice (supondo que o grafo tenha pelo menos um vértice)
    dfs(0)
    
    return all(visited)

# Função para verificar o grau de cada vértice
def check_degrees(graph, n):
    odd_degree_vertices = 0
    for i in range(n):
        if len(graph[i]) % 2 != 0:
            odd_degree_vertices += 1
    return odd_degree_vertices

# Função para verificar se o grafo tem caminho ou circuito euleriano
def eulerian_path_or_cycle(G):
    # Obter a lista de adjacência do grafo
    graph = {k: list(v) for k, v in G.adjacency()}  # Converte o formato para lista de adjacência
    
    # Número de vértices
    n = len(G.nodes)
    
    if not is_connected(graph, n):
        return "Não é conexo, não há caminho ou circuito euleriano."
    
    odd_degree_count = check_degrees(graph, n)
    
    if odd_degree_count == 0:
        return "O grafo possui um circuito euleriano."
    elif odd_degree_count == 2:
        return "O grafo possui um caminho euleriano."
    else:
        return "O grafo não possui caminho ou circuito euleriano."
