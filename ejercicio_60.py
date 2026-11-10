tabla = [[ 1,  2,  3,  4,  5],
         [ 6,  7,  8,  9, 10],
         [11, 12, 13, 14, 15],
         [16, 17, 18, 19, 20],
         [21, 22, 23, 24 ,25]]
for indice_columna in range(5):
    suma = 0
    for indice_fila in range(5):
        suma = suma + tabla[indice_fila][indice_columna]
    print(f'la suma de la columna {indice_columna} es {suma}')

for fila in tabla:
    suma = sum(fila)
    print(f'la suma de la fila {fila} es {suma}')
