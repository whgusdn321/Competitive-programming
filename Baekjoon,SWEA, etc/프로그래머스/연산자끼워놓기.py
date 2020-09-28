import sys
read = lambda:sys.stdin.readline().rstrip()

N = int(read())
arr = [int(a) for a in read().split()]

s_m_p_d = [int(a) for a in read().split()]


def go(arr, stack, stacks):
    global visited
    if len(stack) == len(arr):
        stacks.append(stack.copy())
        return
    for i in range(0, len(arr)):
        if not visited[i]:
            visited[i] = True
            stack.append(i)
            go(arr, stack, stacks)
            stack.pop()
            visited[i] = False

# stacks = []
# visited = [False] * len(arr)
# go(arr, [], stacks)
#print('stacks : ', stacks)
smpd = []
for i, item in enumerate(s_m_p_d):
    if i == 0:
        for _ in range(item):
            smpd.append('add')
    if i == 1:
        for _ in range(item):
            smpd.append('sub')
    if i == 2:
        for _ in range(item):
            smpd.append('mul')
    if i == 3:
        for _ in range(item):
            smpd.append('div')

smpd_s = []
visited = [False] * len(smpd)
go(smpd, [], smpd_s)

results = []


for smpdper in smpd_s:
    num = arr[0]
    for i in range(0, len(smpdper)):
        if smpd[smpdper[i]] == 'add':
            num += arr[i+1]
        elif smpd[smpdper[i]] == 'mul':
            num *= arr[i+1]
        elif smpd[smpdper[i]] == 'sub':
            num -= arr[i+1]
        elif smpd[smpdper[i]] == 'div':
            if num < 0 and arr[i+1] > 0:
                num = -1*((-num)//arr[i+1])
            else:
                num //= arr[i+1]
    results.append(num)
print(max(results))
print(min(results))



