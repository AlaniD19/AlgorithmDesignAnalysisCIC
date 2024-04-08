# CIC IPN / MCIC
# Programa: stableMatching.py
# Descripción:
# Autor: Alan Delgado
# Fecha de creación: Marzo 2024
# Versión: 1.0
# Dependencias: sinteticGeneration.py - para las pruebas
# Complejidad temporal: O(n²)

import sinteticGeneration
import matplotlib.pyplot as plt

def graphComplex(pathDocValues):
    """
    Despliega la grafica de los valores de complejidad temporal.
    Args: string: Ruta del archivo con los valores a graficar.
    Returns: NA
    """
    # Listas para almacenar los valores de n y tiempo
    n_values = []
    tiempo_values = []
    # Leer los datos desde el archivo de texto
    with open('data.txt', 'r') as file:
        for line in file:
            n, tiempo = map(int, line.strip().split(','))
            n_values.append(n)
            tiempo_values.append(tiempo)
    # Graficar los datos
    plt.plot(n_values, tiempo_values, marker='o', linestyle='-')
    plt.title('Duración de la ejecución en función de n')
    plt.xlabel('n')
    plt.ylabel('Tiempo')
    plt.grid(True)
    plt.show()


if __name__ == '__main__':