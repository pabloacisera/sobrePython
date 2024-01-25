# Crear una lista original
lista_original = [1, 2, 3, 4, 5]

# Crear una copia de la lista original
copia_lista = lista_original.copy()

copia_lista.remove(3) #se deberia haber utilizado .pop(3)


# Modificar un dato en la copia
dato_modificado = 99

# Agregar el nuevo dato en la posición correspondiente de la lista original
copia_lista.insert(2, dato_modificado)

# Imprimir las listas originales y modificadas
print("Lista Original:", lista_original)
print("Copia de Lista:", copia_lista)


#del() elimina por indice, a diferencia de remove() que elimina un elemento especifico

lista_a= ["clave", "valor"]
del lista_a[1]
print (lista_a)