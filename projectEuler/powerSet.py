'''def powerset(elements):
    power_set = []
    n = len(elements)
    # Generar todos los subconjuntos no vacíos usando bits
    for i in range(1, 2 ** n):
        subset = []
        for j in range(n):
            if i & (1 << j):
                subset.append(elements[j])
        power_set.append(subset)
    # Ordenar primero por la longitud de los subconjuntos y luego según el orden de entrada
    power_set.sort(key=lambda x: (len(x), [elements.index(e) for e in x]))
    return power_set


if __name__ == '__main__':
    number_elements = int(input())
    elements = input().split()
    #output = [sorted(sublista) for sublista in powerset(elements)]
    output = powerset(elements)
    for subset in output:
        print(" ".join(subset))
        '''

def power_set(s):
    subsets = [[]]
    for element in s:
        subsets += [current + [element] for current in subsets]
    return subsets

# Captura de datos
N = input()
elements = input().split()

# Generar el conjunto potencia
#elements.sort()
subsets = power_set(elements)

# Filtrar y ordenar los subconjuntos
subsets = [subset for subset in subsets if subset]
subsets.sort(key=len)

# Imprimir los subconjuntos
for subset in subsets:
    print(*subset)

