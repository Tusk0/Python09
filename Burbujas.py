#Author: Aguilar Flores Diego 4IV8
#Title: Burbujas
def DATOS():
    lista=[]
    while True:
        o=int(input("Ingresa los numeros para ordenar e ingresa 0 para finalizar:"))
        if o==0:
            return lista
        else:
            lista.append(o)
    return lista
def ORDEN(lista):
    long=len(lista)
    for u in range(0,long):
        for d in range(0,long-1):
            if lista[d]>lista[d+1]:
                otro=lista[d]
                lista[d]=lista[d+1]
                lista[d+1]=otro
    return lista

lista=DATOS()
lista=ORDEN(lista)
print("Lista ordenada de mayor a menor:")
print(lista)