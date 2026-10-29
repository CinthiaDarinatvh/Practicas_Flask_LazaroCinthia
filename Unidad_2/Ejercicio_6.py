tabla =[
    ["Nombre" , "Edad" , "Calificaciones"],
    ["Karla",16,8.0],
    ["Dulce",16,8.0],
    ["Ulises",16,6.0],
    ["Oscar",16,6.0],
    ["Mariel",16,9.0],
    ["Sherlyn",16,9.0],
    ["Jorge",16,6.0],
    ["Melisa",16,8.0],
    ["Jesus",16,7.0],
    ["Ximena",16,6.0],
    ["Nora",16,7.0],
]

buscar=input("Ingresa tu nombre: ")
filas=len(tabla)
columnas=len(tabla[0])

for i in range(filas):
    for j in range(columnas):
        if tabla[i][j]==buscar:
            print(f"encontre {buscar} en [{i}] [{j}]")
            print(f"Datos: {tabla[i]}")