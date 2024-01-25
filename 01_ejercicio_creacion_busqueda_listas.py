lista = []

def crear_paciente():
    name = input("Ingrese el nombre que desea incorporar: ")
    lista.append(name)

def buscar_paciente():
    name = input("Ingrese el usuario que desea buscar: ")
    if name in lista:
        conteo = lista.count(name)
        return f'Se ha encontrado "{name}" {conteo} veces en la lista.'
    else:
        return f'No se ha encontrado el usuario "{name}" en la lista.'

# Paso 1: Agregar un paciente a la lista
crear_paciente()

# Paso 2: Buscar un paciente en la lista
resultado_busqueda = buscar_paciente()
print(resultado_busqueda)