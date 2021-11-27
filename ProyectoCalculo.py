import tkinter as tk
from tkinter import ttk, messagebox
import sympy as s

import VentanaGrafica.Grafica
from VentanaGrafica import *


def VerVentanaNueva():
    VentanaGrafica.Grafica.ver()

def Integrar():
    if CajaLI.get() != "" and CajaLS.get() != "":
        ResultadoIntegralFuncion.delete(0, "end")
        ResultadoIntegralDefinida.delete(0, "end")
        i = s.symbols('x')
        fx = CajaFun.get()
        fx2 = CajaFun.get()
        LI = float(CajaLI.get())
        LS = float(CajaLS.get())
        dx = s.Integral(fx, (i, LI, LS)).doit()
        dx2 = s.Integral(fx2, i).doit()
        ResultadoIntegralFuncion.insert(0, dx2)
        ResultadoIntegralDefinida.insert(0, dx)
    else:
        ResultadoIntegralFuncion.delete(0, "end")
        ResultadoIntegralDefinida.delete(0, "end")
        x = s.symbols('x')
        fx = CajaFun.get()
        dx = s.Integral(fx, x).doit()
        ResultadoIntegralFuncion.insert(0, dx)
        print(dx)


raiz = tk.Tk()
raiz.geometry("600x500")
raiz.title("Calculo Integral UADEC")
#Labels
IngresarFuncion = tk.Label(raiz, text="Ingrese la función: ", font="Monospaced").place(x = 10, y = 10)
LimiteInferior = tk.Label(raiz, text="Limite Inferior: ", font="Monospaced").place(x=10, y=70)
LimiteSuperior = tk.Label(raiz, text="Limite Superior: ", font="Monospaced").place(x=10, y=140)
EtiquetaRIntegral = tk.Label(raiz, text="Resultado de la integral en funcion:", font="Monospaced").place(x=10, y=235)
EtiquetaIntegralD = tk.Label(raiz, text="Resultado de la integral evaluada:", font="Monospaced").place(x=10, y=325)
#Cajas de texto
CajaFun = tk.Entry(raiz, font="Monospaced")
CajaFun.place(x=225, y=10)
CajaLI = ttk.Entry(raiz, font="Monospaced")
CajaLI.place(x=225, y=70)
CajaLS = ttk.Entry(raiz, font="Monospaced")
CajaLS.place(x=225, y=140)
#Botones
Calcular = tk.Button(raiz, font="Monospadec", text="Calcular", command=Integrar).place(x=120, y=180)
Graficar = tk.Button(raiz, font="Monospaced", text="Graficar", command=VerVentanaNueva).place(x=200, y=180)
#ResultadoFuncionesIntegradas
ResultadoIntegralFuncion = ttk.Entry(raiz, font="Monospaced", width=50)
ResultadoIntegralFuncion.place(x=10, y=260)
ResultadoIntegralDefinida = tk.Entry(raiz, font="Monospaced", width=50)
ResultadoIntegralDefinida.place(x=10, y=350)
raiz.mainloop()