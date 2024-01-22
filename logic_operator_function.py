def suma_condicional(numero_uno, numero_dos):
    if numero_uno== 5:
        resultado=numero_uno + numero_dos
        return resultado
    else: 
        resultado='no corresponde la operacion'
        return resultado
    
resultado= suma_condicional(7, 4)
print(resultado)

resultado= suma_condicional(5, 9)
print(resultado)