
import networkx as nx
import matplotlib.pyplot as plt
import random
from collections import defaultdict, deque
import itertools
import copy
import collections

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


def isGrafo(entrada):
    # Verifica se a entrada é um dicionário
    if not isinstance(entrada, dict):
        return False
    
    # Itera sobre cada nó e suas conexões
    for no, conexoes in entrada.items():
        # Verifica se cada conexão está em uma lista ou conjunto
        if not isinstance(conexoes, (list, set)):
            return False
        
        # Verifica a simetria das conexões para um grafo não direcionado
        for conexao in conexoes:
            # Verifica se o nó atual está na lista de conexões do nó conectado
            if no not in entrada.get(conexao, []):
                return False
    
    # Se todas as verificações passarem, é um grafo
    return True


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
    
    # Para cada vértice, extrai as chaves dos vizinhos (adjacências)
    for vertice, vizinhos in grafo.items():
        lista_adjacencia[vertice] = list(vizinhos.keys())
    
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

# Função auxiliar para converter lista de adjacência em conjunto de arestas
def obter_arestas(grafo):
    arestas = set()
    for vertice, vizinhos in grafo.items():
        for vizinho in vizinhos:
            # Adiciona a aresta de maneira ordenada para evitar duplicatas
            arestas.add(tuple(sorted((vertice, vizinho))))
    return arestas

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

def caminho_bfs(grafo, inicio, destino):
    # Lista para rastrear caminhos, cada elemento é uma lista representando um caminho parcial
    fila = [[inicio]]
    
    # Conjunto para rastrear os nós visitados
    visitados = set()
    
    while fila:
        # Retira o primeiro caminho da lista
        caminho = fila.pop(0)
        
        # Obtém o último nó do caminho atual
        no_atual = caminho[-1]
        
        # Verifica se o nó destino foi alcançado
        if no_atual == destino:
            return caminho
        
        # Verifica os vizinhos do nó atual
        for vizinho in grafo.get(no_atual, []):
            if vizinho not in visitados:
                # Marca o vizinho como visitado
                visitados.add(vizinho)
                
                # Cria um novo caminho e adiciona à fila
                novo_caminho = caminho + [vizinho]
                fila.append(novo_caminho)
    
    # Retorna None se não houver caminho entre inicio e destino
    return None


# 8) Dado um vértice, retorne, se existir um ciclo no qual ele se situe (usando DFS)
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
    # Verifica se G' é grafo
    if not(isGrafo(grafo2)):
        return False
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

def busca_destinos(grafo, inicio, destinos):
    # Realiza uma cópia dos destinos para não modificar a lista original
    destinos_restantes = set(destinos)
    caminho = []
    
    def procura(v):
        # Adiciona o vértice atual ao caminho e remove-o dos destinos restantes se for um destino
        caminho.append(v)
        if v in destinos_restantes:
            destinos_restantes.remove(v)
        
        # Para a busca se todos os destinos foram encontrados
        if not destinos_restantes:
            return True
        
        # Continua a busca para os vizinhos
        for vizinho in grafo.get(v, []):
            if vizinho not in caminho:
                if procura(vizinho):
                    return True
        return False
    
    # Inicia a DFS a partir do vértice inicial
    procura(inicio)
    
    # Verifica se ainda há destinos não encontrados
    if destinos_restantes:
        print("Destinos não alcançados:", destinos_restantes)
    
    return caminho if not destinos_restantes else caminho, destinos_restantes

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

def eh_arvore(lista_adjacencia):
    """
    Verifica se um grafo representado por lista de adjacência é uma árvore.

    Parâmetros:
      - lista_adjacencia: Dicionário de adjacência representando o grafo.

    Retorna:
      - True se o grafo for uma árvore, False caso contrário.
    """
    # Contagem de vértices e arestas
    count_vertices = len(lista_adjacencia)
    count_arestas = sum(len(vizinhos) for vizinhos in lista_adjacencia.values()) // 2  # Arestas são bidirecionais

    # Primeira condição: |E| == |V| - 1
    if count_arestas != count_vertices - 1:
        return False

    # Conjunto para armazenar os vértices visitados
    visitados = set()

    # Função recursiva para DFS
    def dfs(vertice, pai):
        visitados.add(vertice)
        for vizinho in lista_adjacencia[vertice]:
            if vizinho not in visitados:
                if not dfs(vizinho, vertice):  # Chamada recursiva
                    return False
            elif vizinho != pai:  # Encontramos um ciclo
                return False
        return True

    # Pegamos um vértice arbitrário para iniciar a DFS
    primeiro_vertice = next(iter(lista_adjacencia))

    # Segunda condição: Deve ser conexo e não ter ciclos
    if not dfs(primeiro_vertice, None):
        return False

    # Terceira condição: Todos os vértices devem ser alcançados (grafo conexo)
    if len(visitados) != count_vertices:
        return False

    return True

def spanning_tree(graph, vertices):
    """
    Gera uma árvore de abrangência (qualquer uma) a partir do grafo,
    usando uma DFS a partir do primeiro vértice da lista.
    A árvore é representada como um conjunto de arestas, onde cada aresta é um frozenset com 2 vértices.
    """
    T = set()
    visited = set()
    
    def dfs(u):
        visited.add(u)
        for v in graph[u]:
            if v not in visited:
                # Adiciona a aresta de forma não direcionada (ordem irrelevante)
                T.add(frozenset({u, v}))
                dfs(v)
                
    dfs(vertices[0])
    return T

def get_path_edges(T, start, end):
    """
    Dado T (um conjunto de arestas que forma uma árvore) e dois vértices start e end,
    encontra o caminho único entre eles. Retorna a lista de arestas (cada uma um frozenset)
    que compõem esse caminho.
    """
    # Constrói a lista de adjacência para a árvore T.
    adj = {}
    for edge in T:
        for node in edge:
            if node not in adj:
                adj[node] = set()
        a, b = tuple(edge)
        adj[a].add(b)
        adj[b].add(a)
    
    # Busca em profundidade para encontrar o caminho de start até end.
    visited = set([start])
    parent = {start: None}
    stack = [start]
    found = False
    
    while stack:
        current = stack.pop()
        if current == end:
            found = True
            break
        for neighbor in adj.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                stack.append(neighbor)
                
    if not found:
        return None  # Em uma árvore, isso não deve ocorrer.
    
    # Reconstrói o caminho (lista de arestas) a partir dos ponteiros parent.
    path_edges = []
    cur = end
    while parent[cur] is not None:
        p = parent[cur]
        path_edges.append(frozenset({cur, p}))
        cur = p
    return path_edges

def generate_all_spanning_trees(graph):
    """
    A partir de um grafo (lista de adjacência representada por um dicionário: vértice -> lista de vizinhos),
    gera todas as árvores de abrangência do grafo usando a técnica de troca cíclica.
    
    Retorna uma lista de árvores, onde cada árvore é representada também por uma lista de adjacência
    (neste caso, um dicionário: vértice -> lista ordenada de vizinhos).
    """
    # Constrói o conjunto total de arestas do grafo.
    E = set()
    for u in graph:
        for v in graph[u]:
            E.add(frozenset({u, v}))
    
    vertices = list(graph.keys())
    # Obtém uma árvore de abrangência inicial (por exemplo, usando DFS).
    T0 = spanning_tree(graph, vertices)
    
    # Usaremos um conjunto para armazenar as árvores já geradas, utilizando sua representação canônica.
    all_trees = set()  # Cada árvore será representada como frozenset de arestas.
    result_trees = []   # Aqui armazenamos cada árvore como um conjunto (T: set de frozensets).
    
    def dfs_spanning(T):
        canon = frozenset(T)  # Representação imutável da árvore T.
        if canon in all_trees:
            return
        all_trees.add(canon)
        result_trees.append(T.copy())
        
        # Para cada aresta que está no grafo mas não em T, tenta-se realizar a troca cíclica.
        non_tree_edges = E - T
        for e in non_tree_edges:
            # Desempacota os dois vértices da aresta e.
            u, v = tuple(e)
            # Encontra o caminho único entre u e v em T.
            path_edges = get_path_edges(T, u, v)
            if path_edges is None:
                continue
            # O ciclo fundamental é composto pelo caminho encontrado + a aresta e.
            cycle_edges = set(path_edges)
            cycle_edges.add(e)

            # gera uma nova árvore T_new = T ∪ {e} - {f}.
            for f in cycle_edges:
                if f == e:
                    continue
                T_new = T.copy()
                T_new.remove(f)
                T_new.add(e)
                dfs_spanning(T_new)
    
    dfs_spanning(T0)
    
    # Converte cada árvore (representada como conjunto de arestas) para lista de adjacência.
    trees_adj_list = []
    for T in result_trees:
        adj = {v: set() for v in vertices}
        for edge in T:
            a, b = tuple(edge)
            adj[a].add(b)
            adj[b].add(a)
        # Converte os conjuntos de vizinhos para listas ordenadas.
        adj_list = {v: sorted(list(neigh)) for v, neigh in adj.items()}
        trees_adj_list.append(adj_list)
        
    return trees_adj_list

def gerar_arvore_abrangencia(grafo, inicio):
    """
    Gera uma árvore de abrangência a partir de um nó inicial usando DFS.
    """
    arvore = []
    visitado = set()
    
    def dfs(no, pai):
        visitado.add(no)
        for vizinho in grafo[no]:
            if vizinho not in visitado:
                arvore.append((no, vizinho))
                dfs(vizinho, no)
    
    dfs(inicio, None)
    
    # Retorna como conjunto de arestas para facilitar comparações
    return set(arvore)

def gerar_arvore_abrangencia_lista_adjacencia(grafo, inicio):
    """
    Gera uma árvore de abrangência a partir de um nó inicial usando DFS.
    Retorna a árvore como uma lista de adjacência.
    
    Parâmetros:
      - grafo: Dicionário de adjacência representando o grafo original.
      - inicio: Vértice de onde a busca começará.
      
    Retorna:
      - Uma lista de adjacência representando a árvore de abrangência.
    """
    arvore = {no: set() for no in grafo}  # Inicializa a lista de adjacência
    visitado = set()

    def dfs(no):
        visitado.add(no)
        for vizinho in grafo[no]:
            if vizinho not in visitado:
                arvore[no].add(vizinho)  # Adiciona a conexão na árvore
                arvore[vizinho].add(no)  # Como é uma árvore, a relação é bidirecional
                dfs(vizinho)

    dfs(inicio)

    # Removendo os nós sem conexões (para deixar apenas a estrutura da árvore)
    arvore = {no: vizinhos for no, vizinhos in arvore.items() if vizinhos}

    return arvore

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

def soma_simetrica(grafo1, grafo2):
    # Obtém as arestas de cada grafo
    arestas_g1 = obter_arestas(grafo1)
    arestas_g2 = obter_arestas(grafo2)

    # Calcula a soma simétrica entre os conjuntos de arestas
    soma_simetrica = arestas_g1.symmetric_difference(arestas_g2)

    return soma_simetrica

def distancia_por_soma(T1, T2):
    # Aqui esperamos que T1 e T2 sejam conjuntos de arestas (frozenset)
    # Por exemplo, cada aresta é representada por frozenset({u, v})
    # A soma simétrica entre dois conjuntos é: A ^ B
    diff = T1 ^ T2
    return len(diff)  # Se cada aresta é única, não precisa dividir por 2

def convert_adjlist_to_edge_set(adj_list):
    """
    Converte uma árvore representada como lista de adjacência (dicionário)
    para um conjunto de arestas, onde cada aresta é um frozenset({u, v}).
    """
    edge_set = set()
    for u, vizinhos in adj_list.items():
        for v in vizinhos:
            # Usamos frozenset para garantir que a aresta {u, v} seja única
            edge_set.add(frozenset({u, v}))
    return edge_set

def encontrar_arvore_central(grafo):
    """
    Encontra a árvore central do grafo.
    O grafo é fornecido como lista de adjacência (dicionário: vértice -> lista de vizinhos).
    Retorna (indice_central, arvore_central) onde:
      - indice_central é o índice da árvore central na lista de árvores geradas;
      - arvore_central é a árvore central no formato de lista de adjacência.
    """
    # Gera todas as árvores de abrangência
    arvores = generate_all_spanning_trees(grafo)
    n = len(arvores)
    
    # Converte cada árvore para conjunto de arestas
    arvores_edge_set = [convert_adjlist_to_edge_set(T) for T in arvores]
    
    # Calcula as distâncias entre as árvores (indexadas de 0 a n-1)
    distancias = {i: {} for i in range(n)}
    for i, j in itertools.combinations(range(n), 2):
        d = distancia_por_soma(arvores_edge_set[i], arvores_edge_set[j])
        distancias[i][j] = d
        distancias[j][i] = d
    
    # Para cada árvore, calcula a distância máxima em relação às demais (excentricidade)
    max_distancias = {}
    for i in range(n):
        # Se n == 1, a árvore única terá excentricidade 0
        max_distancias[i] = max(distancias[i].values()) if distancias[i] else 0
    
    # A árvore central é aquela que minimiza a distância máxima
    indice_central = min(max_distancias, key=max_distancias.get)
    
    return indice_central, arvores[indice_central]

def obter_lista_adjacencia_arvore_central(grafo):
    """
    Converte a árvore central encontrada em uma lista de adjacência.

    Parâmetros:
        arvore_central (list of tuple): Lista de arestas representando a árvore central.

    Retorno:
        dict: Lista de adjacência da árvore central.
    """
    arvore_central = encontrar_arvore_central(grafo)[1]
    lista_adjacencia = {}

    for u, v in arvore_central:
        if u not in lista_adjacencia:
            lista_adjacencia[u] = []
        if v not in lista_adjacencia:
            lista_adjacencia[v] = []

        # Adiciona as conexões (grafo não direcionado)
        lista_adjacencia[u].append(v)
        lista_adjacencia[v].append(u)

    return lista_adjacencia

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
def is_connected(lista_adjacencia):
    """
    Verifica se um grafo representado por lista de adjacência é conectado.
    Retorna True se for conectado e False caso contrário.
    """
    if not lista_adjacencia:
        return False  # Grafo vazio não é conectado
    
    # Pegamos um vértice qualquer para iniciar a DFS
    vertice_inicial = next(iter(lista_adjacencia))  
    visitados = set()
    
    # Função auxiliar de DFS
    def dfs(v):
        visitados.add(v)
        for vizinho in lista_adjacencia.get(v, []):
            if vizinho not in visitados:
                dfs(vizinho)

    # Inicia a busca em profundidade
    dfs(vertice_inicial)
    
    # Se todos os vértices foram visitados, o grafo é conectado
    return len(visitados) == len(lista_adjacencia)

# Função para verificar o grau de cada vértice
def check_degrees(graph, n):
    odd_degree_vertices = 0
    for i in range(n):
        if len(graph[i]) % 2 != 0:
            odd_degree_vertices += 1
    return odd_degree_vertices

def eh_euleriano(G):
    lista_adjacencia = {k: list(v) for k, v in G.adjacency()}
    """ Verifica se um grafo é Euleriano e retorna o circuito Euleriano caso exista. """
    if not(is_connected(lista_adjacencia)):
        return False, None
    
    G = nx.Graph(lista_adjacencia)
    
    # Verifica se todos os vértices têm grau par
    if all(G.degree(v) % 2 == 0 for v in G.nodes) and nx.is_connected(G):
        circuito = list(nx.eulerian_circuit(G))
        # Cria a lista de adjacência apenas com o circuito Euleriano
        circuito_lista = {v: [] for v in G.nodes}
        for u, v in circuito:
            circuito_lista[u].append(v)
            circuito_lista[v].append(u)
        return True, circuito_lista
    return False, None


def eh_hamiltoniano(G):
    lista_adjacencia = {k: list(v) for k, v in G.adjacency()}
    """ Verifica se um grafo é Hamiltoniano e retorna o circuito Hamiltoniano caso exista. """
    if not(is_connected(lista_adjacencia)):
        return False, None
    G = nx.Graph(lista_adjacencia)
    n = len(G.nodes)
    
    # Verificação dos teoremas de Dirac e Ore (condições suficientes, mas não necessárias)
    if all(G.degree(v) >= n / 2 for v in G.nodes) or all(G.degree(u) + G.degree(v) >= n for u, v in nx.non_edges(G)):
        # Usa o algoritmo de busca por ciclo Hamiltoniano (Heurístico)
        ciclo_hamiltoniano = nx.approximation.traveling_salesman_problem(G, cycle=True)
        
        # Cria a lista de adjacência apenas com o circuito Hamiltoniano encontrado
        hamilton_lista = {v: [] for v in G.nodes}
        for i in range(len(ciclo_hamiltoniano) - 1):
            u, v = ciclo_hamiltoniano[i], ciclo_hamiltoniano[i + 1]
            hamilton_lista[u].append(v)
            hamilton_lista[v].append(u)
        return True, hamilton_lista
    return False, None

# Função para verificar se o grafo tem caminho ou circuito euleriano
def eulerian_path_or_cycle(G):
    # Obter a lista de adjacência do grafo
    graph = {k: list(v) for k, v in G.adjacency()}  # Converte o formato para lista de adjacência
    
    # Número de vértices
    n = len(G.nodes)
    
    if not is_connected(graph):
        return "Não é conexo, não há caminho ou circuito euleriano."
    
    odd_degree_count = check_degrees(graph, n)
    
    if odd_degree_count == 0:
        return "O grafo possui um circuito euleriano."
    elif odd_degree_count == 2:
        return "O grafo possui um caminho euleriano."
    else:
        return "O grafo não possui caminho ou circuito euleriano."

#----------------------- Plot grafos
def plotar_subgrafo(grafo, n):
    # Verifica se o número de nós no grafo é menor que 'n'
    total_nos = len(grafo.nodes)
    if total_nos <= n:
        # Se o grafo já tem 'n' nós ou menos, plote o grafo completo
        subgrafo = grafo
    else:
        # Seleciona um nó inicial aleatório
        no_inicial = random.choice(list(grafo.nodes))
        
        # Usa uma busca em largura para obter até 'n' nós conectados a partir do nó inicial
        sub_nos = set([no_inicial])
        for vizinho in nx.bfs_edges(grafo, no_inicial):
            sub_nos.update(vizinho)
            if len(sub_nos) >= n:
                break
        
        # Cria o subgrafo a partir dos nós selecionados
        subgrafo = grafo.subgraph(sub_nos)
    
    # Plota o subgrafo
    plt.figure(figsize=(8, 6))
    nx.draw(subgrafo, with_labels=True, node_size=500, font_size=10, font_color="black")
    plt.title(f"Subgrafo com até {n} nós")
    plt.show()

def grafo_para_lista_adjacencia(G):
    # Inicializa o dicionário para armazenar a lista de adjacência
    lista_adjacencia = {}
    
    # Itera sobre cada nó no grafo
    for vertice in G.nodes():
        # Obtém os vizinhos (vértices adjacentes) de cada vértice
        adjacentes = list(G.neighbors(vertice))
        
        # Adiciona o vértice e sua lista de adjacentes ao dicionário
        lista_adjacencia[vertice] = adjacentes
    
    return lista_adjacencia

def plotar_nos_maior_grau(G):
    # Calcula o grau de cada nó e encontra o grau máximo
    graus = dict(G.degree())
    grau_maximo = max(graus.values())
    
    # Filtra os nós que têm o grau máximo
    nos_maior_grau = [n for n, grau in graus.items() if grau == grau_maximo]
    
    # Destaca o grafo e os nós com o maior grau
    plt.figure(figsize=(12, 12))
    pos = nx.spring_layout(G, k=0.6, iterations=50)  # Ajuste k para controlar o espaçamento
    
    # Desenha o grafo
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, edge_color='gray')
    
    # Destaca os nós com o maior grau
    nx.draw_networkx_nodes(G, pos, nodelist=nos_maior_grau, node_color='orange', node_size=700)
    
    plt.title(f"Nó(s) com Maior Grau ({grau_maximo})")
    plt.show()

# Função para encontrar e plotar o(s) nó(s) com menor grau
def plotar_nos_menor_grau(G):
    # Calcula o grau de cada nó e encontra o grau mínimo
    graus = dict(G.degree())
    grau_minimo = min(graus.values())
    
    # Filtra os nós que têm o grau mínimo
    nos_menor_grau = [n for n, grau in graus.items() if grau == grau_minimo]
    
    # Destaca o grafo e os nós com o menor grau
    plt.figure(figsize=(12, 12))
    pos = nx.spring_layout(G, k=0.6, iterations=50)  # Ajuste k para controlar o espaçamento
    
    # Desenha o grafo
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, edge_color='gray')
    
    # Destaca os nós com o menor grau
    nx.draw_networkx_nodes(G, pos, nodelist=nos_menor_grau, node_color='red', node_size=700)
    
    plt.title(f"Nó(s) com Menor Grau ({grau_minimo})")
    plt.show()

def plot_nx_grafo(G):
    # Visualiza o grafo
    pos = nx.spring_layout(G, k=0.6, iterations=80)  # Ajuste k para controlar o espaçamento

    # Plotando o grafo
    plt.figure(figsize=(12, 12))  # Aumenta o tamanho da figura
    nx.draw(G, pos, with_labels=True, node_size=500, font_size=10, font_weight='bold', node_color="skyblue", edge_color="gray")
    plt.title("Grafo com Nós Mais Espaçados")
    plt.show()
    return

def plotar_no_com_vizinhos(grafo, no):
    # Cria um grafo vazio para o subgrafo
    subgrafo = nx.Graph()
    
    # Adiciona o nó selecionado e seus vizinhos
    subgrafo.add_node(no)  # Adiciona o nó selecionado
    for vizinho in grafo[no]:  # Adiciona cada vizinho e a aresta entre eles
        subgrafo.add_edge(no, vizinho)
    
    # Desenha o subgrafo com o nó e seus vizinhos
    plt.figure(figsize=(5, 5))
    nx.draw(subgrafo, with_labels=True, node_size=500, font_size=12, font_color="black", node_color="skyblue")
    plt.show()

def adj_list_to_nx(lista_adjacencia):
    G = nx.Graph()

    # Adiciona vértices e arestas
    for vertice, vizinhos in lista_adjacencia.items():
        for vizinho in vizinhos:
            G.add_edge(vertice, vizinho)

    return G

def plotar_lista_adj(lista_adjacencia, k, iter):
    """
    Plota um grafo a partir de uma lista de adjacência.
    
    Parâmetros:
        lista_adjacencia (dict): Dicionário representando o grafo, onde as chaves são os vértices
                                 e os valores são listas de vértices adjacentes.
    """
    G = adj_list_to_nx(lista_adjacencia)

    # Desenha o grafo
    plt.figure(figsize=(12, 9))
    pos = nx.spring_layout(G, k=k, iterations=iter)  # Ajusta a dispersão dos nós
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=1000, font_size=10, font_weight='bold')

    plt.title("Representação do Grafo a partir da Lista de Adjacência")
    plt.show()

def plotar_grafo_com_graus(grafo):
    # Calcula os graus de cada nó
    graus = dict(grafo.degree())
    
    # Define a posição dos nós no gráfico
    pos = nx.spring_layout(grafo, k=0.7, iterations=50)  # Ajuste k para controlar o espaçamento
    
    # Desenha o grafo
    plt.figure(figsize=(8, 8))
    nx.draw(grafo, pos, with_labels=True, node_size=500, font_size=12, font_color="skyblue", node_color="skyblue")
    
    # Adiciona o grau ao lado de cada nó
    labels = {no: f"{no} ({grau})" for no, grau in graus.items()}
    nx.draw_networkx_labels(grafo, pos, labels=labels, font_size=10, font_color="black")
    
    plt.show()

def plotar_subgrafo_lista(grafo, vertices):
        # Cria um subgrafo contendo apenas os vértices e as arestas entre eles
    subgrafo = grafo.subgraph(vertices)
    
    # Configura o plot do subgrafo
    plt.figure(figsize=(12, 12))

    # Define a posição dos nós no gráfico
    pos = nx.spring_layout(grafo, k=0.7, iterations=80)  # Ajuste k para controlar o espaçamento
    
    # Desenha o subgrafo
    nx.draw(subgrafo, pos, with_labels=True, node_size=500, font_size=10, font_color="black", node_color="skyblue")
    nx.draw_networkx_edges(subgrafo, pos, width=1.5)
    
    # Exibe o plot
    plt.title("Subgrafo com vértices selecionados")
    plt.show()

def edges_to_dict(edges):
    """
    Converte uma lista de arestas (tuplas) em um dicionário de adjacência.
    Cada vértice é uma chave, e o valor é um dicionário com os seus vizinhos.
    Como o grafo é não direcionado, cada aresta é inserida em ambas as direções.
    """
    graph = {}
    for u, v in edges:
        if u not in graph:
            graph[u] = {}
        if v not in graph:
            graph[v] = {}
        # Insere a aresta nas duas direções
        graph[u][v] = {}
        graph[v][u] = {}
    return graph

def obter_componente(T, inicio, aresta_bloqueada):
    """
    Executa uma busca em profundidade (DFS) em T a partir do vértice 'inicio',
    ignorando a aresta 'aresta_bloqueada' (considerada com ordem canônica).
    Retorna o conjunto de vértices atingíveis (a componente conexa que contém 'inicio').
    """
    aresta_bloqueada = tuple(sorted(aresta_bloqueada))
    visitados = set()
    pilha = [inicio]
    
    while pilha:
        atual = pilha.pop()
        if atual not in visitados:
            visitados.add(atual)
            for vizinho in T[atual]:
                # Ignora a aresta bloqueada
                if tuple(sorted((atual, vizinho))) == aresta_bloqueada:
                    continue
                if vizinho not in visitados:
                    pilha.append(vizinho)
    return visitados

def cortes_fundamentais(G, T):
    """
    Recebe:
      - G: grafo completo representado como dicionário de adjacência {vértice: {vizinhos: {}}}
      - T: árvore de abrangência de G, representada no mesmo formato
    Retorna:
      - Um dicionário cujas chaves são arestas da árvore (tupla (u, v) com u < v)
        e os valores são conjuntos com as arestas de G que compõem o corte fundamental
        associado à remoção da aresta da árvore.
        
    Se G e/ou T forem fornecidos como listas de arestas, eles serão convertidos.
    """
    # Converte para dicionário se os parâmetros forem listas
    if isinstance(G, list):
        G = edges_to_dict(G)
    if isinstance(T, list):
        T = edges_to_dict(T)
    
    cortes = {}
    
    # Itera apenas sobre as arestas de T (evitando duplicação com u < v)
    for u in T:
        for v in T[u]:
            if u < v:
                # Remove virtualmente a aresta (u, v) e obtém a componente que contém u
                comp = obter_componente(T, u, (u, v))
                # Em G, o corte fundamental é o conjunto de arestas que ligam
                # um vértice da componente a um vértice fora dela.
                corte = set()
                for w in comp:
                    for viz in G[w]:
                        if viz not in comp:
                            corte.add(tuple(sorted((w, viz))))
                cortes[tuple(sorted((u, v)))] = corte
    return cortes

def plotar_cortes_fundamentais(G, cortes, k=0.1, iter=50):
    """
    Recebe:
      - G: Grafo original representado como um dicionário de adjacência.
      - cortes: Dicionário retornado pela função cortes_fundamentais(G, T),
                onde as chaves são arestas da árvore e os valores são conjuntos
                de arestas de corte fundamental.
      - k, iter: Parâmetros para melhorar a visualização do layout do grafo.

    Retorna:
      - Um plot do grafo com as arestas normais em cinza e as de corte em vermelho.
    """
    # Criar o grafo do NetworkX
    G_nx = adj_list_to_nx(G)

    # Criar layout para visualização
    plt.figure(figsize=(12, 9))
    pos = nx.spring_layout(G_nx, k=k, iterations=iter)

    # Obter todas as arestas do grafo
    todas_arestas = set(G_nx.edges())

    # Obter apenas as arestas de corte do dicionário 'cortes'
    arestas_de_corte = set()
    for conjunto in cortes.values():
        arestas_de_corte.update(conjunto)  # Adiciona as arestas de corte

    # As arestas normais são aquelas que NÃO estão em cortes
    arestas_normais = todas_arestas - arestas_de_corte

    # Desenhar todas as arestas normais primeiro (em cinza)
    nx.draw(G_nx, pos, with_labels=True, node_color="gray", node_size=1000, font_size=10, font_weight="bold")
    nx.draw_networkx_edges(G_nx, pos, edgelist=list(arestas_normais), edge_color="blue", width=1.5)

    # Desenhar apenas as arestas de corte em vermelho
    nx.draw_networkx_edges(G_nx, pos, edgelist=list(arestas_de_corte), edge_color="red", width=2.5)

    plt.title("Grafo com Arestas de Corte em Vermelho")
    plt.show()


def calcular_excentricidades(grafo):
    """
    Calcula a excentricidade de cada vértice de um grafo.
    
    Parâmetros:
      grafo: dict
             Representa o grafo como uma lista de adjacência. Por exemplo:
             {
                 'A': ['B', 'C'],
                 'B': ['A', 'D'],
                 'C': ['A', 'D'],
                 'D': ['B', 'C', 'E'],
                 'E': ['D']
             }
    
    Retorna:
      Um dicionário onde cada chave é um vértice e o valor é a sua excentricidade.
      Se o vértice não alcançar todos os outros (grafo desconexo), a excentricidade será float('inf').
    """
    excentricidades = {}
    
    # Para cada vértice, fazemos uma busca em largura (BFS) para encontrar as distâncias mínimas a todos os outros vértices.
    for vertice in grafo:
        # dicionário para armazenar as distâncias mínimas a partir do vértice atual
        distancias = {}
        fila = deque()
        fila.append(vertice)
        distancias[vertice] = 0
        
        while fila:
            atual = fila.popleft()
            for vizinho in grafo.get(atual, []):
                if vizinho not in distancias:
                    distancias[vizinho] = distancias[atual] + 1
                    fila.append(vizinho)
        
        # Se nem todos os vértices foram alcançados, consideramos a excentricidade como infinita.
        if len(distancias) < len(grafo):
            excentricidades[vertice] = float('inf')
        else:
            excentricidades[vertice] = max(distancias.values())
    
    return excentricidades

def analyze_robustness(G, nodes_to_remove):
    G_copy = G.copy()
    G_copy.remove_nodes_from(nodes_to_remove)
    largest_cc = max(nx.connected_components(G_copy), key=len, default=[])
    return len(largest_cc)


def analise_robustez(G):
    # Encontrar pontos de articulação (nós cuja remoção desconecta o grafo)
    articulation_points = list(nx.articulation_points(G))

    # Encontrar arestas críticas (arestas cuja remoção desconecta o grafo)
    bridges = list(nx.bridges(G))

    print(f"Pontos de articulação (nós críticos): {articulation_points}")
    print(f"Arestas críticas (bridges): {bridges}")
    
    # Simular a remoção de nós críticos
    for node in articulation_points:
        new_size = analyze_robustness(G, [node])
        print(f"Removendo {node}, o maior componente agora tem {new_size} nós.")
    
    # Encontrar componentes conexos no grafo
    connected_components = list(nx.connected_components(G))
    num_components = len(connected_components)

    print(f"Número de componentes conexos no grafo: {num_components}")
    for i, component in enumerate(connected_components):
        print(f"Componente {i+1}: {component}")

def num_componentes_apos_remocao(grafo, vertice_removido):
    """
    Recebe um grafo (lista de adjacência) e o nome de um vértice.
    Retorna o número de componentes conexos do grafo resultante
    após a remoção do vértice (e de todas as arestas incidentes a ele).

    Parâmetros:
      - grafo: dict, onde cada chave é um vértice e o valor é uma lista de vizinhos.
      - vertice_removido: vértice a ser removido.

    Retorna:
      - número de componentes conexos (int).
    """
    # Cria uma cópia do grafo sem o vértice removido
    subgrafo = {}
    for v, vizinhos in grafo.items():
        if v == vertice_removido:
            continue
        # Filtra os vizinhos para remover o vértice que será excluído
        subgrafo[v] = [w for w in vizinhos if w != vertice_removido]

    # Função auxiliar para realizar a busca em profundidade (DFS)
    def dfs(inicio, visitados):
        stack = [inicio]
        while stack:
            atual = stack.pop()
            if atual in visitados:
                continue
            visitados.add(atual)
            for vizinho in subgrafo.get(atual, []):
                if vizinho not in visitados:
                    stack.append(vizinho)

    visitados = set()
    componentes = 0

    # Para cada vértice do subgrafo que ainda não foi visitado,
    # inicia uma DFS e conta um novo componente.
    for v in subgrafo:
        if v not in visitados:
            dfs(v, visitados)
            componentes += 1

    return componentes


def bfs_distance(graph, start, target):
    """
    Calcula a distância mínima (em número de arestas) entre 'start' e 'target'
    usando busca em largura (BFS). Se não houver caminho, retorna float('inf').
    """
    if start == target:
        return 0
    visited = {start}
    queue = collections.deque([(start, 0)])
    while queue:
        current, dist = queue.popleft()
        for neighbor in graph.get(current, []):
            if neighbor == target:
                return dist + 1
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))
    return float('inf')

def eulerize_graph(graph):
    """
    Recebe um grafo (em lista de adjacência) e retorna uma lista de novas arestas 
    (como tuplas (u, v)) que devem ser adicionadas para que o grafo se torne Euleriano.

    Critérios:
      - Apenas vértices de grau ímpar são emparelhados.
      - Não se liga vértices que já estão adjacentes.
      - Entre os pares permitidos, escolhe-se aqueles cuja distância (número de arestas) 
        seja mínima.
    """
    INF = float('inf')
    
    # 1. Identifica os vértices de grau ímpar.
    odd_vertices = [v for v in graph if len(graph[v]) % 2 == 1]
    n = len(odd_vertices)
    if n == 0:
        # Se não houver vértices de grau ímpar, o grafo já é Euleriano.
        return []
    
    # 2. Constroi uma matriz de custos entre os vértices ímpares.
    # Se dois vértices já são adjacentes, o custo será INF (não permitimos nova ligação).
    cost_matrix = [[INF] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                cost_matrix[i][j] = 0
            else:
                # Se já existe ligação direta, não permitimos adicionar outra.
                if odd_vertices[j] in graph.get(odd_vertices[i], []):
                    cost_matrix[i][j] = INF
                else:
                    cost_matrix[i][j] = bfs_distance(graph, odd_vertices[i], odd_vertices[j])
    
    # 3. Encontrar o emparelhamento perfeito mínimo usando programação dinâmica com bitmask.
    memo = {}
    
    def dp(mask):
        """
        Para um subconjunto de vértices (representado por 'mask', onde cada bit 1 indica
        que o vértice correspondente (na lista odd_vertices) ainda não foi emparelhado),
        retorna uma tupla (custo, pares) onde:
          - custo: custo total mínimo para emparelhar esses vértices.
          - pares: lista de tuplas (i, j) representando os índices dos vértices emparelhados.
        """
        if mask == 0:
            return 0, []
        if mask in memo:
            return memo[mask]
        
        # Escolhe o primeiro vértice ainda não emparelhado.
        i = 0
        while not (mask & (1 << i)):
            i += 1
        best_cost = INF
        best_pairs = None
        # Remove i do mask.
        mask_without_i = mask & ~(1 << i)
        # Tenta emparelhar i com cada outro vértice disponível.
        j_bit = mask_without_i
        while j_bit:
            # Recupera o menor índice j disponível no mask.
            j = (j_bit & -j_bit).bit_length() - 1
            new_mask = mask_without_i & ~(1 << j)
            sub_cost, sub_pairs = dp(new_mask)
            total_cost = cost_matrix[i][j] + sub_cost
            if total_cost < best_cost:
                best_cost = total_cost
                best_pairs = sub_pairs + [(i, j)]
            # Remove o bit menos significativo e repete.
            j_bit = j_bit & (j_bit - 1)
        
        memo[mask] = (best_cost, best_pairs)
        return memo[mask]
    
    full_mask = (1 << n) - 1
    _, matching = dp(full_mask)
    
    # 4. Converte os pares de índices para as arestas (nomes dos vértices).
    added_edges = []
    for i, j in matching:
        added_edges.append((odd_vertices[i], odd_vertices[j]))
    
    return added_edges