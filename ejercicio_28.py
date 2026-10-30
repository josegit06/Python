inferior = int(input("Introduce el límite inferior: "))
superior = int(input("Introduce el limite superior: "))

while inferior > superior:
    print("El limite inferior debe ser menor")
    inferior = int(input("Introduce el límite inferior: "))
    superior = int(input("Introduce el limite superior: "))

dentro = 0
fuera = 0
iguales = 0

while True:
    numero = int(input("Introduce un numero (0 para terminar): "))

    if numero == 0:
        break
    elif numero == inferior or numero == superior:
        iguales = iguales + 1
    elif numero > inferior and numero < superior:
        dentro = dentro + numero
    else:
        fuera = fuera + 1
print(f'Suma de los numeros dentro del intervalo: {dentro}')
print(f'Suma de los numeros fuera del intervalo: {fuera}')
print(f'Suma de los numeros iguales al intervalo: {iguales}')

