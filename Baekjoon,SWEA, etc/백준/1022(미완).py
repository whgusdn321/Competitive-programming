r1, c1, r2, c2 = map(int, input().split())
#valid range r1 <= y <= r2, c1 <= x <= c2


def valid_range(y, x):
    if r1 <= y <= r2 and  c1 <= x <= c2:
        return True
    else:
        return False


k = max(abs(r1), abs(r2), abs(c1), abs(c2))
H = r2 - (r1-1)
W = c2 - (c1-1)
#print('H , W :', H, W)
maap = [[0] * W for _ in range(H)]
# for _ in range(H):
#     print(maap[_])

cur_y = 0
cur_x = 0
value = 1
if valid_range(cur_y, cur_x):
    #print('cur_y-r1 :',cur_y-r1)
    #print('cur_x-c1 :',cur_x-c1)
    maap[cur_y-r1][cur_x-c1] = value
value += 1

for i in range(k):
    cur_y = cur_y
    cur_x = cur_x + 1
    if valid_range(cur_y, cur_x):
        maap[cur_y - r1][cur_x - c1] = value
    value += 1

    l = 3 + 2*i
    for _ in range(l-2):
        cur_y -= 1
        if valid_range(cur_y, cur_x):
            maap[cur_y - r1][cur_x - c1] = value
        value += 1
    for _ in range(l-1):
        cur_x -= 1
        if valid_range(cur_y, cur_x):
            maap[cur_y - r1][cur_x - c1] = value
        value += 1
    for _ in range(l-1):
        cur_y += 1
        if valid_range(cur_y, cur_x):
            maap[cur_y - r1][cur_x - c1] = value
        value += 1
    for _ in range(l-1):
        cur_x += 1
        if valid_range(cur_y, cur_x):
            maap[cur_y - r1][cur_x - c1] = value
        value += 1

# for _ in range(H):
#     print(maap[_])

maxi, maxj = 0, 0
for i in range(H):
    for j in range(W):
        if maap[i][j] > maap[maxi][maxj]:
            maxi = i
            maxj = j

maxnum = maap[maxi][maxj]
#print('maxnum : ',maxnum)
k = 0
while maxnum // 10 != 0:
    maxnum //= 10
    k += 1
for i in range(H):
    for j in range(W):
        num = maap[i][j]
        kk = 0
        while num // 10 != 0:
            num //= 10
            kk += 1
        print(' ' * (k - kk), end='')
        print(maap[i][j], end=' ')
    print()