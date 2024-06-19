N = int(input())
G = []
for _ in range(2):
    row = list(map(int, input().split()))
    G.append(row)

orden = {int(i): [] for i in range(1, N + 1)}
task = [[a, b] for a, b in zip(G[0], G[1])]
arr = dict(zip(orden, task))

arr_ord = dict(sorted(arr.items(), key=lambda n: n[1][1]))
B = []
orden = []
tiempo_actual = 0
latencia_total = 0

for j, k in arr_ord.items():
    horas, entrega = k
    ini_time = tiempo_actual
    end_time = ini_time + horas
    latencia = max(0, end_time - entrega)
    latencia_total += latencia
    tiempo_actual = end_time
    B.append(latencia)
    orden.append(j)

B = max(B)
print(B)
print(*orden)