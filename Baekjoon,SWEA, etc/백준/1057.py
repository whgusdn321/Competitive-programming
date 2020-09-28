import sys
N, a, b = map(int, sys.stdin.readline().split())

r = 0
while(True):
    if a == 0 and b == 0:
        print(-1)
        break
    elif (a%2 != 0 and a == b-1) or (b%2 != 0 and b == a-1):
        print(r+1)
        break
    else:
        r += 1
        if a%2 == 0:
            a = a//2
        else:
            a = a//2+1
        if b%2 == 0:
            b = b//2
        else:
            b = b//2+1