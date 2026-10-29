#Creando un diccionario
persona={
    "Nombre":"Darina",
    "Edad":16,
    "Profesion":"Programador",
    "Estudiante":False
}

print(persona)
#Accediendo a un valor en especifico
print(persona["Nombre"])
#Se puede usar el metodo get()
#Es util porque no marca error si el valor existe
print(persona.get("Profesion"))
#Modificar un valor existente
persona["Edad"]=17
print(persona["Edad"])
#Agregar un par (clave:valor)
persona=["Ciudad"]="Cecyranch"
print(persona)
#Recorrer un diccionario con un bucle