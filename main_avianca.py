import csv
from grafos import grafos
import networkx as nx

def busca_grafo(txt):
    # Inicializa o grafo não direcionado
    G = nx.Graph()

    # Abre e lê o arquivo CSV, considerando que ele está separado por ";"
    # Substitua "materias.csv" pelo nome do seu arquivo CSV
    with open(txt, mode='r') as file:
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
    return G

G = busca_grafo("Grafo Avianca.csv")

G_adj = grafos.grafo_para_lista_adjacencia(G)
E = grafos.numero_arestas_lista_adjacencia(G_adj)
V = grafos.numero_vertices(G_adj)
# print(len(grafos.vertices_adjacentes(G_adj, "BOG")))
#grafos.plotar_lista_adj(G_adj, 0.9, 60)

excentricidades = grafos.calcular_excentricidades(G_adj)
vertices_excentricidade = sorted(excentricidades.items(), key=lambda item: item[1])

# Seleciona os 3 primeiros (ou menos, se o grafo tiver menos de 3 vértices)
min3 = vertices_excentricidade[:3]

print("Os 3 vértices com menor excentricidade são:")
for vertice, excent in min3:
    print(f"Vértice {vertice} com excentricidade {excent}")

max3 = vertices_excentricidade[-3:]

print("Os 3 vértices com maior excentricidade são:")
for vertice, excent in max3:
    print(f"Vértice {vertice} com excentricidade {excent}")
#-----------------------------1. Ache sua árvore central
#central_tree = grafos.obter_lista_adjacencia_arvore_central(G_adj)
#grafos.plotar_lista_adj(central_tree, 0.9, 60)

#-----------------------------2. Verifique se o grafo representativo de seu problema é euleriano
# isEuler, euler_cycle = grafos.eh_euleriano(G_adj)
# if isEuler:
#     print("Tem ciclo euleriano")
#     grafos.plotar_lista_adj(euler_cycle, 0.9, 60)
# else:
#     print("Não é euleriano")

#-----------------------------3 Verifique se o grafo representativo do seu problema é hamiltoniano.
#isHamil, hamil_cycle = grafos.eh_hamiltoniano(G_adj)
#if isHamil:
#    print("Tem ciclo hamiltoniano")
#    grafos.plotar_lista_adj(hamil_cycle, 0.9, 60)
#else:
#    print("Não é hamiltoniano")

#-----------------------------4. Determina algum corte fundamental para o grafo representativo do seu problema.
# T = grafos.obter_lista_adjacencia_arvore_central(G_adj)
# cortes = grafos.cortes_fundamentais(G_adj, T)
# print(cortes)
#grafos.plotar_cortes_fundamentais(G_adj, cortes[0], k=5, iter=50)

#-----------------------------5. Considerando alguns cortes do grafo representativo do seu problema, faça uma análise de robustez e acessibilidade das entidades que você escolheu para serem nós no seu modelo de grafo.


#-----------------------------6. Usando todos os conceitos vistos até aqui, resolva o problema que você formulou, indicando suas características.

new_edges = grafos.eulerize_graph(G_adj)
print(new_edges)
for edge in new_edges:
    G.add_edge(edge[0], edge[1])

grafos.plot_nx_grafo(G)