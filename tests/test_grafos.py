import pytest
from grafos.grafos import (
    calcular_graus, gerar_matriz_adjacencia, gerar_grafo_a_partir_matriz,
    gerar_matriz_incidencia, gerar_grafo_a_partir_matriz_incidencia,
    gerar_lista_adjacencia, gerar_grafo_a_partir_lista,
    numero_vertices, numero_arestas_lista_adjacencia,
    numero_arestas_matriz_adjacencia, numero_arestas_matriz_incidencia, verificar_subgrafo,
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

@pytest.fixture
def grafo_exemplo_1():
    return {
        "A": ["B", "C", "D"],
        "B": ["A", "C", "D", "E", "F"],
        "C": ["A", "B", "G", "H"],
        "D": ["A", "B","C", "I", "J"],
        "E": ["B", "K"],
        "F": ["B", "L"],
        "G": ["C", "M"],
        "H": ["C", "N"],
        "I": ["D", "O"],
        "J": ["D", "P"],
        "K": ["E", "Q"],
        "L": ["F", "R"],
        "M": ["G", "S"],
        "N": ["H", "T"],
        "O": ["I", "U"],
        "P": ["J", "V"],
        "Q": ["K", "W"],
        "R": ["L", "X"],
        "S": ["M", "Y"],
        "T": ["N", "Z"],
        "U": ["O", "AA"],
        "V": ["P", "BB"],
        "W": ["Q", "CC"],
        "X": ["R", "DD"],
        "Y": ["S", "EE"],
        "Z": ["T", "FF"],
        "AA": ["U", "GG"],
        "BB": ["V", "HH"],
        "CC": ["W", "II"],
        "DD": ["X", "JJ"],
        "EE": ["Y", "KK"],
        "FF": ["Z", "LL"],
        "GG": ["AA", "MM"],
        "HH": ["BB", "NN"],
        "II": ["CC", "OO"],
        "JJ": ["DD", "PP"],
        "KK": ["EE", "QQ"],
        "LL": ["FF", "RR"],
        "MM": ["GG", "SS"],
        "NN": ["HH", "TT"],
        "OO": ["II", "UU"],
        "PP": ["JJ", "VV"],
        "QQ": ["KK", "WW"],
        "RR": ["LL", "XX"],
        "SS": ["MM", "YY"],
        "TT": ["NN", "ZZ"],
        "UU": ["OO", "AAA"],
        "VV": ["PP", "BBB"],
        "WW": ["QQ", "CCC"],
        "XX": ["RR", "DDD"],
        "YY": ["SS", "EEE"],
        "ZZ": ["TT", "FFF"],
        "AAA": ["UU", "GGG"],
        "BBB": ["VV", "HHH"],
        "CCC": ["WW", "III"],
        "DDD": ["XX", "JJJ"],
        "EEE": ["YY", "KKK"],
        "FFF": ["ZZ", "LLL"],
        "GGG": ["AAA", "MMM"],
        "HHH": ["BBB", "NNN"],
        "III": ["CCC", "OOO"],
        "JJJ": ["DDD", "PPP"],
        "KKK": ["EEE", "QQQ"],
        "LLL": ["FFF", "RRR"],
        "MMM": ["GGG", "SSS"],
        "NNN": ["HHH", "TTT"],
        "OOO": ["III", "UUU"],
        "PPP": ["JJJ", "VVV"],
        "QQQ": ["KKK", "WWW"],
        "RRR": ["LLL", "XXX"],
        "SSS": ["MMM", "YYY"],
        "TTT": ["NNN", "ZZZ"],
        "UUU": ["OOO", "AAAA"],
        "VVV": ["PPP", "BBBB"],
        "WWW": ["QQQ", "CCCC"],
        "XXX": ["RRR", "DDD"],
        "YYY": ["SSS", "EEE"],
        "ZZZ": ["TTT", "FFF"],
        "AAAA": ["UUU", "BBB"],
        "BBBB": ["VVV", "DDD"],
        "CCCC": ["WWW", "DDD"]
    }

@pytest.fixture
def grafo_exemplo_subgrafo():
    return { 
        "A": ["B", "C"], 
        "B": ["A", "E"], 
        "C": ["A"]
    }
            
@pytest.fixture
def grafo_aero():
    return {
    "ATL": ["LAX", "JFK", "ORD"],
    "LAX": ["ATL", "SFO", "DFW"],
    "JFK": ["ATL", "LHR", "LAX"],
    "ORD": ["ATL", "DEN", "LAX"],
    "SFO": ["LAX", "SEA", "DEN"],
    "DFW": ["ATL", "DEN", "MIA"],
    "LHR": ["JFK", "CDG", "DXB"],
    "DEN": ["ORD", "SFO", "DFW"],
    "SEA": ["SFO", "LAX", "PHX"],
    "MIA": ["ATL", "DFW", "BOS"],
    "CDG": ["LHR", "FRA", "DXB"],
    "DXB": ["LHR", "CDG", "JFK"],
    "PHX": ["SEA", "LAX", "LAS"],
    "BOS": ["MIA", "JFK", "EWR"],
    "FRA": ["CDG", "MUC", "DXB"],
    "MUC": ["FRA", "VIE", "ZRH"],
    "DXB": ["CDG", "LHR", "FRA"],
    "VIE": ["MUC", "ZRH", "PRG"],
    "ZRH": ["MUC", "VIE", "BRN"],
    "PRG": ["VIE", "FRA", "WAW"],
    "BRN": ["ZRH", "MUC", "STR"],
    "WAW": ["PRG", "FRA", "CPH"],
    "STR": ["BRN", "ZRH", "TXL"],
    "CPH": ["WAW", "FRA", "OSL"],
    "TXL": ["STR", "ZRH", "MUC"],
    "OSL": ["CPH", "FRA", "ARN"],
    "ARN": ["OSL", "CPH", "BLL"],
    "BLL": ["ARN", "CPH", "HEL"],
    "HEL": ["BLL", "ARN", "OSL"],
    "CPH": ["WAW", "OSL", "BLL"],
    "TXL": ["STR", "ZRH", "MUC"],
    "OSL": ["CPH", "FRA", "ARN"],
    "ARN": ["OSL", "CPH", "BLL"],
    "BLL": ["ARN", "CPH", "HEL"],
    "HEL": ["BLL", "ARN", "OSL"],
    "CPH": ["WAW", "OSL", "BLL"],
    "TXL": ["STR", "ZRH", "MUC"],
    "OSL": ["CPH", "FRA", "ARN"],
    "ARN": ["OSL", "CPH", "BLL"],
    "BLL": ["ARN", "CPH", "HEL"],
    "HEL": ["BLL", "ARN", "OSL"],
    "CPH": ["WAW", "OSL", "BLL"],
    "TXL": ["STR", "ZRH", "MUC"],
    "OSL": ["CPH", "FRA", "ARN"],
    "ARN": ["OSL", "CPH", "BLL"],
    "BLL": ["ARN", "CPH", "HEL"],
    "HEL": ["BLL", "ARN", "OSL"],
    "CPH": ["WAW", "OSL", "BLL"],
    "TXL": ["STR", "ZRH", "MUC"],
    "OSL": ["CPH", "FRA", "ARN"],
    "ARN": ["OSL", "CPH", "BLL"],
    "BLL": ["ARN", "CPH", "HEL"],
    "HEL": ["BLL", "ARN", "OSL"],
    "CPH": ["WAW", "OSL", "BLL"],
    "TXL": ["STR", "ZRH", "MUC"],
    "OSL": ["CPH", "FRA", "ARN"],
    "ARN": ["OSL", "CPH", "BLL"],
    "BLL": ["ARN", "CPH", "HEL"],
    "HEL": ["BLL", "ARN", "OSL"],
    "CPH": ["WAW", "OSL", "BLL"],
    "TXL": ["STR", "ZRH", "MUC"],
    "OSL": ["CPH", "FRA", "ARN"],
    "ARN": ["OSL", "CPH", "BLL"],
    "BLL": ["ARN", "CPH", "HEL"],
    "HEL": ["BLL", "ARN", "OSL"],
    "CPH": ["WAW", "OSL", "BLL"],
    "TXL": ["STR", "ZRH", "MUC"],
    "OSL": ["CPH", "FRA", "ARN"],
    "ARN": ["OSL", "CPH", "BLL"],
    "BLL": ["ARN", "CPH", "HEL"],
    "HEL": ["BLL", "ARN", "OSL"],
    "CPH": ["WAW", "OSL", "BLL"],
    "TXL": ["STR", "ZRH", "MUC"],
    "OSL": ["CPH", "FRA", "ARN"],
    "ARN": ["OSL", "CPH", "BLL"],
    "BLL": ["ARN", "CPH", "HEL"],
    "HEL": ["BLL", "ARN", "OSL"],
    "CPH": ["WAW", "OSL", "BLL"],
    "TXL": ["STR", "ZRH", "MUC"],
    "OSL": ["CPH", "FRA", "ARN"],
    "ARN": ["OSL", "CPH", "BLL"],
    "BLL": ["ARN", "CPH", "HEL"],
    "HEL": ["BLL", "ARN", "OSL"],
    "CPH": ["WAW", "OSL", "BLL"]
}

def test_calcular_graus(grafo_exemplo_1):
    maior_grau, menor_grau = calcular_graus(grafo_exemplo_1)
    assert maior_grau == 5
    assert menor_grau == 2

def test_verificar_subgrafo(grafo_exemplo_1, grafo_exemplo_subgrafo):
    assert True == verificar_subgrafo(grafo_exemplo_1, grafo_exemplo_subgrafo)
