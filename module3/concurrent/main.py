import asyncio


async def display_even_numbers(limit: int) -> None:
	for number in range(0, limit + 1, 2):
		print(f"Even: {number}")
		await asyncio.sleep(0)


async def display_odd_numbers(limit: int) -> None:
	for number in range(1, limit + 1, 2):
		print(f"Odd: {number}")
		await asyncio.sleep(0)


async def main() -> None:
	limit = 5000
	await asyncio.gather(
		display_even_numbers(limit),
		display_odd_numbers(limit),
	)


if __name__ == "__main__":
	asyncio.run(main())
