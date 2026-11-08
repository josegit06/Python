nombres = []
edades = []

nombre = input("Nombre del alumno (* para terminar): ")

while nombre != "*":
    edad = int(input(f'Edad de {nombre}: '))
    nombres.append(nombre)
    edades.append(edad)
    nombre = input("Nombre del alumno (* para terminar): ")

if len(nombres) > 0:
    print("Alumnos mayores de edad: ")
    for i in range(len(nombres)):
        if edades[i] >= 18:
            print(nombres[i], "-", edades[i], "años")

    mayor_edad = edades[0]
    for edad in edades:
        if edad > mayor_edad:
            mayor_edad = edad

    print(f'Alumnos con mas edad ({mayor_edad} años): ')
    for i in range(len(nombres)):
        if edades[i] == mayor_edad:
            print(nombres[i])

else:
    print("No se ha registrado ningun alumno")
