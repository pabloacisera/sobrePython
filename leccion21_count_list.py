persona= ['pablo', 'cisera', 34,'pablo', 'soltero']

#si quisieramos contar cuantas veces se repite un elemento de la lista
print(persona.count('pablo')) #devuelve 2

# a diferencia de contar los elementos de una lista
print(len(persona)) #devuelve 5

#podemos incorporar datos aislados y posteriormente igualarlos a otros elementos
#DESEMPAQUETADO

lista=[22, 'fontana', 'soltero', 'javier']

edad, apellido, estado, nombre= lista

print(nombre) #javier

#o tambien mediante el proceso inverso
lista_invertida= [ 'hobbies', 'domicilio' ]

futbol, reconquista= lista_invertida

print(reconquista) #domicilio

