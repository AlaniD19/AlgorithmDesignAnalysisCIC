'''
Autor: Alan Delgado
Fecha: 23/03/2021

ESCUELA SUPERIOR DE CÓMPUTO - IPN
ANALISIS DE ALGORTIMOS

--- Ddo un laberinto aleatrio generado en una matriz, encontrar la solución por
    medio de backtracking.

para su correcto funcionamiento tener en la misma carpeta o proyecto python
el archivo maze_generator que crea los laberintos aleatorios

COMPLEJIDAD DEL ALGORTIMO: O(n^2)
'''

import maze_generator

# medida del laberinto -> (2n+1)-2
l = 10                                          # definimos el entero del laberinto
maze_c, maze = maze_generator.laberinto(l, l)   # creamos el laberinto
SIZE = len(maze)
maze_solve = [[0]*SIZE for _ in range(SIZE)]    #c reamos una matriz para la solución

def encontrar_camino(r, c):
    if (r==SIZE-1) and (c==SIZE-1):
        maze_solve[r][c] = 1
        return True
    if 0 <= r < SIZE and c>=0 and c<SIZE and maze_solve[r][c] == 0 and maze[r][c] == 0:
        maze_solve[r][c] = 1
        if encontrar_camino(r+1, c):
            return True
        if encontrar_camino(r, c+1):
            return True
        if encontrar_camino(r-1, c):
            return True
        if encontrar_camino(r, c-1):
            return True
        maze_solve[r][c] = 0
        return False
    return 0


if encontrar_camino(0,0):                   # si encontramos un camino solucion...
    for i in range(len(maze_solve)):        # modificamos los 0's por vacios y los 1's por #'s
        for j in range(len(maze_solve)):    # para mejorar la visualización del camino final
            if maze_solve[i][j] == 0: maze_solve[i][j] = ' '
            elif maze_solve[i][j] == 1: maze_solve[i][j] = '#'

    print('Laberinto original...')
    print(maze_c, '\n\n')                   # mostramos el laberinto creado externamente
    print('Solucion..')
    for i in maze_solve:                    # mostramos el camino solucion
        print(i)

else:
    print ("No hay solución crack...")