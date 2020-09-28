#스도쿠
test_cases = int(input())
for testcase in range(1, test_cases+1):
    maap = []
    for _ in range(9):
        temp = [int(a) for a in input().split()]
        maap.append(temp)

    boool = True
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            nums = 0
            for y in range(3):
                for x in range(3):
                    nums += maap[i+y][j+x]

            if nums != 45:
                boool = False
                break
        if not boool:
            break

    if boool:
        for i in range(0, 9):
            nums = 0
            for j in range(0, 9):
                nums += maap[i][j]

            if nums != 45:
                boool = False
                break
            if not boool:
                break

    if boool:
        for i in range(0, 9):
            nums = 0
            for j in range(0, 9):
                nums += maap[j][i]
            if nums != 45:
                boool = False
                break
            if not boool:
                break
    if boool:
        print('#{} {}'.format(testcase, 1))
    else:
        print('#{} {}'.format(testcase, 0))

