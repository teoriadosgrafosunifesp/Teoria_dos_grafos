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
    # Número de vagas por semana, considerando 5 dias e 2 vagas por dia
    vagas_por_semestre = len(grade_horaria) * len(grade_horaria[0])
    
    # Ordenação topológica das matérias (garante a ordem de cursar respeitando as dependências)
    ordem_topologica = list(nx.topological_sort(G))
    
    semestres = []
    semestre_atual = []
    dias_por_semestre = len(grade_horaria)  # Número de dias na grade horária (5 dias)
    vagas_por_dia = len(grade_horaria[0])  # Número de vagas por dia (2 vagas por dia)
    
    materias_cursadas = set()  # Para acompanhar as matérias já cursadas
    credito_semestre = 0  # Controla o total de créditos alocados no semestre
    
    # Primeiro, alocamos as matérias sem pré-requisitos
    materias_sem_pre_requisitos = set(creditos.keys()) - set(G.nodes())
    
    # Aloca matérias sem pré-requisitos no primeiro semestre disponível
    for materia in materias_sem_pre_requisitos:
        aulas_por_semestre = creditos[materia]
        if credito_semestre + aulas_por_semestre <= vagas_por_semestre:
            semestre_atual.append(materia)
            materias_cursadas.add(materia)
            credito_semestre += aulas_por_semestre  # Adiciona os créditos ao semestre atual
        else:
            semestres.append((semestre_atual, credito_semestre))  # Adiciona o semestre com créditos
            semestre_atual = [materia]
            materias_cursadas.add(materia)
            credito_semestre = aulas_por_semestre  # Reinicia a contagem de créditos
    
    # Agora alocamos as outras matérias respeitando as dependências
    for materia in ordem_topologica:
        # Verificar se todos os pré-requisitos da matéria já foram cursados
        pre_requisitos = list(G.predecessors(materia))
        if not all(pre in materias_cursadas for pre in pre_requisitos):
            continue  # Não pode alocar a matéria sem cursar os pré-requisitos
        
        aulas_por_semestre = creditos[materia]
        
        # Verifica se a matéria pode ser alocada no semestre atual
        if credito_semestre + aulas_por_semestre <= vagas_por_semestre:
            semestre_atual.append(materia)
            materias_cursadas.add(materia)
            credito_semestre += aulas_por_semestre  # Adiciona os créditos ao semestre atual
        else:
            # Se o semestre atual não comporta mais essa matéria, adiciona o semestre e começa um novo
            semestres.append((semestre_atual, credito_semestre))  # Adiciona o semestre com créditos
            semestre_atual = [materia]
            materias_cursadas.add(materia)
            credito_semestre = aulas_por_semestre  # Reinicia a contagem de créditos
    
    if semestre_atual:
        semestres.append((semestre_atual, credito_semestre))  # Adiciona o último semestre
    
    return semestres

def resolver_curso(grafo_path, creditos_path, grade_horaria):
    G = ler_grafo_dependencias(grafo_path)
    creditos = ler_creditos(creditos_path)
    
    semestres = calcular_semestres(G, creditos, grade_horaria)
    
    # Imprimir a configuração de matérias por semestre com a soma de créditos
    for i, (semestre, total_creditos) in enumerate(semestres, 1):
        print(f"Semestre {i}: {', '.join(semestre)} | Total de Créditos: {total_creditos}")

# Exemplo de uso
grafo_path = 'grafo_dependencias.csv'  # CSV com as dependências entre matérias
creditos_path = 'creditos.csv'  # CSV com os créditos de cada matéria
grade_horaria = [
    ['A', 'B'],  # 1º dia, 2 vagas
    ['C', 'D'],  # 2º dia, 2 vagas
    ['E', 'F'],  # 3º dia, 2 vagas
    ['G', 'H'],  # 4º dia, 2 vagas
    ['I', 'J'],  # 5º dia, 2 vagas
]

resolver_curso(grafo_path, creditos_path, grade_horaria)
