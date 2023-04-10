"""
Utiliza la ejecución condicional y la instrucción continue para "comer" las siguientes vocales A , E , I , O , U de la palabra ingresada. 
Imprime las letras no consumidas en la pantalla, cada una de ellas en una línea separada.
Author: Aguilar Flores Diego 4IV8
"""

palabra = input("Ingresa una palabra: ")
palabra = palabra.upper()
for vocal in palabra:
    if vocal == "A" or vocal == "E" or vocal == "I" or vocal == "O" or vocal == "U":
        continue
        
    print(vocal)
        