
import networkx as nx
import matplotlib.pyplot as plt
import random
from collections import defaultdict, deque
import itertools

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

def encontrar_arvore_central(grafo):
    """
    Encontra a árvore central do grafo.
    """
    arvores = {}
    vertices = list(grafo.keys())

    # Gera todas as árvores de abrangência a partir de cada vértice
    for v in vertices:
        arvores[v] = gerar_arvore_abrangencia(grafo, v)

    # Calcula todas as distâncias entre as árvores
    distancias = {v: {} for v in vertices}
    for (v1, v2) in itertools.combinations(vertices, 2):
        distancia = calcular_distancia_arvores(arvores[v1], arvores[v2])
        distancias[v1][v2] = distancia
        distancias[v2][v1] = distancia

    # Para cada árvore, calcula a maior distância em relação às outras
    max_distancias = {v: max(distancias[v].values()) for v in vertices}

    # Encontra a árvore com a menor distância máxima
    arvore_central = max(max_distancias, key=max_distancias.get)
    
    return arvore_central, arvores[arvore_central]

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

def plotar_cortes_fundamentais(G, cortes, k, iter):
    """
    Recebe:
      - G: Grafo original representado como um dicionário de adjacência.
      - cortes: Dicionário retornado pela função cortes_fundamentais(G, T), 
                onde as chaves são arestas da árvore e os valores são conjuntos 
                de arestas de corte fundamental.

    Retorna:
      - Um plot do grafo com as arestas de corte fundamental destacadas em vermelho.
    """
    # Criar o grafo do networkx
    G_nx = adj_list_to_nx(G)

    # Criar layout
    plt.figure(figsize=(12, 9))
    pos = nx.spring_layout(G_nx, k=k, iterations=iter)

    # Desenhar todas as arestas normais em cinza
    nx.draw(G_nx, pos, with_labels=True, node_color="lightblue", edge_color="gray", node_size=1000, font_size=10, font_weight="bold")

    # Desenhar as arestas de corte em vermelho
    for corte in cortes.values():
        nx.draw_networkx_edges(G_nx, pos, edgelist=list(corte), edge_color="red", width=2.5)

    plt.title("Grafo com Arestas de Corte em Vermelho")
    plt.show()


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
