N, M, L = map(int, input().split())
arr = [0]*N
cur_idx = 0
while arr[cur_idx] != M:
    arr[cur_idx] += 1
    if arr[cur_idx] == M:
        break
    else:
        if arr[cur_idx] %2 == 1:
            cur_idx = (cur_idx + L)%N
        else:
            cur_idx = (cur_idx - L)%N
print(sum(arr)-1)