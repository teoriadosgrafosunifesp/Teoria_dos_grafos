from matplotlib import pyplot as plt
import networkx as nx
import csv

from grafos.grafos import analise_robustez, calcular_distancia_arvores, calcular_graus, caminho_dfs, cortes_fundamentais, edges_to_dict, eh_euleriano, eh_hamiltoniano, encontrar_ciclo, eulerian_path_or_cycle, existe_aresta_matriz_adjacencia, find_center_tree, generate_spanning_trees, gerar_lista_adjacencia, gerar_matriz_adjacencia, gerar_matriz_incidencia, grau_vertice_matriz_adjacencia, numero_vertices, subgrafo_ou_vice_versa, verificar_subgrafo, vertices_adjacentes

def visualizar_arvore_central(central_tree):
    T = nx.Graph(central_tree)
    plt.figure(figsize=(8, 6))
    nx.draw(T, with_labels=True, node_color='lightgreen', edge_color='black', node_size=2000, font_size=10)
    plt.show()

def visualizar_grafo(G):
    plt.figure(figsize=(8, 6))
    nx.draw(G, with_labels=True, node_color='lightblue', edge_color='black', node_size=2000, font_size=10)
    plt.show()

# Funções para carregar grafos
def carregar_grafo():
    print("Escolha a forma de entrada do grafo:")
    print("1 - Inserir arestas manualmente (formato: u v)")
    print("2 - Carregar de um arquivo CSV")
    
    opcao = input("Opção: ")
    G = nx.Graph()
    
    if opcao == "1":
        print("Digite as arestas (pressione Enter sem valor para finalizar):")
        while True:
            entrada = input().strip()
            if not entrada:
                break
            try:
                u, v = entrada.split()
                G.add_edge(u, v)
            except ValueError:
                print("Formato inválido. Use: u v")
    
    elif opcao == "2":
        caminho = input("Digite o caminho do arquivo CSV: ")
        try:
            with open(caminho, newline='') as csvfile:
                leitor = csv.reader(csvfile)
                for linha in leitor:
                    if len(linha) == 2:
                        G.add_edge(linha[0], linha[1])
            print("Grafo carregado com sucesso!")
        except FileNotFoundError:
            print("Arquivo não encontrado.")
    
    return G

# Função para carregar múltiplos grafos
def carregar_varios_grafos():
    grafos = []
    n = int(input("Quantos grafos você deseja importar? "))
    
    for i in range(n):
        print(f"\nCarregando grafo {i+1}:")
        G = carregar_grafo()
        grafos.append(G)
    
    return grafos


def encontrar_ciclo_em_grafo(grafo):
    vertice = input("Digite o vértice inicial para buscar ciclo: ")
    ciclo = encontrar_ciclo(dict(grafo.adjacency()), vertice)
    
    if ciclo:
        print(f"Ciclo encontrado: {ciclo}")
    else:
        print("Nenhum ciclo encontrado.")


# Funções para execução do comando
def gerar_comando_com_funcao(grafos):
    while True:
        print("\nEscolha uma função para executar:")
        print("1 - Gerar matriz de adjacência")
        print("2 - Gerar matriz de incidência")
        print("3 - Gerar lista de adjacência")
        print("4 - Verificar subgrafo ou vice-versa")
        print("5 - Calcular maior e menor grau")
        print("6 - Verificar se um grafo é subgrafo de outro")
        print("7 - Listar grafos carregados")
        print("8 - Encontrar ciclo em um grafo")
        print("9 - Encontrar caminho DFS entre dois vértices")
        print("10 - Verificar se existe aresta entre dois vértices na matriz de adjacência")
        print("11 - Verificar vértices adjacentes de um vértice")
        print("12 - Verificar grau de um vértice na matriz de adjacência")
        print("13 - Contar o número de vértices em um grafo")
        print("14 - Gerar árvores geradoras de um grafo")
        print("15 - Calcular distância entre duas árvores de abrangência")
        print("16 - Determinar árvore central")
        print("17 - Visualizar o grafo")
        print("18 - Verificar se o grafo possui circuito ou caminho euleriano")
        print("19 - Gerar Cortes das Arestas Fundamentais")
        print("20 - Verificar se o grafo é euleriano?")
        print("21 - Verificar se o grafo é hamiltoniano?")
        print("22 - Análise de Robustez, Pontos de Articulação Identificados, Arestas Críticas Encontrada e  Acessibilidade Avaliada")
        
        print("0 - Sair")
        
        opcao = input("Opção: ")
        if opcao == "0":
            break
        elif opcao == "7":
            print("\nGrafos carregados:")
            for i, G in enumerate(grafos):
                print(f"Grafo {i+1}: {list(G.nodes)}")
        elif opcao in ["1", "2", "3", "4", "5", "6", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22"]:
            if len(grafos) > 1 and opcao in ["1", "2", "3", "5", "8", "9", "10", "11", "12", "13", "14", "18", "20", "21", "22"]:
                print("\nEscolha qual grafo utilizar:")
                for i, G in enumerate(grafos):
                    print(f"{i+1} - Grafo {i+1}")
                escolha = int(input("Escolha um grafo: ")) - 1
                G = grafos[escolha]
            else:
                G = grafos[0]

            if opcao == "1":
                for linha in gerar_matriz_adjacencia(dict(G.adjacency())):
                    print(linha)
            elif opcao == "2":
                for linha in gerar_matriz_incidencia(dict(G.adjacency())):
                    print(linha)
            elif opcao == "3":
                for v, neighbors in gerar_lista_adjacencia(dict(G.adjacency())).items():
                    print(f"{v}: {neighbors}")
            elif opcao == "4":
                if len(grafos) > 1:
                    print("\nEscolha os grafos para verificar subgrafo:")
                    for i, G in enumerate(grafos):
                        print(f"{i+1} - Grafo {i+1}")
                    escolha1 = int(input("Escolha o primeiro grafo: ")) - 1
                    escolha2 = int(input("Escolha o segundo grafo: ")) - 1
                    resultado = subgrafo_ou_vice_versa(dict(grafos[escolha1].adj), dict(grafos[escolha2].adj))
                    print(resultado)
                else:
                    print("Não há grafos suficientes para comparar.")
            elif opcao == "5":
                maior, menor = calcular_graus(dict(G.adjacency()))
                print(f"Maior grau: {maior}, Menor grau: {menor}")
            elif opcao == "6":
                if len(grafos) > 1:
                    print("\nEscolha os grafos para verificar subgrafo:")
                    for i, G in enumerate(grafos):
                        print(f"{i+1} - Grafo {i+1}")
                    escolha1 = int(input("Escolha o primeiro grafo: ")) - 1
                    escolha2 = int(input("Escolha o segundo grafo: ")) - 1
                    resultado = verificar_subgrafo(dict(grafos[escolha1].adj), dict(grafos[escolha2].adj))
                    print("Subgrafo verificado: ", resultado)
                else:
                    print("Não há grafos suficientes para comparar.")
            elif opcao == "8":  # Encontrar ciclo
                encontrar_ciclo_em_grafo(G)
            elif opcao == "9":  # Caminho DFS
                inicio = input("Digite o vértice de início para o caminho DFS: ")
                destino = input("Digite o vértice de destino para o caminho DFS: ")
                caminho = caminho_dfs(dict(G.adjacency()), inicio, destino)
                if caminho:
                    print(f"Caminho DFS encontrado: {caminho}")
                else:
                    print("Caminho não encontrado.")
            elif opcao == "10":  # Existe aresta
                matriz_adjacencia = gerar_matriz_adjacencia(dict(G.adjacency()))
                v1 = int(input("Digite o primeiro vértice: "))
                v2 = int(input("Digite o segundo vértice: "))
                if existe_aresta_matriz_adjacencia(matriz_adjacencia, v1, v2):
                    print(f"Existe uma aresta entre {v1} e {v2}")
                else:
                    print(f"Não existe aresta entre {v1} e {v2}")
            elif opcao == "11":  # Vértices adjacentes
                vertice = input("Digite o vértice para verificar os adjacentes: ")
                adjacentes = vertices_adjacentes(dict(G.adjacency()), vertice)
                print(f"Vértices adjacentes a {vertice}: {adjacentes}")
            elif opcao == "12":  # Grau de vértice
                matriz_adjacencia = gerar_matriz_adjacencia(dict(G.adjacency()))
                vertice = int(input("Digite o vértice para verificar seu grau: "))
                grau = grau_vertice_matriz_adjacencia(matriz_adjacencia, vertice)
                print(f"Grau do vértice {vertice}: {grau}")
            elif opcao == "13":  # Número de vértices
                numero = numero_vertices(dict(G.adjacency()))
                print(f"Número de vértices no grafo: {numero}")
            elif opcao == "14":  # Gerar árvores geradoras
                vertices = list(G.nodes)
                k = int(input("Quantas árvores geradoras você deseja gerar? (Digite 0 para gerar todas) "))
                
                # Se k for 0, gera todas as árvores possíveis
                if k == 0:
                    k = len(vertices) * (len(vertices) - 1) // 2  # Um número alto para gerar todas as árvores
                
                # Chama a função generate_spanning_trees
                trees = generate_spanning_trees(dict(G.adjacency()), vertices, k)
                
                # Exibe as árvores geradoras
                for i, tree in enumerate(trees):
                    print(f"\nÁrvore {i+1}:")
                    for u, neighbors in tree.items():
                        print(f"{u}: {', '.join(map(str, neighbors))}")
            elif opcao == "15":  # Calcular distância entre árvores de abrangência
                if len(grafos) > 1:
                    print("\nEscolha as duas árvores de abrangência para calcular a distância:")
                    for i, G in enumerate(grafos):
                        print(f"{i+1} - Grafo {i+1}")
                    escolha1 = int(input("Escolha a primeira árvore: ")) - 1
                    escolha2 = int(input("Escolha a segunda árvore: ")) - 1
                    
                    # Verifica se os grafos selecionados são árvores de abrangência
                    if nx.is_tree(grafos[escolha1]) and nx.is_tree(grafos[escolha2]):
                        # Converte as árvores em listas de arestas
                        A1 = list(grafos[escolha1].edges())
                        A2 = list(grafos[escolha2].edges())
                        
                        # Calcula a distância entre as árvores
                        distancia = calcular_distancia_arvores(A1, A2)
                        print(f"Distância entre as árvores: {distancia}")
                    else:
                        print("Um ou ambos os grafos selecionados não são árvores de abrangência.")
                else:
                    print("Não há grafos suficientes para comparar.")
            elif opcao == "16":  # Encontrar nó central e gerar a árvore geradora central
                if len(grafos) > 1:
                    print("\nEscolha qual grafo utilizar:")
                    for i, G in enumerate(grafos):
                        print(f"{i+1} - Grafo {i+1}")
                    escolha = int(input("Escolha um grafo: ")) - 1
                    G = grafos[escolha]
                else:
                    G = grafos[0]
                
                center, central_tree = find_center_tree(dict(G.adjacency()))
                print(f"Nó central do grafo: {center}")
                print("Árvore geradora central:")
                for node, neighbors in central_tree.items():
                    print(f"{node}: {', '.join(map(str, neighbors))}")
                escolha = str(input("Deseja visualizar o grafo: (S ou N) ")).upper()
                if(escolha == "S"):
                    visualizar_arvore_central(central_tree)
            elif opcao == "17":  # Visualizar o grafo
                if len(grafos) > 1:
                    print("\nEscolha qual grafo visualizar:")
                    for i, G in enumerate(grafos):
                        print(f"{i+1} - Grafo {i+1}")
                    escolha = int(input("Escolha um grafo: ")) - 1
                    G = grafos[escolha]
                else:
                    G = grafos[0]
                
                visualizar_grafo(G)
            elif opcao == "18":  # Existe aresta
                resultado = eulerian_path_or_cycle(G)
                print(resultado)
            elif opcao == "19":
                if len(grafos) > 1:
                    print("\nEscolha um grafo e uma árvores de abrangência para realizar os cortes:")
                    for i, G in enumerate(grafos):
                        print(f"{i+1} - Grafo {i+1}")
                    escolha1 = int(input("Escolha o grafo: ")) - 1
                    escolha2 = int(input("Escolha a árvore de abrangência: ")) - 1
                    
                    # Verifica se os grafos selecionados são árvores de abrangência
                    if nx.is_tree(grafos[escolha2]):
                        # Converte as árvores em listas de arestas
                        A1 = list(grafos[escolha1].edges())
                        A2 = list(grafos[escolha2].edges())
                        
                        # Calcula a distância entre as árvores
                        cortes = cortes_fundamentais(A1, A2)
                        for aresta, corte in cortes.items():
                            print(f"Corte fundamental da aresta {aresta}: {corte}")
                    else:
                        print("houve um erro .")
                else:
                    print("Não há grafos suficientes para comparar.")
            elif opcao == "20":
                resultado = eh_euleriano(G)
                print(resultado)
            elif opcao == "21":
                resultado = eh_hamiltoniano(G)
                print(resultado)
            elif opcao == "22":
                analise_robustez(G)
        else:
            print("Opção inválida.")


def main():
    grafos = carregar_varios_grafos()
    gerar_comando_com_funcao(grafos)


if __name__ == "__main__":
    main()
