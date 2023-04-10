"""
Author:Diego Aguilar 4IV8
"""
import tkinter as tk
from tkinter import ttk

class Traductor(ttk.Frame):
    def __init__(self,parent):
        self.Diccionario = []
        self.leerDiccionario()
        super().__init__(parent)
        
        self.texto_esp = tk.Label(parent, text="Palabra en español:")
        self.texto_esp.place(x = 30, y=110)

        self.txt_esp = tk.Entry(parent)
        self.txt_esp.place(x=190,y=110)

        self.texto_eng = tk.Label(parent, text="Palabra en inglés:")
        self.texto_eng.place(x=30, y=140)

        self.txt_eng = tk.Entry(parent)
        self.txt_eng.place(x=190,y=140)

        self.btnAgregar = ttk.Button(parent, text="Agregar al diccionario", command=self.añadir_palabra)
        self.btnAgregar.place(x= 320,y=120)

        self.btndic = ttk.Button(parent, text="Mostrar diccionario", command=self.mostrarDic)
        self.btndic.place(x =450, y= 310)
        
        self.texto_dic = tk.Label(parent, text="")
        self.texto_dic.place(x=600, y=0)

        self.texto_filtro = tk.Label(parent, text="Buscar en el diccionario(filtro por letras):")
        self.texto_filtro.place(x = 30, y=20)

        self.txt_filtro = tk.Entry(parent)
        self.txt_filtro.place(x=245,y=20)

        self.btnFiltrar = ttk.Button(parent, text="Filtrar", command=self.filtro)
        self.btnFiltrar.place(x =370, y= 15)
        
        self.filtrado= tk.Label(parent,text="")
        self.filtrado.place(x=450, y=10)

        self.texto_frase = tk.Label(parent, text="Frase en español:")
        self.texto_frase.place(x = 30, y=50)

        self.txt_frase = tk.Entry(parent)
        self.txt_frase.place(x=120,y=50)

        self.btn_Traducir = ttk.Button(parent, text="Traducir", command=self.traducir)
        self.btn_Traducir.place(x=250,y=45)

        self.texto_traducido = tk.Label(parent, text="Traducción en inglés:")
        self.texto_traducido.place(x=325,y=50)
        
        self.archivo = open("Diccionario.txt","a+",encoding="utf8")
        
    def leerDiccionario(self):
        try:
            with open("Diccionario.txt", "r", encoding="utf8") as archivo:
                for linea in archivo:
                    palabra = linea.strip().split(",")
                    self.Diccionario.append((palabra[0], palabra[1]))
        except FileNotFoundError:
            print("El archivo del diccionario no existe todavía.")
            
    def añadir_palabra(self):
        espalabra = self.txt_esp.get()
        engpalabra = self.txt_eng.get()
        self.Diccionario.append((espalabra, engpalabra))
        self.txt_esp.delete(0, tk.END)
        self.txt_eng.delete(0, tk.END)
        with open("Diccionario.txt", "a+", encoding="utf8") as archivo:
            for palabra in self.Diccionario:
                archivo.write(f"{palabra[0]},{palabra[1]}\n")
            print("Cambios guardados exitosamente.")
        
    def mostrarDic(self):
        with open('Diccionario.txt', 'r',encoding="utf8") as archivo:
            contenido = archivo.read()
            lineas = contenido.splitlines()
            dictex = '\n'.join(lineas)
            self.texto_dic.config(text=dictex)
        

    def filtro(self):
        letra = self.txt_filtro.get().lower()
        filtrado = [palabra for palabra in self.Diccionario if palabra[0].lower().startswith(letra)]
        tfiltrado =""
        for palabra in filtrado:
            tfiltrado += f"{palabra[0]} - {palabra[1]}\n"
        self.filtrado.config(text=tfiltrado)

    def traducir(self):
        espfrase = self.txt_frase.get()
        palabras = espfrase.split()
        engfrase = ""
        for palabra in palabras:
            encontrada = False
            for esp, eng in self.Diccionario:
                if palabra == esp:
                    engfrase += eng + " "
                    encontrada = True
                    break
            if not encontrada:
                engfrase += palabra + " "
        self.texto_traducido.config(text=engfrase)
    



ventana = tk.Tk()
ventana.title("Diccionario Español-Inglés Aguilar Flores Diego 4IV8")
ventana.geometry("950x500")
traduc = Traductor(ventana)
ventana.mainloop()