def go(mode, num, before_num, cnt):
    global cnts, allowed_nums, wanted
    #print('num: ', int(num), 'before_num :', before_num)
    if int(before_num) == wanted:
        cnts.append(cnt)
        return
    if int(num) * int(before_num) > wanted:
        return
    if int(num) > wanted :
        return

    if mode == 'pedding':
        for allowed in allowed_nums:
            if not(num == '0' and allowed == '0'):
                num += allowed
                go('pedding', num, before_num, cnt + 1)
                num = num[:-1]
            if not num == '0':
                go('mul', num, before_num, cnt + 1)
    else: # mode == 'mul'
        if int(num) != 1:
            num = int(num) * int(before_num)
            go('pedding', '0', str(num), cnt + 1)


TC = int(input())
for tc in range(1, TC+1):
    temp = [int(a) for a in input().split()]
    allowed_nums =[]
    for i in range(10):
        if temp[i]:
            allowed_nums.append(str(i))
    wanted = int(input())
    cnts = []
    go('pedding', '0', 1, 0)
    if cnts:
        print('#{} {}'.format(tc, min(cnts)))
    else:
        print('#{} {}'.format(tc, -1))