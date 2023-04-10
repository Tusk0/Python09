#MULTIPLOS DE 3
lista = []
i = int(input("Ingrese un numero para iniciar xd"))
while i != 0:
    e = int(input("Ingrese numeros para filtrar (0 para parar)"))
    if(e != 0):
        lista.append(e)
    else:
        break

def filtrito(lista):
    if  e % 3 == 0:
        for e in lista:
            print(lista[e])

lista=filtrito(lista)