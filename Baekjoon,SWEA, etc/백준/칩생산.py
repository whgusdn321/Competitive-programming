def draw:


T = int(input())
for tc in range(1, T+1):
    H, W = map(int, input().split())
    maap = []
    for _ in range(H):
        temp = [int(char) for char in input().split()]
        maap.append(temp)
    cnt = 0
    for i in range(H):
        for j in range(W):
            boool = draw(i, j, maap)
            if boool:
                cnt += 1
