# IF = Si condicional
# Else = Si no es verdad

print("Verificación de acceso")

edad_usuario=int(input("Introduzca su edad: "))

if edad_usuario<18:
	print("No puedes entrar")
elif edad_usuario>100:
		print("Edad incorrecta")
else:
	print("Puedes Pasar")
		