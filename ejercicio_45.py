nombre = input("Introduce tu nombre y apellidos: ")

iniciales = ""
anterior = " "

for letra in nombre:
    if anterior == " " and letra != " ":
        iniciales = iniciales + letra.upper()
    anterior = letra

print(f'Tus iniciales son {iniciales}')
