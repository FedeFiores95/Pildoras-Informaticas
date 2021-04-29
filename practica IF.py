print("Evaluación de notas de alumnos")

nota_alumno=input("Introduzca la nota del alumno: ")

def evaluacion(nota): #Funcion
	valoracion="aprobado"
	if nota<7:
		valoracion="desaprobado"
	return valoracion

print(evaluacion(int(nota_alumno)))