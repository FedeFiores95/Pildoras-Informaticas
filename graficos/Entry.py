from tkinter import *

#Raiz de la ventana
raiz=Tk()

#1er Frame
miFrame=Frame(raiz, width=800, height=300)
miFrame.pack()

#variable de codigo boton
minombre=StringVar()

#widget entry
cuadroNombre=Entry(miFrame, textvariable=minombre)
cuadroNombre.grid(row=1, column=2, sticky="w", padx=10, pady=5)

#widget Label
nombreLabel=Label(miFrame, text="Nombre: ")
nombreLabel.grid(row=1, column=1, sticky="w", padx=10, pady=5)

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=2, column=2, sticky="w", padx=10, pady=5)

apellidoLabel=Label(miFrame, text="Apellido: ")
apellidoLabel.grid(row=2, column=1, sticky="w", padx=10, pady=5)

cuadroPass=Entry(miFrame)
cuadroPass.grid(row=3, column=2, sticky="w", padx=10, pady=5)
cuadroPass.config(show="*")

PassLabel=Label(miFrame, text="Password: ")
PassLabel.grid(row=3, column=1, sticky="w", padx=10, pady=5)

#widget text
textoComentarios=Text(miFrame, width=25, height=9,)
textoComentarios.grid(row=4, column=2, sticky="w", padx=10, pady=5)

comentariosLabel=Label(miFrame, text="Comentarios: ")
comentariosLabel.grid(row=4, column=1, sticky="w", padx=10, pady=5)

#widget barra de scroll Vertical
scrollVert=Scrollbar(miFrame, command=textoComentarios.yview)
scrollVert.grid(row=4,column=3, sticky="nsew")
textoComentarios.config(yscrollcommand=scrollVert.set)

#codigo boton
def codigoBoton():

    minombre.set("Fede")

#Botones
botonEnviar=Button(miFrame, text="Enviar", command=codigoBoton)
botonEnviar.grid(row=5,column=2, sticky="w")


raiz.mainloop()