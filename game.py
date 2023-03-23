from random import choice, randrange
from datetime import datetime
# Operadores posibles

# Cantidad de cuentas a resolver
times = 5
score = 0
# Contador inicial de tiempo.
# Esto toma la fecha y hora actual.
init_time = datetime.now()
print(f"¡Veremos cuanto tardas en responder estas {times} operaciones!")
for i in range(0, times):
# Se eligen números y operador al azar
	number_1 = randrange(10)
	number_2 = randrange(10)
	operators = ["+", "-", "*", "/"]

	operator = choice(operators)

	if operator == operators[3]:
		while number_2 == 0 :
			number_2 = randrange(10)

	print(f"{i+1}- ¿Cuánto es {number_1} {operator} {number_2}?")
	# Le pedimos al usuario el resultado
	result = input("resultado: ")

	if operator == operators[0]:
		real_result = number_1+number_2
	if operator == operators[1]:
		real_result = number_1-number_2
	if operator == operators[2]:
		real_result = number_1*number_2
	if operator == operators[3]:
		real_result = number_1/number_2

	if operator == operators[3] :
		if abs(float(result) - real_result)<1e-5:
			print('El resultado es correcto')
			score=score+1
		else :
			print('El resultado es incorrecto')
	else:
		if(int(result) == real_result):
			print('El resultado es correcto')
			score=score+1
		else :
			print('El resultado es incorrecto')

	operators=[]
# Al terminar toda la cantidad de cuentas por resolver.
# Se vuelve a tomar la fecha y la hora.
end_time = datetime.now()
# Restando las fechas obtenemos el tiempo transcurrido.
total_time = end_time - init_time
# Mostramos ese tiempo en segundos.
print(f"\n Tardaste {total_time.seconds} segundos, con un score final de {score} sobre {times}.")
