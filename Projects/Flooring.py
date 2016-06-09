width = int(input("Width of floor (m): "))
breadth = int(input("Breadth of floor (m): "))
cost = float(input("Tile cost per (m)^2: "))

area = width * breadth
total_cost = area * cost
print("${t} for {c}^2 of flooring".format(t=total_cost, c=area))

