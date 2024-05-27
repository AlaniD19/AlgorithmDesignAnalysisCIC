def powerset(some_list):
    if len(some_list) == 0:
        return [[]]
    subsets = []
    first_element = some_list[0]
    remaining_list = some_list[1:]
    for partial_subset in powerset(remaining_list):
        subsets.append(partial_subset)
        subsets.append(partial_subset[:] + [first_element])
    return subsets


if __name__ == '__main__':
    number_elements = int(input())
    elements = input().split()
    output = powerset(elements)
    for subset in output:
        print(" ".join(subset))