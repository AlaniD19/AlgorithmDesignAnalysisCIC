# CIC IPN / MCIC
# Programa: stableMatching.py
# Descripción:
# Autor: Alan Delgado
# Fecha de creación: Marzo 2024
# Versión: 1.0
# Complejidad temporal: O(n²)


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


# Ejemplo de ejecución
if __name__ == "__main__":
    data = input()
    lines = data.splitlines()

    agents, proposition = lines[0].split()
    agents = int(agents)

    # Inicializar una lista para las líneas restantes
    lines = []

    # Leer las siguientes líneas según el número de agents (2 * agents líneas)
    for _ in range(2 * agents):
        line = input()
        lines.append(line)

    one_prefs = {}
    two_prefs = {}

    for i in range(agents):
        people = lines[i].split()
        key = people[0]
        preferences = people[1:]
        one_prefs[key] = preferences

    for i in range(agents, 2*agents):
        people = lines[i].split()
        key = people[0]
        preferences = people[1:]
        two_prefs[key] = preferences

    if proposition == "m":
        matches = gale_shapley(one_prefs, two_prefs)
    else:
        matches = gale_shapley(two_prefs, one_prefs)
    for person in matches.keys():
        print(person, matches[person])
