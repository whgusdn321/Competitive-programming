codes = ["0001101", "0011001", "0010011", "0111101", "0100011", "0110001", "0101111", "0111011", "0110111", "0001011"]
testcases = int(input())


def numcode(code):
    for i in range(len(codes)):
        if code == codes[i]:
            return i
    return -1


for testcase in range(1, testcases+1):
    H, W = map(int, input().split())
    maap = []
    for i in range(H):
        maap.append(input())

    arr = None
    starti = None
    for i in range(H):
        boool = False
        for j in range(W):
            if maap[i][j] == '1':
                starti = j
                arr = maap[i]
                boool = True
                break
        if boool:
            break

    boool = True
    if starti-3 >= 0 and (starti-3) + 7 * 8 - 1 < W:
        s = starti-3
        for i in range(8):
            codee = arr[s + 7 * i: s + 7 * (i + 1)]
            num = numcode(codee)
            if num == -1:
                boool = False
                break
        if boool:
            starti = s

    if not boool and starti-2>=0 and (starti-2) + 7 * 8 - 1 < W:
        boool = True
        s = starti - 2
        for i in range(8):
            codee = arr[s + 7 * i: s + 7 * (i + 1)]
            num = numcode(codee)
            if num == -1:
                boool = False
                break
        if boool:
            starti = s

    if not boool and starti-1 >=0 and (starti-1) + 7 * 8 - 1 < W:
        boool = True
        s = starti - 1
        for i in range(8):
            codee = arr[s + 7 * i: s + 7 * (i + 1)]
            num = numcode(codee)
            if num == -1:
                boool = False
                break
        if boool:
            starti = s

    nums = []
    for i in range(8):
        codee = arr[starti + 7*i: starti + 7*(i+1)]
        num = numcode(codee)
        nums.append(num)
    if ((nums[0]+nums[2]+nums[4]+nums[6])*3 + (nums[1]+nums[3]+nums[5] + nums[7])) %10 == 0:
        print('#{} {}'.format(testcase, sum(nums)))
    else:
        print('#{} {}'.format(testcase, 0))

