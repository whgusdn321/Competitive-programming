from collections import deque
n = int(input())
arr = deque([i + 1 for i in range(n)])

results = []
while len(arr) > 1:
    b = arr.popleft()
    results.append(b)
    k = arr.popleft()
    arr.append(k)

for item in results :
    print(item, end=' ')

print(arr[-1])