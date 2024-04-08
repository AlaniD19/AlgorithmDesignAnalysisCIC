# CIC IPN / MCIC
# Programa: laberinto.py
# Descripción: Para un laberinto aleatrio generado en una matriz, encuentra la solución con backtracking segun la entrada.
# Autor: Alan Delgado
# Fecha de creación: Marzo 2024
# Versión: 1.0
# Dependencias: maze_generator.py - para las pruebas
# Complejidad temporal: O(n²)

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