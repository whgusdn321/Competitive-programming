def makecombis(char, depth, limit, stakk):
    global combis
    if depth == limit:
        return
    else:
        if char == 'o':
            stakk.append(depth)
        if depth == limit - 1:
            combis.append(stakk)
            return
        if char == 'o':
            makecombis('x', depth+1, limit, stakk.copy())
        else:
            makecombis('x', depth+1, limit, stakk.copy())
            makecombis('o', depth+1, limit, stakk.copy())


N = int(input())
string = input()

nums = []
opers = []

for i in range(N):
    if i % 2 == 0:
        nums.append(int(string[i]))
    else:
        opers.append(string[i])

combis = []
makecombis('x', 0, len(opers), [])
makecombis('o', 0, len(opers), [])

# print('combis : ', combis)
# print('nums : ',nums)
# print('opers : ',opers)
results = []
for combi in combis:
    next_nums = []
    next_opers = []

    i = 0
    while i < len(opers):
        if i not in combi:
            next_nums.append(nums[i])
            next_opers.append(opers[i])
            i += 1
            if i == len(opers):
                next_nums.append(nums[i])
        else:
            a = nums[i]
            b = nums[i+1]
            oper = opers[i]
            if oper == '*':
                c = a * b
            elif oper == '+':
                c = a + b
            else: #oper == '-':
                c = a - b
            next_nums.append(c)
            if i + 1 < len(opers):
                next_opers.append(opers[i+1])
            i += 2
            if i == len(nums)-1:
                next_nums.append(nums[i])
    # print('nums : ', nums)
    # print('opers: ', opers)
    # print('combi : ',combi)
    # print('next_nums : ',next_nums)
    # print('next_opers : ', next_opers)
    while next_opers:
        a = next_nums.pop(0)
        b = next_nums.pop(0)
        oper = next_opers.pop(0)
        if oper == '*':
            c = a * b
        elif oper == '+':
            c = a + b
        else:  # oper == '-':
            c = a - b
        next_nums.insert(0, c)
    #print('nextnums: ',next_nums)
    #print()
    results.append(next_nums[0])

if N == 1:
    print(nums[0])
else:
    print(max(results))

