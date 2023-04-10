"""
Author: Aguilar Flores Diego 4IV8 
"""


cubos =0
altura=0
counter= 0
piezas="*"
a=1

cubos=int(input("Introduzca la cantidad de cubos para construir la piramide: ")) 

if cubos>0:
    for a in range(1,cubos):
        if cubos>0:
            cubos=cubos-a
            a+=1
            altura+=1  

    if cubos<0:
        cubos+=altura
        altura-=1
    elif cubos==0:
        cubos=cubos
        altura=altura

    print ("La altura de la piramide es: ",altura)
    print("Sobran: ",cubos,- " cubos")
    print("La piramide es: ")
elif cubos<0:
    print("No ingresar negativos para la piramide")    

for n in range(0,altura+1):
    print(n*piezas," ")

if cubos == 0:
    print("El residuo es: 0")
elif cubos != 0:
    print("El residuo es: ",cubos, " cubos")
