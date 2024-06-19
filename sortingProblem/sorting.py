def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)


def merge(left, right):
    sorted_arr = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            sorted_arr.append(left[left_index])
            left_index += 1
        else:
            sorted_arr.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        sorted_arr.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        sorted_arr.append(right[right_index])
        right_index += 1

    return sorted_arr


# Captura de datos
num_cases = int(input())
test_cases = []

for _ in range(num_cases):
    case = list(map(int, input().split()))
    test_cases.append(case)

# Procesar y ordenar cada caso de prueba
sorted_cases = [merge_sort(case) for case in test_cases]

# Imprimir los resultados
for sorted_case in sorted_cases:
    print(" ".join(map(str, sorted_case)))
