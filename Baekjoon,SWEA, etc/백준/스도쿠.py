maap = []
for _ in range(9):
    temp = [int(a) for a in input().split()]
    maap.append(temp)

flag = True
while flag:
    flag = False
    for i in range(9):
        for j in range(9):
            if maap[i][j] == 0:
                flag = True
                l, k = i//3, j//3
                stack1 = []
                for m in range(l*3, l*3+3):
                    for n in range(k*3, k*3+3):
                        if maap[m][n] != 0:
                            stack1.append(maap[m][n])
                if len(stack1) == 8:
                    maap[i][j] = 45 - sum(stack1)
                    continue
                else:
                    stack2 = []
                    for m in range(0, 9):
                        if maap[i][m] != 0:
                            stack2.append(maap[i][m])
                    if len(stack2) == 8:
                        maap[i][j] = 45 - sum(stack2)
                        continue
                    else:
                        stack3 = []
                        for n in range(0, 9):
                            if maap[n][j] != 0:
                                stack3.append(maap[n][j])
                        if len(stack3) == 8:
                            maap[i][j] = 45 - sum(stack3)

#print('new maap: ')
for i in range(9):
    for j in range(9):
        print(maap[i][j], end=' ')
    print()

