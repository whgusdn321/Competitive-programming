cube = ['r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r',
        'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o',
        'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b',
        'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g',
        'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w',
        'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y',]


def init_cube():
    global cube
    cube = \
        ['r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r',
         'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o',
         'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b',
         'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g',
         'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w',
         'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', ]


def rotate(side, dirc):
    if side == 'U':
        arr1 = [36, 37, 38, 41, 44, 43, 42, 39]
        arr2 = [9, 10, 11, 20, 19, 18, 2, 1, 0, 27, 28, 29]
        temp1 = [cube[i] for i in arr1]
        temp2 = [cube[i] for i in arr2]
        if dirc == '+':
            for i in range(8):
                cube[arr1[i]] = temp1[(i - 2) % 8]
            for i in range(12):
                cube[arr2[i]] = temp2[(i - 3) % 12]
        else:
            for i in range(8):
                cube[arr1[i]] = temp1[(i + 2) % 8]
            for i in range(12):
                cube[arr2[i]] = temp2[(i + 3) % 12]

    elif side == 'D':
        arr1 = [45, 46, 47, 50, 53, 52, 51, 48]
        arr2 = [15, 16, 17, 26, 25, 24, 8, 7, 6, 33, 34, 35]
        temp1 = [cube[i] for i in arr1]
        temp2 = [cube[i] for i in arr2]

        if dirc == '-':
            for i in range(8):
                cube[arr1[i]] = temp1[(i - 2) % 8]
            for i in range(12):
                cube[arr2[i]] = temp2[(i - 3) % 12]
        else:
            for i in range(8):
                cube[arr1[i]] = temp1[(i + 2) % 8]
            for i in range(12):
                cube[arr2[i]] = temp2[(i + 3) % 12]
    elif side == 'F':
        arr1 = [0, 1, 2, 5, 8, 7, 6, 3]
        arr2 = [42, 43, 44, 18, 21, 24, 53, 52, 51, 33, 30, 27]
        temp1 = [cube[i] for i in arr1]
        temp2 = [cube[i] for i in arr2]

        if dirc == '+':
            for i in range(8):
                cube[arr1[i]] = temp1[(i - 2) % 8]
            for i in range(12):
                cube[arr2[i]] = temp2[(i - 3) % 12]
        else:
            for i in range(8):
                cube[arr1[i]] = temp1[(i + 2) % 8]
            for i in range(12):
                cube[arr2[i]] = temp2[(i + 3) % 12]
    elif side == 'B':
        arr1 = [9, 10, 11, 14, 17, 16, 15, 12]
        arr2 = [36, 37, 38, 20, 23, 26, 47, 46, 45, 35, 32, 29]
        temp1 = [cube[i] for i in arr1]
        temp2 = [cube[i] for i in arr2]

        if dirc == '-':
            for i in range(8):
                cube[arr1[i]] = temp1[(i - 2) % 8]
            for i in range(12):
                cube[arr2[i]] = temp2[(i - 3) % 12]
        else:
            for i in range(8):
                cube[arr1[i]] = temp1[(i + 2) % 8]
            for i in range(12):
                cube[arr2[i]] = temp2[(i + 3) % 12]
    elif side == 'L':
        arr1 = [27, 28, 29, 32, 35, 34, 33, 30]
        arr2 = [42, 39, 36, 9, 12, 15, 45, 48, 51, 6, 3, 0]
        temp1 = [cube[i] for i in arr1]
        temp2 = [cube[i] for i in arr2]

        if dirc == '-':
            for i in range(8):
                cube[arr1[i]] = temp1[(i - 2) % 8]
            for i in range(12):
                cube[arr2[i]] = temp2[(i - 3) % 12]
        else:
            for i in range(8):
                cube[arr1[i]] = temp1[(i + 2) % 8]
            for i in range(12):
                cube[arr2[i]] = temp2[(i + 3) % 12]

    else:  #side == 'R'
        arr1 = [18, 19, 20, 23, 26, 25, 24, 21]
        arr2 = [44, 41, 38, 11, 14, 17, 47, 50, 53, 8, 5 ,2]
        temp1 = [cube[i] for i in arr1]
        temp2 = [cube[i] for i in arr2]
        if dirc == '+':
            for i in range(8):
                cube[arr1[i]] = temp1[(i - 2) % 8]
            for i in range(12):
                cube[arr2[i]] = temp2[(i - 3) % 12]
        else:
            for i in range(8):
                cube[arr1[i]] = temp1[(i + 2) % 8]
            for i in range(12):
                cube[arr2[i]] = temp2[(i + 3) % 12]

tcs = int(input())
for tc in range(1, tcs+1):
    init_cube()
    n = int(input())
    opers = [char for char in input().split()]
    #print('opers : ', opers)
    for oper in opers:
        side = oper[0]
        dirc = oper[1]
        rotate(side, dirc)
    r1 = [36, 37, 38]
    r2 = [39, 40, 41]
    r3 = [42, 43, 44]
    for i in r1:
        print(cube[i], end='')
    print()
    for i in r2:
        print(cube[i], end='')
    print()
    for i in r3:
        print(cube[i], end='')
    print()
