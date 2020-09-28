hex = {'0': '0000', '1': '0001', '2': '0010', '3': '0011',\
       '4': '0100', '5': '0101', '6': '0110', '7': '0111',\
       '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',\
       'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

zeros = ['0'*3*i + '1'*2*i + '0'*1*i + '1'*1*i for i in range(0, 40)]
ones = ['0'*2*i + '1'*2*i + '0'*2*i + '1'*1*i for i in range(0, 40)]
twos = ['0'*2*i + '1'*1*i + '0'*2*i +'1'*2*i for i in range(0, 40)]
threes = ['0'*1*i + '1'*4*i + '0'*1*i +'1'*1*i for i in range(0, 40)]
fours = ['0'*1*i + '1'*1*i + '0'*3*i +'1'*2*i for i in range(0, 40)]
fives = ['0'*1*i + '1'*2*i + '0'*3*i +'1'*1*i for i in range(0, 40)]
sixs = ['0'*1*i + '1'*1*i + '0'*1*i +'1'*4*i for i in range(0, 40)]
sevens = ['0'*1*i + '1'*3*i + '0'*1*i +'1'*2*i for i in range(0, 40)]
eights = ['0'*1*i + '1'*2*i + '0'*1*i +'1'*3*i for i in range(0, 40)]
nines = ['0'*3*i + '1'*1*i + '0'*1*i +'1'*2*i for i in range(0, 40)]


def _inspect(_arr, thick):
    # if string matches perfectly, return codes(8 digits)
    # else, return False
    result = ''
    k = 7 * thick
    for i in range(0, len(_arr), k):
        if _arr[i:i+k] == zeros[thick]:
            result += '0'
        elif _arr[i:i+k] == ones[thick]:
            result += '1'
        elif _arr[i:i + k] == twos[thick]:
            result += '2'
        elif _arr[i:i + k] == threes[thick]:
            result += '3'
        elif _arr[i:i + k] == fours[thick]:
            result += '4'
        elif _arr[i:i + k] == fives[thick]:
            result += '5'
        elif _arr[i:i + k] == sixs[thick]:
            result += '6'
        elif _arr[i:i + k] == sevens[thick]:
            result += '7'
        elif _arr[i:i + k] == eights[thick]:
            result += '8'
        elif _arr[i:i + k] == nines[thick]:
            result += '9'
        else:
            return False
    return result


def inspect(ar, thick):
    arr = '0' * 3 * thick
    for item in ar:
        arr += hex[item]
    arr += '0' * 3 * thick
    for i in range(0, 3*thick + 4):
        result = _inspect(arr[i:i+56*thick], thick)
        if result == False:
            continue
        else:
            if ( (int(result[0]) + int(result[2]) + int(result[4]) + int(result[6]))*3 +
            int(result[1]) + int(result[3]) + int(result[5]) + int(result[7]) ) % 10 == 0:
                summ = sum([int(result[i]) for i in range(8)])

                return summ
    return 0


T = int(input())
for tc in range(1, T+1):
    H, W = map(int, input().split())
    maap = []
    for _ in range(H):
        maap.append(input())
    boool = False
    y = 0
    sums = 0
    while y < H:
        x = 0
        while x < W:
            if not boool and maap[y][x] != '0':
                #x
                for length in range(14, 500, 14):
                    thick = length // 14
                    if x + length - 1 < W and maap[y][x+length-1] != '0':
                        if y > 0 and maap[y][x:x+length] != maap[y-1][x:x+length]:
                            arr = maap[y][x:x+length]
                            sums += inspect(arr, thick)
                    if x + length < W and maap[y][x+length] != '0':
                        if y > 0 and maap[y][x:x+length+1] != maap[y-1][x:x+length+1]:
                            arr = maap[y][x:x+length+1]
                            sums += inspect(arr, thick)
            x += 1



                # while k < W and maap[y][k] != '0':
                #     k += 1
                #     length += 1
                # i = 0
                # while (length - i) % 14 != 0 and (length + i) % 14 != 0:
                #     i += 1
                # if (length - i) % 14 == 0:
                #     thick = (length - i) // 14
                # else:
                #     thick = (length + i) // 14

                # if y > 0 and maap[y][x:x+k] != maap[y-1][x:x+k]:
                #     arr = maap[y][x:x+k]
                #     sums += inspect(arr, thick)
                # x = k
            # else:
            #     x += 1
        y += 1
    if sums == 0:
        print('#{} {}'.format(tc, 0))
    else:
        print('#{} {}'.format(tc, sums))





