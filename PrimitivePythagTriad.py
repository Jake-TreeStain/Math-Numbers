#...Primitive PY-thagorean Triads...#
#.........By Tristan Arthur.........#
#             03/04/2016            #

cap = 1300000
start = 1000000
results = 0
prime_count = 0

for a in range(start, cap):
    for b in range(start, a):
        c = (a ** 2 + b ** 2) ** 0.5
        if c % 1 == 0 and c % 2 != 0 or c % 5 != 0: #Is c a odd whole number?
            prime_count = 0 #Reset previous prime variable
            for divisible in range(start, int(c)): #Loop through start < divisible++ < c
                if c % divisible == 0: #Is c / divisible an integer?
                    prime_count += 1 #Increment prime count
            if prime_count == 1: #Is c a prime number?
                print("{x}={y}+{z}".format(x=int(c), y=a, z=b))
                results += 1

print("results: {res}".format(res=results))
save_file = open("saved_results.txt", "a+")
save_file.write("While {s} < a&b < {c} PRIMITIVE results = {r}\n".format(r=results//2, c=cap, s=start-1))
