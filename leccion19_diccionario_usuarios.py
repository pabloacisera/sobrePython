lista_de_usuarios = {}

def agregar_usuarios():
    nuevo_usuario = {
        'nombre': input('Ingrese nombre: '),
        'apellido': input('Ingrese apellido: '),
        'edad': input('Ingrese edad: '),
        'estado civil': input('Ingrese estado civil: '),
        'direccion': input('Ingrese dirección: '),
        'telefono': input('Ingrese número celular: '),
        'email': input('Ingrese su email: ')
    }
    return nuevo_usuario

def incorporar_nuevo_usuario(nuevo):
    nombre_usuario = nuevo['nombre']
    lista_de_usuarios[nombre_usuario] = nuevo
    print(lista_de_usuarios)

# Agregar un nuevo usuario a la lista
nuevo_usuario = agregar_usuarios()
incorporar_nuevo_usuario(nuevo_usuario)