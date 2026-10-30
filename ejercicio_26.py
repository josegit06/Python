numero1 = int(input("Introduce el primer numero: "))
numero2 = int(input("Introduce el segundo numero: "))

if numero1 > numero2:
    auxiliar = numero1
    numero1 = numero2
    numero2 = auxiliar

while numero1 <= numero2:
    if numero1 % 2 == 0:
        print(numero1)
    numero1 = numero1 + 1
