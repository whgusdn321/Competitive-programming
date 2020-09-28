tc = int(input())
for t in range(tc):

    s = input()
    x = int(input())
    n = len(s)
    w = [-1 for _ in range(len(s))]
    later = []
    pos = True
    for i in range(len(s)):
        if i+x >= n and i-x < 0:
            if s[i] == '1':
                pos = False
                print(-1)
                break
            else:  # w[i]  = '0' | -1
                continue
        elif i+x >= n and i-x >= 0:
            if w[i-x] == -1:
                w[i-x] = s[i]
            else:
                if w[i-x] != s[i]:  # w[i-x] is '0' | '1'
                    pos = False
                    print(-1)
                    break
                else:
                    continue
        elif i+x < n and i-x < 0:
            if w[i+x] == -1:
                w[i+x] = s[i]
            else:
                if w[i+x] != s[i]:
                    pos = False
                    print(-1)
                    break
                else:
                    continue
        else:
            if s[i] == '0':
                if w[i+x] == '1' or w[i-x] == '1':
                    pos = False
                    print(-1)
                    break
                else:
                    w[i+x] = '0'
                    w[i-x] = '0'
            else:
                later.append(i)

    # print("later : ", later)
    if pos:
        for idx in later:
            if w[idx+x] == '0' and w[idx-x] == '0':
                pos = False
                print(-1)
                break
            else:
                if w[idx+x] == -1:
                    w[idx+x] = '1'
                if w[idx-x] == -1:
                    w[idx-x] = '1'
    if pos:
        for i in range(len(w)):
            if w[i] == -1:
                w[i] = '0'
        print("".join(w))
