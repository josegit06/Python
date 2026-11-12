precios = {"manzana": 1.5, "pera": 2, "platano": 1.2, "naranja": 1.8, "mandarina": 0.8}

continuar = "s"

while continuar == "s":
    fruta = input("Introduce una fruta: ")

    if fruta in precios:
        cantidad = float(input("Cuantos kilos has vendido: "))
        total = precios[fruta] * cantidad
        print(f'1 Kilo de {fruta} son {precios[fruta]} €')
        print(f'Precio final de {fruta}: {total} € para {cantidad} Kg')
    else:
        print("Error, esta fruta no la tenemos")
    continuar = input("¿Quieres hacer otra consulta? (s/n): ")

print("Fin del programa")