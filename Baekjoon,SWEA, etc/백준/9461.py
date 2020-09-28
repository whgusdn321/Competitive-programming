test_cases = int(input())
a = [0] *101
#[-1, 1, 1, 1, 2, 2, 3, 4, ]
a[1] = 1
a[2] = 1
a[3] = 1
a[4] = 2
a[5] = 2
#a[6] = 3
#a[7] = 4
#a[8] = 5
for i in range(6, 101):
    a[i] = a[i-1] +a[i-5]
for test_case in range(test_cases):
    n = int(input())
    print(a[n])