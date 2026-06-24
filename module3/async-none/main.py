import time

def make_coffee():
    print("Start coffee")
    print("Coffee brewing (3 seconds)...")
    time.sleep(3)
    print("Coffee done")

def make_toast():
    print("Start toast")
    print("Toast toasting (2 seconds)...")
    time.sleep(2)
    print("Toast done")

start = time.perf_counter()

make_coffee()
make_toast()

end = time.perf_counter()

print(f"\nTotal duration: {end - start:.2f} seconds")