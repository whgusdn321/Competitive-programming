from collections import deque
n = int(input())
arr = deque([i + 1 for i in range(n)])

# i = 0
# for _ in range(n-2):
#     arr[i] = -1
#     temp = arr[i+1]
#     for j in range(i+1, len(arr)-1):
#         arr[j] = arr[j+1]
#     arr[len(arr)-1] = temp
#     i += 1
# print(arr[-1])

while len(arr) > 1:
    arr.popleft()
    k = arr.popleft()
    arr.append(k)
print(arr[-1])