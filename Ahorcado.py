# -*- coding: utf-8 -*-
"""
Created on Sat Apr 01 15:24:41 2023

@author: Diego
"""
import random


palabras = ['ROJO','AZUL','VERDE','LISTA','OBTUSO','VECTOR','OTORRINOLARINGOLOGO','PERRO','GATO','SISTEMAS','PROGRAMA','PYTHON','JAVAGOD','LIMA','LIMON','CIELO','TECLADO','CAFE','TAZA','CEBRA','ULTIMO','FILO','TAZO','CEREBRO','DOCTOR','QUESO','PIZZA','HAMBURGUESA','PIÑA','MANZANA','NARANJA','PERA','PEZ','FE','WEB','MOUSE','CARBON','LAPIZ','REPTIL','ZOMBIE','POLIMORFISMO','ENCAPSULAMIENTO','ABSTRACCION','HERENCIA','BASE','FUERTE','PAPEL','PIEDRA','TIJERAS','REGLA','RESORTE']
partida = random.choice(palabras)

def juego(partida):
    guiones = '_' * len(partida)
    intentos = 6 
    adivinado = False
    intentadas=[]
    
    print("Juega al ahorcado y no me dejes colgado xd")
    print(mostrarPostes(intentos))
    print(guiones)
    print()
    while not adivinado and intentos > 0:
        letra= input("Ingresa una letra ").upper()
        if len(letra) == 1 and letra.isalpha():
            if letra in intentadas:
                print("Ya intentaste con esa letra")
                print(mostrarPostes(intentos))
            elif letra not in partida:
                print("Esa letra no está en la palabra")
                intentos -=1
                intentadas.append(letra)
                print(mostrarPostes(intentos))
            else:
                print("La letra que ingresaste si esta en la palabra")
                print(mostrarPostes(intentos))
                intentadas.append(letra)
                palabra_lista= list(guiones)
                indice = [i for i, intento in enumerate(partida) if intento == letra]
                for index in indice:
                    palabra_lista[index] = letra
                guiones = ''.join(palabra_lista)
                if '_' not in palabra_lista:
                    adivinado = True
        else:
            print("Ingrese solo una letra")
            print(mostrarPostes(intentos))
        print(guiones)
        print()
    if adivinado:
        print("Felicidades,ganaste")
        print(mostrarPostes(intentos))
    else:
        print("PERDISTE")
        print(mostrarPostes(intentos))

                
    
def mostrarPostes(intentos):
    ahorcado = {0:
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |     | |
                   -
                """,1:
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |     | 
                   -
                """,2:
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      
                   -
                """,3:
                """
                   --------
                   |      |
                   |      O
                   |     \|
                   |      
                   -
                """,4:
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |     
                   -
                """,5:
                """
                   --------
                   |      |
                   |      O
                   |    
                   |     
                   -
                """,6:
                """
                   --------
                   |      |
                   |      
                   |      
                   |
                   """
                }
    return ahorcado.get(intentos)

juego(partida)
