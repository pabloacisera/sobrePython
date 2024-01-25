empty_list = []

def agregar(num):
    while num < 10:
        empty_list.append(num)
        num += 1

# Llamada a la función
agregar(5)
print(empty_list)

other_list=[]

def agregar_con_for(valor):
    for i in range(valor,5):
        other_list.append(i)

agregar_con_for(0)


#print(empty_list) #[5,6,7,8,9,10]
print(other_list)


def unificar():
    print(other_list + empty_list)

unificar()



