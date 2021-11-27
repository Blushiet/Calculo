import matplotlib.pyplot as plt
from matplotlib.pyplot import *
from matplotlib.figure import Figure
from matplotlib import style
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import numpy as np
from math import *
import matplotlib.animation as anim
import tkinter as tk
from tkinter import ttk, messagebox
import sympy as s


rang1 = False
rang2 = ""
rang3 = ""


def ver():
    win = tk.Tk()
    win.title("Graficadora de funciones")
    win.geometry("900x700")
    style.use("fivethirtyeight")
    fig = Figure()
    ax = fig.add_subplot(111)

    cvs = FigureCanvasTkAgg(fig, win)
    cvs.draw()
    cvs.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    tlb = NavigationToolbar2Tk(cvs, win)
    tlb.update()
    cvs.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def Reemplazar(a):
        fun = {'cos': 'np.cos'}
        fun1 = {"sen": "np.sin"}
        fun2 = {"tan": "np.tan"}
        fun3 = {"ln": "np.log"}
        fun4 = {"e": "np.exp"}
        for k in fun1:
            for k1 in fun:
                for k2 in fun2:
                    for k3 in fun3:
                        for k4 in fun4:
                            if k in a:
                                a = a.replace(k, fun1[k])
                            elif k1 in a:
                                a = a.replace(k1, fun[k1])
                            elif k2 in a:
                                a = a.replace(k2, fun2[k2])
                            elif k3 in a:
                                a = a.replace(k3, fun3[k3])
                            else:
                                a = a.replace(k4, fun4[k4])
                return a



    def animate(i):
        global rang1
        global rang2
        global rang3
        if rang1 == True:
            try:
                min = float(rang3[0]);
                max = float(rang3[1])
                if min < max:
                    x = np.arange(min, max, 0.01)
                    rang2 = [min, max]
                else:
                    rang1 = False
            except:
                messagebox.showwarning("El rango es incorrecto")
                rang1 = False
                entra_var.delete(0, len(entra_var.get()))
            else:
                if rang2 != "":
                    x = np.arange(rang2[0], rang2[1], 0.01)
                else:
                    x = np.arange(-20, 20, 0.01)
            try:
                sl = eval(graf_dt)
                ax.clear()
                ax.plot(x, sl)
            except:
                ax.plot()
            ax.axhline(0, color="black")
            ax.axvline(0, color="black")
            ani.event_source.stop()

    def representar():
        global graf_dt
        global rang3
        global rang1
        tx_original = entra_func.get()
        if entra_var.get() != "":
            rann = entra_var.get()
            rang3 = rann.split(",")
            rang1 = True
        graf_dt = Reemplazar(tx_original)
        ani.event_source.start()

    ani = anim.FuncAnimation(fig, animate, interval=100)
    plt.show()

    bo1 = tk.Button(win, text="Graficar", command=representar)
    bo1.pack(side=tk.LEFT)
    entra_func = tk.Entry(win, width=60)
    entra_func.pack(side=tk.BOTTOM)
    entra_var = tk.Entry(win, width=20)
    entra_var.pack(side=tk.RIGHT)

    win.mainloop()


ver()
