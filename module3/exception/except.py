def main():
	try:
		result = 10 / 0
		print(result)
	except Exception as error:
		print(f"Caught an exception: {error}")


if __name__ == "__main__":
	main()
