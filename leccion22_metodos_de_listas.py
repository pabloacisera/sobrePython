lista_de_trabajo= [2, 'pablo', 37, 'soltero', True]
# metodo index(): muestra en que posicion se encuentra el elemento buscado

print(lista_de_trabajo.index("soltero")) #3

# metodo copy(): devuelve un copia de la lista para que podamos modificarla

copia_lista= lista_de_trabajo.copy()

copia_lista[3]= "casado"

copia_lista.append(False)

print(lista_de_trabajo)
print(copia_lista)

#metodo pop(): extrae y devuelve el ultimo elemento

devolver=copia_lista.pop(5)
print(devolver)#retiro false y lo devolvio

#metodo sort(): ordena la lista

numeros=[22,64,18,52,36,91,104,22]
numeros.sort()
print(numeros)

#metodo remove(): quita el primer valor que aparece, segùn corresponde el valor que asignemos en los corchetes.

numeros.remove(22)
print(numeros)#quito el primer 22

#metodo reverse(): gira la lista

numeros.reverse()
print(numeros)

#metodo insert(): inserte un elemento, primero se coloca la posicion y luego el elemento

numeros.insert(0, "nuevo_valor")
print(numeros)

#extends(): se utiliza para agregar una lista a otra, y se puede aplicar a tupla o cadena

nuevos_numeros=["valores", "nuevos"]
numeros.extend(nuevos_numeros)
print(numeros)



