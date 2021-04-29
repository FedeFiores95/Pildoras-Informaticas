from io import open

archivo_texto=open("archivo.txt","w")

frase="Estupendo dia para estudiar python"

archivo_texto.write(frase)

archivo_texto.close()

archivo_texto=open("archivo.txt","r")

texto=archivo_texto.read()

print(texto)

archivo_texto.close()

print("OK")