notas = []

while len(notas) < 5:
    nota = float(input("Introduce la nota del alumno (0-10): "))
    if nota >= 0 and nota <= 10:
        notas.append(nota)
    else:
        print("Nota no valida, tiene que ser entre 0 y 10")

media = sum(notas) / len(notas)

print(f'Notas: {notas}')
print(f'Media: {media}')
print(f'Nota más alta: {max(notas)}')
print(f'Nota más baja: {min(notas)}')

