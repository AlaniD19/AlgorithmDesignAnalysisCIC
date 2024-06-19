V, E = map(int, input().split())
G = [input().split() for _ in range(E)]

# Captura del grafo
grafo = {str(i): [] for i in range(1, V + 1)}

def agregar_arista(grafo, u, v):
    grafo[u].append(v)
    grafo[v].append(u)

def DFS(grafo, nodo, visitados, componente):
    visitados.append(nodo)
    componente.append(nodo)
    for vecino in grafo[nodo]:
        if vecino not in visitados:
            DFS(grafo, vecino, visitados, componente)

def componentes_conexas(grafo, V):
    visitados = []
    componentes = []
    for vertice in range(1, V + 1):
        vertice_str = str(vertice)
        if vertice_str not in visitados:
            componente = []
            DFS(grafo, vertice_str, visitados, componente)
            componente = sorted(map(int, componente))
            componentes.append(componente)
    return componentes

for u, v in G:
    agregar_arista(grafo, u, v)

componentes = componentes_conexas(grafo, V)
print(len(componentes))
for componente in componentes:
    print(*componente)
