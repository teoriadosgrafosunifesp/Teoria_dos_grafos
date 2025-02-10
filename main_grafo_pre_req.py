import pandas as pd
import networkx as nx

def ler_grafo_dependencias(csv_path):
    df = pd.read_csv(csv_path)
    G = nx.DiGraph()
    
    for _, row in df.iterrows():
        G.add_edge(row['pre_requisito'], row['materia'])  # Ajustando a direção da aresta
    
    return G

def ler_creditos(csv_path):
    df = pd.read_csv(csv_path)
    creditos = dict(zip(df['materia'], df['creditos']))
    return creditos

def calcular_semestres(G, creditos, grade_horaria):
    vagas_por_semestre = len(grade_horaria) * len(grade_horaria[0])
    ordem_topologica = list(nx.topological_sort(G))
    
    semestres = []
    semestre_atual = []
    materias_cursadas = set()
    credito_semestre = 0
    
    materias_obrigatorias = {"TCCI", "TCCII"}
    materias_sem_pre_requisitos = set(creditos.keys()) - set(G.nodes())
    
    for materia in materias_sem_pre_requisitos:
        if materia in materias_obrigatorias:
            continue  # TCCI e TCCII serão alocados depois
        aulas_por_semestre = creditos[materia]
        if credito_semestre + aulas_por_semestre <= vagas_por_semestre:
            semestre_atual.append(materia)
            materias_cursadas.add(materia)
            credito_semestre += aulas_por_semestre
        else:
            semestres.append((semestre_atual, credito_semestre))
            semestre_atual = [materia]
            materias_cursadas.add(materia)
            credito_semestre = aulas_por_semestre
    
    for materia in ordem_topologica:
        if materia in materias_obrigatorias or materia in materias_cursadas:
            continue
        
        pre_requisitos = list(G.predecessors(materia))
        if not all(pre in materias_cursadas for pre in pre_requisitos):
            continue
        
        aulas_por_semestre = creditos[materia]
        if credito_semestre + aulas_por_semestre <= vagas_por_semestre:
            semestre_atual.append(materia)
            materias_cursadas.add(materia)
            credito_semestre += aulas_por_semestre
        else:
            semestres.append((semestre_atual, credito_semestre))
            semestre_atual = [materia]
            materias_cursadas.add(materia)
            credito_semestre = aulas_por_semestre
    
    if semestre_atual:
        semestres.append((semestre_atual, credito_semestre))
    
    if len(semestres) < 2:
        semestres.append(([], 0))  # Garante que existam pelo menos dois últimos semestres
    
    ultimo_semestre_creditos = sum(creditos[m] for m in semestres[-1][0])
    penultimo_semestre_creditos = sum(creditos[m] for m in semestres[-2][0])
    
    # Verifica se há espaço no penúltimo semestre para TCCI
    if penultimo_semestre_creditos + creditos["TCCI"] <= vagas_por_semestre:
        semestres[-2][0].append("TCCI")
    else:
        # TCCI vai para o semestre 9
        if len(semestres) < 9:
            semestres.append((["TCCI"], creditos["TCCI"]))
        else:
            semestres[8][0].append("TCCI")
    
    # Verifica se há espaço no último semestre para TCCII
    if ultimo_semestre_creditos + creditos["TCCII"] <= vagas_por_semestre:
        semestres[-1][0].append("TCCII")
    else:
        semestres.append((["TCCII"], creditos["TCCII"]))
    
    return semestres

def resolver_curso(grafo_path, creditos_path, grade_horaria):
    G = ler_grafo_dependencias(grafo_path)
    creditos = ler_creditos(creditos_path)
    
    semestres = calcular_semestres(G, creditos, grade_horaria)
    
    for i, (semestre, total_creditos) in enumerate(semestres, 1):
        total_creditos = sum(creditos[m] for m in semestre)
        print(f"Semestre {i}: {', '.join(semestre)} | Total de Créditos: {total_creditos}")

grafo_path = 'grafo_dependencias.csv'
creditos_path = 'creditos.csv'
grade_horaria = [
    ['A', 'B'],
    ['C', 'D'],
    ['E', 'F'],
    ['G', 'H'],
    ['I', 'J'],
]

resolver_curso(grafo_path, creditos_path, grade_horaria)
