cadena = input("Introduce una cadena: ")

apariciones = {}

for letra in cadena:
    if letra in apariciones:
        apariciones[letra] += 1
    else:
        apariciones[letra] = 1

print(apariciones)