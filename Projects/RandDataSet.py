import random

min_value = int(input("Minimum value: "))
max_value = int(input("Maximum value: "))
num_value = int(input("Number of values: "))

for num in range(num_value):
    print(str(random.randint(min_value, max_value)) + ", ", end="")
print()
