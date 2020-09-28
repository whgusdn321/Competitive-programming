N = int(input())
a = [int(char) for char in input().split()]
B, C = map(int, input().split())
ans = 0
for n in a:
    if n <= B:
        ans += 1
        continue
    else:
        n -= B
        ans += 1
        if n % C == 0:
            ans += (n // C)
        else:
            ans += (n // C + 1)
print(ans)