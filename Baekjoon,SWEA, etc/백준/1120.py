import sys
read = lambda:sys.stdin.readline().rstrip()
a, b = read().split()
#print(a)
#print(b)

cnts = []
for i in range(0, len(b)-len(a)+1):
    cnt = 0
    for j in range(len(a)):
        if a[j] != b[i+j]:
            cnt += 1
    cnts.append(cnt)
print(min(cnts))