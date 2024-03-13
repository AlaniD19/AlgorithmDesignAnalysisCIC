import random

def generar_tablas(N):
    # Genera listas de hombres y mujeres
    hombres = list(range(1, N+1))
    mujeres = [chr(i) for i in range(65, 65+N)]

    # Mezcla las listas de hombres y mujeres de manera aleatoria
    #random.shuffle(hombres)
    #random.shuffle(mujeres)

    # Combina los hombres con sus preferencias de mujeres
    tabla_hombres = {hombre: random.sample(mujeres, N) for hombre in hombres}

    # Combina las mujeres con sus preferencias de hombres
    tabla_mujeres = {mujer: random.sample(hombres, N) for mujer in mujeres}

    return tabla_hombres, tabla_mujeres

# Ejemplo de uso
N = 4 #Número de hombres y mujeres
tabla_hombres, tabla_mujeres = generar_tablas(N)

print("Tabla de preferencias de hombres:")
print(tabla_hombres)
for hombre, preferencias in tabla_hombres.items():
    print(f"{hombre}: {', '.join(preferencias)}")

print("\nTabla de preferencias de mujeres:")
print(tabla_mujeres)
for mujer, preferencias in tabla_mujeres.items():
    print(f"{mujer}: {', '.join(map(str, preferencias))}")

#### test numeero de caracteres para emparejar
import string
caracteres = string.ascii_letters  # Contiene todas las letras del alfabeto (mayúsculas y minúsculas)
print("Cantidad de caracteres alfanuméricos:", len(caracteres))