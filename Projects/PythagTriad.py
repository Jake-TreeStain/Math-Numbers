#...PY-thagorean Triads...#
#....By Tristan Arthur....#
#        03/04/2016       #

cap = 1000
start = 1
results = 0

for a in range(start, cap):
    for b in range(start, a):
        c = (a ** 2 + b ** 2) ** 0.5
        if c % 1 == 0: #Is c a whole number/Integer
            print("{x}={y}+{z}".format(x=int(c), y=a, z=b))
            results += 1

print("results: {res}".format(res=results))
save_file = open("saved_results.txt", "a+")
save_file.write("While {s} < a&b < {c} results = {r}\n".format(r=results//2, c=cap, s=start-1))
