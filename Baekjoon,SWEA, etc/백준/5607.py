factorials = [0]
f = 1
for i in range(1, 1000001):
    f *= i
    factorials.append(f)('factorials : ',factorials)