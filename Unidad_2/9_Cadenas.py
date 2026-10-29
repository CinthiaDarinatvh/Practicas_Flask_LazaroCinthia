#CADENAS Y COCADENTACION CON (+)
Cadena1='Hola'
Cadena2='Mundo'
multilinea="""Esto es una cadena
de varias lineas"""
print(Cadena1+Cadena2+multilinea)#print(f"{Cadena1"})S
#CADENAS Y REPETICION
eco="ja"*3
print(eco)
#CAMBIAR UNA CADENA DE MINUSCULA A MAYUSCULA
tu_nombre='Darina'
print(tu_nombre.upper())
#CAMBIAR UNA CADENA DE MAYUSCULA A MINUSCULA
print(tu_nombre.lower())
#REPLAZAR TEXT EN UNA CADENA
frase="Me gusta programacion"
print(frase.replace("programacion","matematicas"))
#FORMATO DE CADENAS (F-String)
edad=16
Nombre='Darina'
mensaje=f"Hola,me llamo {Nombre} y tengo {edad} años"
print(mensaje)
#CONTAR LOS CARACTERES DE UNA CADENA
texto="iFelicidades por aun continuar en el CECY!!!"
cantidad_caracteres=len(texto)
print(cantidad_caracteres)
#COMPROBAR SI UN TEXTO CONTIENE UNA PALABRA
oracion="Aprender python es divertido"
if "Java" in oracion:
    print("Encontrado")
else:
    print("No esta")
#VALIDAR CONTENIDO EN UNA CADENA
nlista="Darina"
print(nlista.isalpha())
print(nlista.isdigit())