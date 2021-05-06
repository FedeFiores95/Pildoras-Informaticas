from tkinter import *

root=Tk()
root.iconbitmap("A:\Fede\python\Ejercicios Pildoras\graficos\explosion.ico")

miFrame=Frame(root, width=500, height=400)

miFrame.pack()

miLabel=Label(miFrame, text="Hola alumnos de Python",fg="blue")
miLabel.place(x=10,y=380)

root.mainloop()