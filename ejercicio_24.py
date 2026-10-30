cantidad = int(input("Cuantos numeros vas a introducir? "))

positivos = 0
negativos = 0
ceros = 0

contador = 0

while contador < cantidad:
    numero = float(input("Introduce un numero: "))

    if numero > 0:
        positivos = positivos + 1
    elif numero < 0:
        negativos = negativos + 1
    else:
         ceros = ceros + 1

    contador = contador + 1

print(f'Numeros mayores que 0: {positivos}')
print(f'Numeros menores que 0: {negativos}')
print(f'Numeros iguales a 0: {ceros}')

