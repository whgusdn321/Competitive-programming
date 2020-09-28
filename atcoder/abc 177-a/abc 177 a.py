d = 0
t = 0
s = 0

d, t, s = map(int, input().split())
if s*t >= d:
    print("Yes")
else:
    print("No")