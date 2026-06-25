def factorial(number: int) -> int:
	if number < 0:
		raise ValueError("factorial is undefined for negative numbers")

	result = 1
	for value in range(2, number + 1):
		result *= value

	return result
