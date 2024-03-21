# Crear un laberinto aleatorio en Python3 usando el algoritmo de
# recorrido en profundidad. El propósito de este programa es mostrar las
# características del lenguaje.
# Autor: Mario Abarca
# Fecha: 2017/09/07
# Modificaciones: Alan Delgado Alarcon
# Fecha edicion: 23/03/2021

## ESTE ALGORITMO NO ES MI AUTORÍA, Y SE UTILIZO PARA ACORTAR TIEMPOS DE PRUEBA
## SE LE REALIZO UNA MODIFICACIÓN PARA SU USO EN LA PRACTICA DE ANALISIS DE ALGORTIMOS

from random import shuffle, randint     # Números pseudoaleatorios
from itertools import product           # Producto cartesiano

def laberinto(m, n):
    def vecinos(i, j):                  # Conjunto de celdas aledañas a (i, j)
        if 0 < i: yield i - 1, j
        if i < m - 1: yield i + 1, j
        if 0 < j: yield i, j - 1
        if j < n - 1: yield i, j + 1

    def visitar(i, j):                  # Alg. de recorrido en profundidad:
        X.add((i, j))                   # Marcar celda actual como visitada
        N = list(vecinos(i, j)); shuffle(N)  # Desordenar celdas vecinas
        for h, k in N:                  # Para cada celda vecina
            if (h, k) in X: continue    # ...que no haya sido visitada:
            A[i + h + 1][j + k + 1] = ' '  # Tumbar el muro que las separa
            B[i + h + 1][j + k + 1] = 0
            visitar(h, k)               # Visitar vecina recursivamente

    A = [['#'] * (2 * n + 1) for i in range(2 * m + 1)]  # Tablero

    ## CREAMOS A LA PAR UNA MATRIZ DE 1'S PARA NUESTRO ANALIZADOR
    B = [[1] * (2 * n + 1) for i in range(2 * m + 1)]

    for i, j in product(range(1, 2*m + 1, 2), range(1, 2*n + 1, 2)):
        A[i][j] = ' '                   # Poner celdas blancas
        B[i][j] = 0                     ## NOSOTROS LENAMOS CON 0'S EL CAMINO CREADO
    X = set()                           # Conjunto de celdas visitadas
    visitar(randint(0, m - 1), randint(0, n - 1))  # Inicio en celda aleatoria
    Z = ('\n'.join(''.join(fila) for fila in A)) # Unir símbolos en un str

    ## AHORA TENEMOS 1 PROBLEMA: EL LABERINTO GENERADO TIENE BORDES QUE NO
    ## NECESITAMOS, ENTONCES LOS ELIMINAMOS DE LA MATRIZ DE NUMEROS
    B = B[1:-1]                         # eliminar bordes superiro e inferior
    for i in range(len(B)):             # eliminar extremos izquierdo y derecho
        del B[i][0]
        del B[i][-1]

    return Z, B

'''
PRUEBA PARA LIMPIAR LA MATRIZ DE NUMEROS RESULTANTES PARA
GENERAR UN LABERINTO LIMPIO PASO A PASO

PARA VISUALIZAR DESCOMENTE LAS SIGUIENTE LINEAS DE CODIGO Y COMENTE LAS LINEAS 45-48
'''
# m, n = laberinto(9, 9)
# print(m, '\n\n')
#
# # for i in n:
# #     print(i)
#
# # eliminamos extremos superior e inferior
# n = n[1:-1]
#
# # for i in n:
# #     print(i)
#
# # print('\n\n')
#
# # eliminar extremos izquierdo y derecho
# for i in range(len(n)):
#     del n[i][0]
#     del n[i][-1]
#
# for i in n:
#     print(i)
#
# print(len(n))