from tkinter import *

raiz = Tk()

raiz.title("Ventana de pruebas")

raiz.resizable(1,1)

raiz.iconbitmap("A:\Fede\python\Ejercicios Pildoras\graficos\explosion.ico")

raiz.geometry("350x180")

raiz.config(bg="black")

miFrame=Frame(raiz)
miFrame.pack()

miLabel=Label(miFrame, text="Hola alumnos de Python")
miLabel.pack()


miFrame.config(bg="green",width="50",height="80")

raiz.mainloop() #esta instruccion debe estar siempre
                #al final de la construccion de la ventana
