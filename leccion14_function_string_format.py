def convertir_ingresar(nombre, apellido):
    mensaje = 'Bienvenido %s %s a Clinica 2.0' % (nombre, apellido)
    print(mensaje)
    
    return mensaje

# Ejemplo de uso
nombre = "Yamila"
apellido = "Vallejos"
resultado = convertir_ingresar(nombre, apellido)