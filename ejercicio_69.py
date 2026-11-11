numero = int(input("Introduce un número: "))
cuadrados = {}

for i in range(1, numero + 1):
    cuadrados[i] = i ** 2

print(cuadrados)