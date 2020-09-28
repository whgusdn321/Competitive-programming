tc = int(input())
for t in range(tc):
    n = int(input())
    s = input()
    m = n-1
    new_str = ""
    for i in range(n):
        new_str += s[m]
    print(new_str)