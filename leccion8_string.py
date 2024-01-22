primera_cadena= 'hola'

segunda_cadena= 'mundo'

print(f'el resultado de utilizar f y barra invertida es :  {primera_cadena} {segunda_cadena}')

print('el resultado es: %s %s' %(primera_cadena, segunda_cadena))

#si quisieramos imprimir un numero dentro de una cadena debemos forzar el string

first_row= 5
second_row= 'el numero es: '

new_string= second_row + str(first_row) 

print(new_string)

