suma = 0
cantidad = 0

while True:
    numero = float(input("Introduce un número (para terminar 0):"))

    if numero == 0:
        break

    suma = suma + numero
    cantidad = cantidad + 1

if cantidad > 0:
    media = suma / cantidad
    print(f'La suma es {suma}')
    print(f'La media es {media}')
else:
    print("No has introducido ningun número")
