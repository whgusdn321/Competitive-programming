T = int(input())

for tc in range(1, T+1):
    arrN, operN, inputN = map(int, input().split())
    opers = [char for char in input()]
    _input = input()

    graph = {}
    stakk1 = []
    arr = [0]*arrN
    for i in range(operN):
        if opers[i] == '[':
            stakk1.append(i)
        elif opers[i] == ']':
            a = stakk1.pop()
            b = i
            graph[a] = b
            graph[b] = a

    ap = 0
    op = 0
    rp = 0
    graph2 = {}
    for item in graph.keys():
        graph2[item] = 0

    for _ in range(50000000):
        if op == len(opers):
            break
        oper = opers[op]
        if oper == '-':
            arr[ap] = (arr[ap]-1)%256
        elif oper == '+':
            arr[ap] = (arr[ap]+1)%256
        elif oper == '<':
            ap = (ap - 1) % arrN
        elif oper == '>':
            ap = (ap + 1) % arrN
        elif oper == '[':
            graph2[op] = arr[ap]
            if arr[ap] == 0:
                op = graph[op]
                continue
        elif oper == ']':
            graph2[op] = arr[ap]
            if arr[ap] != 0:
                op = graph[op]
                continue
        elif oper == '.':
            pass
        else:  # oper == ','
            if rp != inputN:
                arr[ap] = ord(_input[rp])%256
                rp += 1
            else:
                arr[ap] = 255
        op += 1
    if op == len(opers):
        print('Terminates')
    else:
        boool = True
        for a, b in graph.items():
            if a < b:
                if graph2[a] == 0 and graph2[b] != 0:
                    print('Loops {} {}'.format(a, b))
                    boool &= False
                    break
                elif graph[a] != 0 and graph2[b] != 0:
                    print('Loops {} {}'.format(a, b))
                    boool &= False
                    break
                else:
                    boool &= True
        if boool:
            print('Terminates')






