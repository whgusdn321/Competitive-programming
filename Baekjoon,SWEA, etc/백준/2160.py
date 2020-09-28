N = int(input())
maaps = []
for n in range(N):
    map2D = []
    for _ in range(5):
        map2D.append(input())
    maaps.append(map2D)

combis = []


def combi(i, stack, nn):
    global combis, N
    if len(stack) == nn:
        combis.append(stack.copy())
    else:
        for j in range(i+1, N):
            stack.append(j)
            combi(j, stack, nn)
            stack.pop()


combi(-1, [], 2)
cnts = []
#print('combis: ',combis)
for combi in combis:
    cnt = 0
    map1 = maaps[combi[0]] #[5, 7]
    map2 = maaps[combi[1]] #[5, 7]
    for i in range(5):
        for j in range(7):
            if map1[i][j] != map2[i][j]:
                cnt += 1
    cnts.append((combi[0], combi[1], cnt))

min_idx = 0
for i in range(len(cnts)):
    if cnts[i][2] < cnts[min_idx][2]:
        min_idx = i

print(cnts[min_idx][0]+1, cnts[min_idx][1]+1)
