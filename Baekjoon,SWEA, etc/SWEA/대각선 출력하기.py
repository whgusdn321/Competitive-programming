N = 5
arr = [['+'] * 5 for _ in range(5)]
dx, dy = 1, 1
sy, sx = 0, 0
for i in range(5):
    arr[sy][sx] = '#'
    sy += dy
    sx += dx

for i in range(5):
    for j in range(5):
        print(arr[i][j], end='')
    print()
