import random


def generar_tablas(N):
    # Genera listas de hombres y mujeres
    hombres = list(range(1, N + 1))
    mujeres = list(range(N + 1, (N * 2 + 1)))

    # Combina los hombres con sus preferencias de mujeres
    tabla_hombres = {hombre: mujeres[:] for hombre in hombres}
    for hombre in hombres:
        random.shuffle(tabla_hombres[hombre])

    # Combina las mujeres con sus preferencias de hombres
    tabla_mujeres = {mujer: hombres[:] for mujer in mujeres}
    for mujer in mujeres:
        random.shuffle(tabla_mujeres[mujer])

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