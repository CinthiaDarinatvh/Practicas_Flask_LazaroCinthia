#Creando tupla
coordenadas=(10.5,20.3,30.5,10.5) #tupla numerica
nombres=("darina","ana","dulce") #tupla de cadenas de texto

for indice,coordenada in enumerate(coordenadas):
    print(f"[{indice}] ---coordenada: {coordenada}")