usuario = []

def datos_personales():
    nombre = input('Ingrese nombre del paciente: ')
    apellido = input('Ingrese apellido del paciente: ')
    edad = input('Ingrese edad del paciente: ')
    estado = input('Ingrese estado civil del paciente: ')
    telefono = input('Ingrese teléfono del paciente: ')
    direccion = input('Ingrese dirección del paciente: ')

    usuario.append(nombre)
    usuario.append(apellido)
    usuario.append(edad)
    usuario.append(estado)
    usuario.append(telefono)
    usuario.append(direccion)

    print(usuario)

# Llamamos a la función una vez para ingresar los datos
datos_personales()


##CONTINUACION-- VER leccion19