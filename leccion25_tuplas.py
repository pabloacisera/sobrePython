#tupla: conjunto de elementos, que utiliza un metodos similar a la lista, pero 
#que no pueden ser modificadas en sus elementos;

nueva_tupla=('pablo', 'cisera', 37, 'soltero')

print(type(nueva_tupla)) #<class 'tuple'>

print(nueva_tupla.index('soltero')) #1 nos devuelve el indice
print(nueva_tupla.count(37)) #1 nos devuelve la cantidad

#si se pueden unir tuplas

tupla1= ('hola')
tupla2= ('pablo')
unir_tuplas= tupla1 +' '+tupla2
print(unir_tuplas)

#podemos aplicarle un slice
dividir= unir_tuplas[0:1]
print(dividir) #h

print(unir_tuplas[5:-3]) #pa

#si se creo una tupla pero se deben modificar datos podemos forzarla a lista

tupla= ('javier', 'fontana', 28)
crear_lista= list(tupla)
crear_lista.pop(2)
crear_lista.append(29)#primero la convertimos en una lista, luego extraemos el 
#dato erroneo,  y por ultimo incorporamos el dato veraz

print(crear_lista)

volver_a_tupla= tuple(crear_lista)
print(volver_a_tupla) #se transformo la lista en tupla nuevamente

#por ultimo podemos eliminar con la funcion comun a todos los tipo 'del';

del volver_a_tupla
print(volver_a_tupla) #NameError: name 'volver_a_tupla' is not defined