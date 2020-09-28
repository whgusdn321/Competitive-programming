n = int(input())
arr = [int(a) for a in input().split()]

summ = sum(arr)
ans = 0
for i in range(n-1):
    a = arr[i]
    summ -= arr[i]
    b = summ
    ans += (a*b)%(int(1e9+7))

print(ans%(int(1e9+7)))