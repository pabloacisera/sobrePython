#se genera una cadena de texto que incorpora todos los datos de una persona
#y luego se agrega dicha cadena a una lista
data_base = []

def incorporar():
    dato = input('Dato a ingresar en DataBase: ')
    data_base.append(dato)

def mostrar():
    print(data_base)

incorporar()
mostrar()

