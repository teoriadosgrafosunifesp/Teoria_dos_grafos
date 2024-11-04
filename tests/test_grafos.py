import pytest
from grafos.grafos import (
    gerar_matriz_adjacencia, gerar_grafo_a_partir_matriz,
    gerar_matriz_incidencia, gerar_grafo_a_partir_matriz_incidencia,
    gerar_lista_adjacencia, gerar_grafo_a_partir_lista,
    numero_vertices, numero_arestas_lista_adjacencia,
    numero_arestas_matriz_adjacencia, numero_arestas_matriz_incidencia,
    vertices_adjacentes, existe_aresta_lista_adjacencia,
    existe_aresta_matriz_adjacencia, existe_aresta_matriz_incidencia,
    grau_vertice_lista_adjacencia, grau_vertice_matriz_adjacencia,
    graus_grafo_lista_adjacencia, graus_grafo_matriz_adjacencia,
    caminho_dfs, encontrar_ciclo, eh_subgrafo, subgrafo_ou_vice_versa
)

@pytest.fixture
def grafo_exemplo():
    return {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1, 3],
        3: [2]
    }

@pytest.fixture
def matriz_adjacencia_exemplo():
    return [
        [0, 1, 1, 0],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [0, 0, 1, 0]
    ]

@pytest.fixture
def matriz_incidencia_exemplo():
    return [
        [1, 1, 0, 0], 
        [1, 0, 1, 0], 
        [0, 1, 1, 1], 
        [0, 0, 0, 1]
    ]

def test_gerar_matriz_adjacencia(grafo_exemplo, matriz_adjacencia_exemplo):
    assert gerar_matriz_adjacencia(grafo_exemplo) == matriz_adjacencia_exemplo

def test_gerar_grafo_a_partir_matriz(matriz_adjacencia_exemplo, grafo_exemplo):
    assert gerar_grafo_a_partir_matriz(matriz_adjacencia_exemplo) == grafo_exemplo

def test_gerar_matriz_incidencia(grafo_exemplo, matriz_incidencia_exemplo):
    matriz_gerada = gerar_matriz_incidencia(grafo_exemplo) 
    assert matriz_gerada == matriz_incidencia_exemplo

def test_gerar_grafo_a_partir_matriz_incidencia(matriz_incidencia_exemplo, grafo_exemplo):
    grafo_gerada = gerar_grafo_a_partir_matriz_incidencia(matriz_incidencia_exemplo)
    assert grafo_gerada == grafo_exemplo

def test_gerar_lista_adjacencia(grafo_exemplo):
    assert gerar_lista_adjacencia(grafo_exemplo) == grafo_exemplo

def test_gerar_grafo_a_partir_lista(grafo_exemplo):
    assert gerar_grafo_a_partir_lista(grafo_exemplo) == grafo_exemplo

def test_numero_vertices(grafo_exemplo):
    assert numero_vertices(grafo_exemplo) == 4

def test_numero_arestas_lista_adjacencia(grafo_exemplo):
    assert numero_arestas_lista_adjacencia(grafo_exemplo) == 4

def test_numero_arestas_matriz_adjacencia(matriz_adjacencia_exemplo):
    assert numero_arestas_matriz_adjacencia(matriz_adjacencia_exemplo) == 4

def test_numero_arestas_matriz_incidencia(matriz_incidencia_exemplo):
    assert numero_arestas_matriz_incidencia(matriz_incidencia_exemplo) == 4

def test_vertices_adjacentes(grafo_exemplo):
    assert vertices_adjacentes(grafo_exemplo, 2) == [0, 1, 3]

def test_existe_aresta_lista_adjacencia(grafo_exemplo):
    assert existe_aresta_lista_adjacencia(grafo_exemplo, 0, 1) == True
    assert existe_aresta_lista_adjacencia(grafo_exemplo, 0, 3) == False

def test_existe_aresta_matriz_adjacencia(matriz_adjacencia_exemplo):
    assert existe_aresta_matriz_adjacencia(matriz_adjacencia_exemplo, 0, 1) == True
    assert existe_aresta_matriz_adjacencia(matriz_adjacencia_exemplo, 0, 3) == False

def test_existe_aresta_matriz_incidencia(matriz_incidencia_exemplo):
    assert existe_aresta_matriz_incidencia(matriz_incidencia_exemplo, 0, 1) == True
    assert existe_aresta_matriz_incidencia(matriz_incidencia_exemplo, 0, 3) == False

def test_grau_vertice_lista_adjacencia(grafo_exemplo):
    assert grau_vertice_lista_adjacencia(grafo_exemplo, 2) == 3

def test_grau_vertice_matriz_adjacencia(matriz_adjacencia_exemplo):
    assert grau_vertice_matriz_adjacencia(matriz_adjacencia_exemplo, 2) == 3

def test_graus_grafo_lista_adjacencia(grafo_exemplo):
    assert graus_grafo_lista_adjacencia(grafo_exemplo) == {0: 2, 1: 2, 2: 3, 3: 1}

def test_graus_grafo_matriz_adjacencia(matriz_adjacencia_exemplo):
    assert graus_grafo_matriz_adjacencia(matriz_adjacencia_exemplo) == {0: 2, 1: 2, 2: 3, 3: 1}

def test_caminho_dfs(grafo_exemplo):
    caminho1 = caminho_dfs(grafo_exemplo, 0, 3)
    caminho2 = caminho_dfs(grafo_exemplo, 3, 0)
    assert caminho1 == [0, 1, 2, 3]
    assert caminho2 == [3, 2, 0]

def test_encontrar_ciclo(grafo_exemplo):
    assert encontrar_ciclo(grafo_exemplo, 0) == [0, 1, 2, 0]

def test_eh_subgrafo(grafo_exemplo):
    subgrafo = {0: [1], 1: [0]}
    assert eh_subgrafo(subgrafo, grafo_exemplo) == True
    assert eh_subgrafo(grafo_exemplo, subgrafo) == False

def test_subgrafo_ou_vice_versa(grafo_exemplo):
    subgrafo = {0: [1], 1: [0]}
    assert subgrafo_ou_vice_versa(subgrafo, grafo_exemplo) == "Grafo1 é subgrafo de Grafo2"
    assert subgrafo_ou_vice_versa(grafo_exemplo, subgrafo) == "Grafo2 é subgrafo de Grafo1"
