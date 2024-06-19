# CIC IPN / MCIC
# Programa: stableMatching.py
# Descripción:
# Autor: Alan Delgado
# Fecha de creación: Marzo 2024
# Versión: 1.0
# Dependencias: sinteticGeneration.py - para la generación de datos
# Complejidad temporal: O(n²)

import time
import sinteticGeneration
import matplotlib.pyplot as plt


def gale_shapley(hom_preferencias, muj_preferencias):
    """ Genera un emparejamiento estable con base en el algoritmo de Gale-Shapley
        ARGS: hom_preferencias, muj_preferencias (dict): tablas de preferencias por cada agente
        RETURN: emparejamiento (dict): emparejamiento estable
    """
    # Inicializar listas de estados
    hom_libre = list(hom_preferencias.keys())
    emparejamiento = {}
    muj_actual_pareja = {mujer: None for mujer in muj_preferencias.keys()}
    muj_ranking = {}

    # Crear ranking de preferencias de mujeres
    for mujer, prefs in muj_preferencias.items():
        muj_ranking[mujer] = {hombre: rank for rank, hombre in enumerate(prefs)}

    while hom_libre:
        hombre = hom_libre.pop(0)
        hom_prefs = hom_preferencias[hombre]

        for mujer in hom_prefs:
            pareja_actual = muj_actual_pareja[mujer]

            if pareja_actual is None:
                # La mujer está libre, emparejarla con el hombre
                emparejamiento[hombre] = mujer
                muj_actual_pareja[mujer] = hombre
                break
            else:
                # La mujer ya está emparejada, verificar si prefiere al nuevo hombre
                rank_pareja_actual = muj_ranking[mujer][pareja_actual]
                rank_potencial_pareja = muj_ranking[mujer][hombre]

                if rank_potencial_pareja < rank_pareja_actual:
                    # La mujer prefiere al nuevo hombre, cambiar de pareja
                    emparejamiento[hombre] = mujer
                    muj_actual_pareja[mujer] = hombre
                    hom_libre.append(pareja_actual)  # La expareja se convierte en libre
                    break
    return emparejamiento


def graphComplex(pathDocValues):
    """ Despliega la gráfica de los valores de complejidad temporal.
        Args: string: Ruta del archivo con los valores a graficar.
        Returns: NA
    """
    # Listas para almacenar los valores de n y tiempo
    n_values = []
    tiempo_values = []

    # Leer los datos desde el archivo de texto
    with open(pathDocValues, 'r') as file:
        for i, line in enumerate(file, start=2):
            tiempo = float(line.strip())
            n_values.append((i ** 2)*3)
            tiempo_values.append(tiempo)
    # Graficar los datos
    plt.plot(n_values, tiempo_values, marker='o', linestyle='-', color='lightcoral')
    #plt.title('Duración de la ejecución en función de $n$')
    plt.xlabel('$n$ (tamaño de entrada)')
    plt.ylabel('Tiempo (segundos)')
    #plt.title('Duración de la generación de datos de entrada en función de $n$')
    plt.title('Duración de la impresión del emparejamiento en función de $n$')

    plt.xscale('log', base=2)
    #plt.yscale('log')
    #plt.grid(True, which="both", ls="--")
    plt.grid(True)
    plt.savefig("exc.png", dpi=1000)
    plt.show()


# Ejemplo de ejecución
if __name__ == "__main__":
    archivos = ["execution_times.txt", "generation_times.txt", "print_times.txt"]
    for nombre_archivo in archivos:
        with open(nombre_archivo, "w") as archivo:
            archivo.write("")
    for n in range(1,100):
        s_time_generation = time.perf_counter()
        men_prefs, women_prefs = sinteticGeneration.generar_tablas((n**2)*3)
        e_time_generation = time.perf_counter()
        generation_time = e_time_generation - s_time_generation
        s_time_algorithm = time.perf_counter()  # Iniciar medición de tiempo
        matches = gale_shapley(men_prefs, women_prefs)
        e_time_algorithm = time.perf_counter()  # Finalizar medición de tiempo
        execution_time = e_time_algorithm - s_time_algorithm
        s_time_print = time.perf_counter()
        print(f"Matches {n}: {matches}")
        e_time_print = time.perf_counter()
        print_time = e_time_print - s_time_print
        # Guardar el tiempo de ejecución en un archivo
        with open("generation_times.txt", "a") as file:
            file.write(f"{generation_time:.8f}\n")
        with open("execution_times.txt", "a") as file:
            file.write(f"{execution_time:.8f}\n")
        with open("print_times.txt", "a") as file:
            file.write(f"{print_time:.8f}\n")
    #graphComplex('execution_times.txt')
    #graphComplex('generation_times.txt')
    graphComplex('print_times.txt')