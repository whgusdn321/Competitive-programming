from collections import deque

primes = []
prime = [True] * 10000
prime[0] = False
prime[1] = False

for i in range(2, 10000): #애라토네스의 채 구현
    if prime[i]:
        primes.append(i)
        for j in range(2, 10000):
            if i*j > 9999:
                break
            prime[i*j] = False


def isprime(a):
    global prime
    char =''
    for item in a:
        char += str(item)
    num = int(char)
    return prime[num]


def num(a):
    char = ''
    for item in a:
        char += str(item)
    num = int(char)
    return num


def howmanyprime(a, b): #모든 공간을 다 조사하기 위하여 bfs/dfs를 사용해야한다. 왜 bfs를 사용하였는가? bfs의 queue안의 원소들에 거리를 저장하는 것을 나는 많이 해와서..
    global prime, visited
    queue = deque([[a, 0]]) #[[1,0,3,3], 0]
    visited[num(a)] = True
    while queue:
        aa = queue.popleft()
        if aa[0] == b:
            return(aa[1])
        for k in range(4):
            for i in range(10): #일딴, 불가능한 경우도 포함한 더 큰 경우를 생각하고
                aaa = aa[0].copy()
                aaa[k] = i
                if not visited[num(aaa)] and num(aaa) >= 1000 and isprime(aaa): # 못가는곳을 뺀다(num > 1000, isprime(aaa) 그리고! 항상 bfs의 핵심, 간곳은 또 가면 무한루프가 된다(visited[] 해줘야함)
                    visited[num(aaa)] = True
                    queue.append([aaa, aa[1]+1])
    return -1

test_cases = int(input())
for test_case in range(test_cases):
    a, b = input().split()
    a = [int(k) for k in a]
    b = [int(k) for k in b]
    visited = [False] * 10000
    result = howmanyprime(a, b)
    if result != -1:
        print(result)
    else:
        print('Impossible')