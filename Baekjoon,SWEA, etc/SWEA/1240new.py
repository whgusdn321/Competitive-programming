codes = {'0001101':'0', '0011001':'1', '0010011':'2', '0111101':'3',
         '0100011': '4', '0110001':'5', '0101111':'6', '0111011':'7',
         '0110111':'8', '0001011':'9'}


def valid(code):
    if code in codes.keys():
        return True
    else:
        return False


def _inspect(start, arr):
    global W, result
    boool = True
    num = ''
    s = start
    for i in range(s, s+56, 7):
        if i+7 > W:
            boool = False
            break
        code = arr[i:i+7]
        if valid(code):
            num += codes[code]
        else:
            boool = False
            break
    if boool:
        _1, _2, _3, _4, _5, _6, _7, _8 = [int(char) for char in num]
        if ((_1+_3+_5+_7)*3 + (_2+_4+_6) + _8) % 10 == 0:
            result = (_1+_2+_3+_4+_5+_6+_7+_8)
            return True
        else:
            return False
    else:
        return False


def inspect(maap):
    global W
    for a in maap:
        j = 0
        for i in range(0, W):
            if a[i] != '0':
                j = i
                break

        if j-1>=0:
            boool = _inspect(j-1, a)
            if boool:
                break
        if j-2>=0:
            boool = _inspect(j-2, a)
            if boool:
                break
        if j-3>=0:
            boool = _inspect(j-3, a)
            if boool:
                break


T = int(input())
for tc in range(1, T+1):
    H, W = map(int, input().split())
    maap = []
    zeros = '0'*W
    result = 0

    for i in range(H):
        a = input()
        if a!= zeros:
            if len(maap) != 0 and a != maap[-1]:
                maap.append(a)
            elif len(maap) == 0:
                maap.append(a)
            else:
                pass
    inspect(maap)
    print('#{} {}'.format(tc, result))