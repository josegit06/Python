minutos = int(input("Introduce una cantidad de minutos sin decimales: "))

horas = minutos // 60
minutos_restantes = minutos % 60

print(f'{minutos} minutos son {horas} horas y {minutos_restantes} minutos.')
