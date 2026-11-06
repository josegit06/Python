cadena = input("Introduce un texto: ")
caracter = input("Buscar caracter en el texto (solo uno): ")

if len(caracter) != 1:
    print("Solo un carácter")
else:
    print(f'El caracter {caracter} aparece {cadena.count(caracter)} veces')
