persona=[];

nombre= input('ingrese nombre: ')
apellido= input('ingrese apellido: ')
edad= input('ingrese edad: ')

persona.append(nombre)
persona.append(apellido)
persona.append(edad)

print(persona)
print(persona[1])
print('el nombre de la persona es: ' + persona[0] + ' y tiene '+ persona[2] + ' años.')