lista = ["objeto", "objeto", ..., "pablo", "objeto", ...]

try:
    busqueda = lista.index(input('Ingrese búsqueda: '))
    print('El elemento buscado se encuentra en la posición:', busqueda)
except ValueError:
    print('El elemento buscado no se encuentra en la presente lista.')



