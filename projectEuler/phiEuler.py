def euler_phi(n):
    phi = list(range(n+1))
    for i in range(2, n+1):
        if phi[i] == i:
            for j in range(i, n+1,i):
                phi[j] *= (i - 1)
                phi[j] //= i
    return phi


def etf(n):
    phi = euler_phi(n)
    max = 0
    index = 0
    for i in range(2, n+1):
        n_phi = i / phi[i]
        if n_phi > max:
            max = n_phi
            index = i
    return index


if __name__ == "__main__":
    n = 1_000_000
    print(etf(n))