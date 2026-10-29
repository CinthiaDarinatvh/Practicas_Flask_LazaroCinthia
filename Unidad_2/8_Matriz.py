#Creando matriz
numeros=[
    [1,2,3],#fila 0
    [2,3,4],#fila1
    [5,6,7]#fila2
]
#Obteniendo el numero d efilas
filas=len(numeros)#filas=3
#Obteniendo el numero de columnas
columnas=len(numeros[0])
#Ciclo externo para los indices de las flas(i)
for i in range(filas):
    #Ciclo interno para los indices de las columnas
    for j in range(columnas):
        print(f"[{i}] [{j}] = {numeros[i][j]}")