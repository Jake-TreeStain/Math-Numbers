start = 1
cap = 100
results = 0

for num in range(start, cap):
    if num % 2 != 0 or num % 5 != 0:
        prime = 0
        for divide in range(start, num):
            if num % divide == 0:
                primitive += 1
        if prime == 1:
            print(num)
            results += 1
print(results)
