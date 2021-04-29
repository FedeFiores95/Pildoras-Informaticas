import math

edad=int(input("Introduce tu edad: "))

while edad<=0 or edad>100:
	print("Has introducido una edad incorrecta. Vuelve a intentarlo")
	edad=int(input("Introduce tu edad: "))

print(f"Tu edad es {edad}")

print("¨Programa de cálculo de raíz cuadrada")
numero=int(input("Introduce un numero: "))

intentos=0

while numero<=0:
	print("No se puede hallar la raíz de un numero negativo")

	if intentos==2:
		print("Has intentado demasiadas veces. El programa finalizará")
		break;

	numero=int(input("Introduce un numero: "))

if intentos<2:
	solucion=math.sqrt(numero)
	print("La raíz cuadrada de "+ str(numero) + " es " + str(solucion))
