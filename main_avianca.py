import csv
from grafos import grafos
import networkx as nx

# Inicializa o grafo não direcionado
G = nx.Graph()

# Abre e lê o arquivo CSV, considerando que ele está separado por ";"
# Substitua "materias.csv" pelo nome do seu arquivo CSV
with open("Grafo Avianca.csv", mode='r') as file:
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
# plotar_subgrafo(G, 9)

G_adj = grafo_para_lista_adjacencia(G)
G_lista = grafos.gerar_matriz_adjacencia(G_adj)

# plotar_grafo_com_graus(G)
# print(grafos.existe_aresta_lista_adjacencia(G_adj, "AOC", "Lab de AOC"))
# print(grafos.busca_destinos(G_adj, "CUV", ["AL I", "IA", "CD", "PEC"])[0])
# print(grafos.caminho_bfs(G_adj, "LP", "Lab de CD"))
# print(grafos.maior_clique(G_adj))
# plotar_no_com_vizinhos(G, "Teoria dos Grafos")
# plotar_subgrafo_lista(G, grafos.busca_destinos(G_adj, "CUV", ["AL I", "IA", "CD", "PEC"])[0])