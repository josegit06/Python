import random

numero_secreto = random.randint(1, 100)

intentos = 10

while intentos > 0:
    numero = int(input("Adivina el número del 1 al 100: "))

    if numero < 1 or numero > 100:
        print("Introduce un número del 1 al 100: ")
        continue

    intentos = intentos - 1

    if numero == numero_secreto:
        print(f'Correcto! Has acertado en {intentos}')
        break

    elif numero < numero_secreto:
        print("El numero secreto es mayor")

    else:
        print("El numero secreto es menor")

    print(f'Te quedan {intentos}')

    if intentos == 0 and numero != numero_secreto:
        print(f"Has perdido! No te quedan intentos, el numero secreto era {numero_secreto}")
