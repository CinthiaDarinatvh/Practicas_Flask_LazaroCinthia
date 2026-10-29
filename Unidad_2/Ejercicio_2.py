numero=int(input("ingresa un numero del 1 al 10:"))
if numero >= 1 and numero <= 10:
    print("tabla de multiplicar del", numero)
    i = 1
    while i <= 10:
        resultado = numero * i
        print(numero,"x", i, "=",resultado)
        i = i + 1
else:
    print("Error:El numero debe estar entre 1 y 10")