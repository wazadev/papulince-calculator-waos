import os
from tkinter import *
import numpy as np  # Importar NumPy para álgebra lineal
import math
from tkinter import messagebox
import pygame

# Variables globales para el idioma
IDIOMA = "español"
pygame.mixer.init()

# Ruta de los archivos de audio
CARPETA_AUDIO = os.path.dirname(__file__)
ARCHIVO_ESPANOL = os.path.join(CARPETA_AUDIO, "español.wav")
ARCHIVO_ENGLISH = os.path.join(CARPETA_AUDIO, "english.wav")

# Funciones científicas
def sin():
    try:
        resultado_entry.delete(0, END)
        resultado_entry.insert(END, math.sin(float(entrada_entry.get())))
    except ValueError:
        resultado_entry.delete(0, END)
        resultado_entry.insert(END, "Error")

def cos():
    try:
        resultado_entry.delete(0, END)
        resultado_entry.insert(END, math.cos(float(entrada_entry.get())))
    except ValueError:
        resultado_entry.delete(0, END)
        resultado_entry.insert(END, "Error")

def tan():
    try:
        resultado_entry.delete(0, END)
        resultado_entry.insert(END, math.tan(float(entrada_entry.get())))
    except ValueError:
        resultado_entry.delete(0, END)
        resultado_entry.insert(END, "Error")

def exp():
    try:
        resultado_entry.delete(0, END)
        resultado_entry.insert(END, math.exp(float(entrada_entry.get())))
    except ValueError:
        resultado_entry.delete(0, END)
        resultado_entry.insert(END, "Error")

def log():
    try:
        resultado_entry.delete(0, END)
        resultado_entry.insert(END, math.log(float(entrada_entry.get())))
    except ValueError:
        resultado_entry.delete(0, END)
        resultado_entry.insert(END, "Error")

def calcular():
    operacion = entrada_entry.get()
    
    if operacion == "pi":
        resultado_entry.delete(0, END)
        resultado_entry.insert(END, "3.1416")
    else:
        try:
            resultado = eval(operacion)
            resultado_entry.delete(0, END)
            resultado_entry.insert(END, resultado)
            entrada_entry.delete(0, END)
            entrada_entry.insert(END, operacion)  # Mostrar la operación en la entrada superior
        except:
            resultado_entry.delete(0, END)
            resultado_entry.insert(END, "Error")

# Función para cambiar el idioma
def cambiar_idioma():
    global IDIOMA
    if IDIOMA == "español":
        IDIOMA = "english"
        pygame.mixer.music.load(ARCHIVO_ENGLISH)
        pygame.mixer.music.play()
    else:
        IDIOMA = "español"
        pygame.mixer.music.load(ARCHIVO_ESPANOL)
        pygame.mixer.music.play()
    actualizar_idioma()

# Función para actualizar los textos según el idioma seleccionado
def actualizar_idioma():
    if IDIOMA == "español":
        boton_language.config(text="Language")
        boton_fractales.config(text="Fractales")
        boton_resultado.config(text="Resultado")
        boton_algebra.config(text="Álgebra Lineal")
    else:
        boton_language.config(text="Idioma")
        boton_fractales.config(text="Fractals")
        boton_resultado.config(text="Result")
        boton_algebra.config(text="Linear Algebra")

# Función para abrir la ventana de Álgebra Lineal
def abrir_ventana_algebra():
    ventana_algebra = Toplevel(ventana)
    ventana_algebra.title("Álgebra Lineal")
    
    # Definir botones y funcionalidades para la pantalla de operaciones de Álgebra Lineal
    matriz_a = np.array([[1, 2], [3, 4]])  # Ejemplo de matriz
    
    lbl_operaciones = Label(ventana_algebra, text="Operaciones:")
    lbl_operaciones.grid(row=0, column=0, padx=5, pady=5)
    
    btn_determinante = Button(ventana_algebra, text="Determinante", command=lambda: calcular_determinante(matriz_a))
    btn_determinante.grid(row=1, column=0, padx=5, pady=5)
    
    btn_inversa = Button(ventana_algebra, text="Inversa", command=lambda: calcular_inversa(matriz_a))
    btn_inversa.grid(row=1, column=1, padx=5, pady=5)
    
    btn_transpuesta = Button(ventana_algebra, text="Transpuesta", command=lambda: calcular_transpuesta(matriz_a))
    btn_transpuesta.grid(row=1, column=2, padx=5, pady=5)
    
    btn_producto_punto = Button(ventana_algebra, text="Producto Punto", command=lambda: calcular_producto_punto(matriz_a, matriz_a))
    btn_producto_punto.grid(row=2, column=0, padx=5, pady=5)
    
    btn_producto_cruz = Button(ventana_algebra, text="Producto Cruz", command=lambda: calcular_producto_cruz(matriz_a, matriz_a))
    btn_producto_cruz.grid(row=2, column=1, padx=5, pady=5)
    
    btn_diagonalizacion = Button(ventana_algebra, text="Diagonalización", command=lambda: calcular_diagonalizacion(matriz_a))
    btn_diagonalizacion.grid(row=2, column=2, padx=5, pady=5)
    
    # Definir botones y funcionalidades para la pantalla de resultado de Álgebra Lineal
    lbl_resultado = Label(ventana_algebra, text="Resultado:")
    lbl_resultado.grid(row=3, column=0, padx=5, pady=5)
    
    lbl_resultado_texto = Label(ventana_algebra, text="")
    lbl_resultado_texto.grid(row=4, column=0, padx=5, pady=5)
    
# Función para calcular el determinante de una matriz
def calcular_determinante(matriz):
    determinante = np.linalg.det(matriz)
    lbl_resultado_texto.config(text=str(determinante))
    
# Función para calcular la inversa de una matriz
def calcular_inversa(matriz):
    inversa = np.linalg.inv(matriz)
    lbl_resultado_texto.config(text=str(inversa))
    
# Función para calcular la transpuesta de una matriz
def calcular_transpuesta(matriz):
    transpuesta = np.transpose(matriz)
    lbl_resultado_texto.config(text=str(transpuesta))

# Función para calcular el producto punto de dos matrices
def calcular_producto_punto(matriz_a, matriz_b):
    producto_punto = np.dot(matriz_a, matriz_b)
    lbl_resultado_texto.config(text=str(producto_punto))
    
# Función para calcular el producto cruz de dos matrices
def calcular_producto_cruz(matriz_a, matriz_b):
    producto_cruz = np.cross(matriz_a, matriz_b)
    lbl_resultado_texto.config(text=str(producto_cruz))

# Función para calcular la diagonalización de una matriz
def calcular_diagonalizacion(matriz):
    valores_propios, vectores_propios = np.linalg.eig(matriz)
    lbl_resultado_texto.config(text="Valores Propios:\n{}\n\nVectores Propios:\n{}".format(valores_propios, vectores_propios))

# Crear ventana principal
ventana = Tk()
ventana.geometry("600x400")  # Ventana más grande
ventana.title("Calculadora Científica")

# Widgets Entry
entrada_entry = Entry(ventana)
entrada_entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

resultado_entry = Entry(ventana)
resultado_entry.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

# Botones
botones = [
    ("sin", 2, 0), ("cos", 2, 1), ("tan", 2, 2), ("exp", 2, 3),
    ("log", 3, 0), ("7", 3, 1), ("8", 3, 2), ("9", 3, 3),
    ("4", 4, 0), ("5", 4, 1), ("6", 4, 2), ("*", 4, 3),
    ("1", 5, 0), ("2", 5, 1), ("3", 5, 2), ("-", 5, 3),
    ("0", 6, 0), (".", 6, 1), ("=", 6, 2), ("/", 6, 3),
    ("π", 7, 0), ("AC", 7, 1), ("Resultado", 7, 2), ("+", 7, 3),
    ("Fractales", 8, 0)
]

for (texto, fila, columna) in botones:
    if texto == "Fractales":
        boton_fractales = Button(ventana, text=texto, width=15, command=lambda: messagebox.showinfo("Fractales", "Animaciones de fractales"))
        boton_fractales.grid(row=fila, column=columna, padx=5, pady=5)
    elif texto == "AC":
        boton = Button(ventana, text=texto, width=15, command=lambda: entrada_entry.delete(0, END))
        boton.grid(row=fila, column=columna, padx=5, pady=5)
    elif texto == "=":
        boton = Button(ventana, text=texto, width=5, command=calcular)
        boton.grid(row=fila, column=columna, padx=5, pady=5)
    elif texto == "Resultado":
        boton_resultado = Button(ventana, text=texto, width=10, command=calcular)
        boton_resultado.grid(row=fila, column=columna, padx=5, pady=5)
    elif texto == "π":
        boton = Button(ventana, text=texto, width=5, command=lambda c=texto: entrada_entry.insert(END, "pi"))
        boton.grid(row=fila, column=columna, padx=5, pady=5)
    else:
        comando = globals().get(texto, lambda: None)
        boton = Button(ventana, text=texto, width=5, command=lambda c=texto: entrada_entry.insert(END, c))
        boton.grid(row=fila, column=columna, padx=5, pady=5)

# Botón de idioma
boton_language = Button(ventana, text="Idioma", width=10, command=cambiar_idioma)
boton_language.grid(row=8, column=1, padx=5, pady=5)

# Botón de Álgebra Lineal
boton_algebra = Button(ventana, text="Álgebra Lineal", width=15, command=abrir_ventana_algebra)
boton_algebra.grid(row=8, column=0, padx=5, pady=5)

# Actualizar el idioma inicial
actualizar_idioma()

# Main loop
ventana.mainloop()

