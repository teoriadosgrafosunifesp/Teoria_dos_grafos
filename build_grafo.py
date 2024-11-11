import csv
import networkx as nx
import matplotlib.pyplot as plt
import random

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

# Inicializa o grafo não direcionado
G = nx.Graph()

# Abre e lê o arquivo CSV, considerando que ele está separado por ";"
# Substitua "materias.csv" pelo nome do seu arquivo CSV
with open("Grafo de matérias.csv", mode='r') as file:
    reader = csv.reader(file, delimiter=';')  # Define o delimitador como ";"
    next(reader)  # Pula o cabeçalho

    # Itera sobre cada linha (matéria e seu(s) pré-requisito(s))
    for row in reader:
        materia = row[0]
        pre_requisitos = row[1]

        # Adiciona o nó da matéria
        G.add_node(materia)

        # Verifica e processa os pré-requisitos
        if pre_requisitos != "-":  # Ignora se não houver pré-requisito
            # Separa os pré-requisitos por vírgula e cria uma aresta para cada um
            for pre_req in pre_requisitos.split(","):
                pre_req = pre_req.strip()  # Remove espaços extras
                G.add_node(pre_req)  # Adiciona o nó do pré-requisito
                G.add_edge(materia, pre_req)  # Adiciona aresta entre a matéria e o pré-requisito

# plotar_nos_maior_grau(G)
# plotar_nos_menor_grau(G)
plotar_subgrafo(G, 9)
# # Visualiza o grafo
# pos = nx.spring_layout(G, k=0.6, iterations=80)  # Ajuste k para controlar o espaçamento

# # Plotando o grafo
# plt.figure(figsize=(12, 12))  # Aumenta o tamanho da figura
# nx.draw(G, pos, with_labels=True, node_size=500, font_size=10, font_weight='bold', node_color="skyblue", edge_color="gray")
# plt.title("Grafo com Nós Mais Espaçados")
# plt.show()
