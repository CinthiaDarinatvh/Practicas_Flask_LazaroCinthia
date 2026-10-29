#Realizar un programa que calcula
#La compra total de cuatro productos
#Es mayor a 2000 pesos que me haga un descuento
#Del 10%
#DATOS DE ENTRADA
precio1=float(input("Introduce el precio del producto 1"))
precio2=float(input("Introduce el precio del producto 2"))
precio3=float(input("Introduce el precio del producto 3"))
precio4=float(input("Introduce el precio del producto 4"))
#PROCESO
total=precio1+precio2+precio3+precio4
if total>2000:
    total=(total-(total*.10))
    #TOTAL=(3000-)(3000*,10)) TOTAL=2700
    print(total)
else:
    print("NO TIENES DESCUENTO")