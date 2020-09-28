import sys
read = lambda :sys.stdin.readline().rstrip()

L = int(read())
A = int(read())
B = int(read())
C = int(read())
D = int(read())

if A%C == 0:
    a = A//C
else:
    a = A//C+1

if B%D == 0:
    b = B//D
else:
    b = B//D+1

if a>=b:
    print(L-a)
else:
    print(L-b)
