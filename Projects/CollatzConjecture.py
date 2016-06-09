num = int(input("Input Positive Integer: "))
load = input("Load (True/*)?: ")

step = 0

while num != 1:
    if num % 2 == 0:
        num = num // 2
    else:
        num = num * 3 + 1
    if load == "True":
        print(num)
    step += 1

print("{x} Steps.".format(x=step))
