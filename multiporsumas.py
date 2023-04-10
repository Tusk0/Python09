
"""
Created on Tue Jan 31 15:49:44 2023

@author: yo
"""

multiplicador = 0
multiplicando = 0
resultado=0

multiplicando=int(input("Introduce el multiplicando: "))
multiplicador=int(input("Introduce el multiplicador: "))

if (multiplicador >0):
    while multiplicador >0:
        resultado+=multiplicando
        multiplicador-=1
elif multiplicador <0:
    while multiplicador <0:
        resultado-=multiplicando
        multiplicador+=1
        
print("El resultado de la multiplicacion con sumas es: ", resultado)