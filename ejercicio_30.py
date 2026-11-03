numero = 1

while numero <= 5:
    print(f'Tabla de multiplicar del {numero}')
    contador = 1
    while contador <= 10:
        print(numero, "x", contador, "=", numero * contador)
        contador = contador + 1
    numero = numero + 1
