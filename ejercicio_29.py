base = float(input("Introduce la base: "))
exponente = int(input("Introduce el exponente: "))

resultado = 1
contador = 0

while contador < exponente:
    resultado = resultado * base
    contador = contador + 1

print(f'El resultado es {resultado}')
