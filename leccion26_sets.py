###sets###

#es como crear una lista pero no modificables;
#su sintaxis es igual a la creacion de un diccionario;

my_set={'pablo', 'cisera', 'soltero', 37}

print(type(my_set))

#metodos de sets

primer_metodo= len(my_set)
print(primer_metodo) #4

my_set.add('andres')
print(my_set) #incorpora a la ultima posicion

nuevo_set=my_set.copy()
nuevo_set.add('otro elemento')
print(nuevo_set)

diferencias= nuevo_set.difference(my_set)
print(diferencias) #otro elemento