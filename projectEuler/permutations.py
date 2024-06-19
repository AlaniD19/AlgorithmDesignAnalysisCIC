def permute(arr, r):
    result = []
    def generate_permutations(current_permutation, remaining_elements):
        if len(current_permutation) == r:
            result.append(current_permutation[:])
            return
        for i in range(len(remaining_elements)):
            generate_permutations(current_permutation + [remaining_elements[i]], remaining_elements[:i] + remaining_elements[i+1:])
    generate_permutations([], arr)
    return result

# Captura de datos
N, R = map(int, input().split())
elements = input().split()

# Generar permutaciones
elements.sort()
permutations = permute(elements, R)

# Ordenar las permutaciones lexicográficamente
permutations.sort()

# Imprimir las permutaciones
for perm in permutations:
    print(" ".join(perm))
