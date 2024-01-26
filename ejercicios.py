set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

set1.difference_update(set2)

print(set1) #{1,2} se eliminaron de la lista los elementos equivalentes que habia en la segunda lista

set2.discard(5)
print(set2)#{3, 4, 6, 7}SI EL ELEMENTO NO EXISTE, NO ARROJA ERROR SINO QUE SIMPLEMENTE NO HACE NADA.





