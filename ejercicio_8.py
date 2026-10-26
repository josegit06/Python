sueldo_base = float(input("Introduce el sueldo base: "))

venta1 = float(input("Introduce la primera venta: "))
venta2 = float(input("Introduce la segunda venta: "))
venta3 = float(input("Introduce la tercera venta: "))

comisiones = (venta1 + venta2 + venta3) * 0.10
sueldo_total = sueldo_base + comisiones

print(f'El dinero recibidoo por comisiones es de {comisiones} euros')
print(f'El sueldo total del mes es de {sueldo_total} euros')
