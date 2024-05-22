import random
from multiprocessing import Pool


def generar_preferencias_parallel(item, lista2):
    return item, random.sample(lista2, len(lista2))


def generar_tablas(N):
    hombres = list(range(1, N + 1))
    mujeres = list(range(N + 1, N * 2 + 1))

    with Pool() as pool:
        tabla_hombres = dict(pool.starmap(generar_preferencias_parallel, [(hombre, mujeres) for hombre in hombres]))
        tabla_mujeres = dict(pool.starmap(generar_preferencias_parallel, [(mujer, hombres) for mujer in mujeres]))

    return tabla_hombres, tabla_mujeres


'''
N = 4  # Número de hombres y mujeres
tabla_hombres, tabla_mujeres = generar_tablas(N)

print("Tabla de preferencias de hombres:")
print(tabla_hombres)
for hombre, preferencias in tabla_hombres.items():
    # print(f"{hombre}: {', '.join(preferencias)}")
    print(f"{hombre}: {', '.join(map(str, preferencias))}")

print("\nTabla de preferencias de mujeres:")
print(tabla_mujeres)
for mujer, preferencias in tabla_mujeres.items():
    print(f"{mujer}: {', '.join(map(str, preferencias))}")
    # print(f"{mujer}: {', '.join(preferencias)}")

#### test numeero de caracteres para emparejar
##import string
##caracteres = string.ascii_letters  # Contiene todas las letras del alfabeto (mayúsculas y minúsculas)
##print("Cantidad de caracteres alfanuméricos:", len(caracteres))
'''
