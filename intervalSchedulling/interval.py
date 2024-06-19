# Captura de datos
N = int(input())
G = [list(map(int, input().split())) for _ in range(2)]

# Estructura de datos
tasks = [(G[0][i], G[1][i], i + 1) for i in range(N)]
tasks_sorted = sorted(tasks, key=lambda x: x[1])

# Algoritmo greedy
selected_indices = []
end_time = 0

for start, end, index in tasks_sorted:
    if start >= end_time:
        selected_indices.append(index)
        end_time = end

# Imprimir resultados
print(len(selected_indices))
print(*sorted(selected_indices))
