meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

mes = int(input("Introduce el numero del mes (1-12): "))

while mes < 1 and mes > 12:
    mes = int(input("Mes no valido, introduce un número entre 1 y 12: "))

print(f'El mes {meses[mes - 1]}, tiene {dias[mes - 1]} dias')

