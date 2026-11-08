notas = []

while len(notas) < 5:
    nota = float(input("Introduce la nota del alumno (0-10): "))
    if nota >= 0 and nota <= 10:
        notas.append(nota)
    else:
        print("Nota no valida, tiene que ser entre 0 y 10")

suma = 0
mayor = notas[0]
menor = notas[0]

for nota in notas:
    suma = suma + nota
    if nota > mayor:
        mayor = nota
    if nota < menor:
        menor = nota

media = suma / len(notas)

print(f'Notas: {notas}')
print(f'Media: {media}')
print(f'Nota más alta: {mayor}')
print(f'Nota más baja: {menor}')

