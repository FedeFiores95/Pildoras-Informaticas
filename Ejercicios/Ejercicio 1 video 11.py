num1=int(input("Ingrese el primer número: "))
num2=int(input("Ingrese el segundo número: "))

def DevuelveMax(n1,n2):
	if n1 > n2:
		print (n1)
	elif n2 > n1:
		print (n2)
	else:
		print("Son iguales")

print("El número mas alto es: ")

print(DevuelveMax(num1,num2))