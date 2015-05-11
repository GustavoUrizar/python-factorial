"""Factorial"""



def factorial(number):
	if number > 0:
		fact = number * factorial(number -1)
		return fact
	else:
		number == 0
		return 1


	
