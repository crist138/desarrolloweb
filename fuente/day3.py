# Ejercicio para ver si un numero esta dentro de un rango :)

n1 = int(input('Ingresa el valor uno: '))

valorminimo = 0
valormaximo = 5

estaenrango = (valorminimo <= n1) and (valormaximo >= n1) # Expresiones Booleanas

if estaenrango:
	print(f'El numero {n1} esta dentro de rango')
else:
	print(f'El numero {n1} NO esta dentro de rango')