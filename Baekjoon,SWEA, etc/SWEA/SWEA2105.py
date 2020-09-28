"""
이 문제는 상당히 복잡하다. 약 3시간에 걸쳐서 푼 문제로, 한번 다시 풀어볼 필요성이 굉장히 크다.
생각해야 할 부분이 많아서 문제 자체가 복잡하다..
이 문제를 다 풀고, 문제를 풀기위해서 생각해야 하는 부분들을 다시한번 정리해보았다.

    1.가는 방향은 어딘데? -> 원래 기초적인 DFS/BFS문제들은 대부분 상,하,좌,우 만 나와서 거기에 항상 익숙해져 있다. 하지만 이 문제는
                            기본적으로 가는방향이 다르다. 따라서 우선은 가는방향(마름모꼴을 이루면서, 나중에 합쳐지게 dfs가 돌게) 잘 구현을 해야 한다는 것을 알 수 있다.
    1-1)그리고 가면서 문을 열어둔다.(return되고 다음줄에 또 함수 호출)
    2.go(specific_i, specific_j, dy, dx, visited, sofar)는 그래서 불려서 뭘 하는데?
        -> 이것을 그림(maap)과 연동시켜서 약간 이미지를 그리면서 도데체 이 함수가 call되었을때 무엇을 하는지, 즉 특정한 순간에 무엇을 하는지! 약간 느낌을 가지자.
        -> 이 함수는 다음에 갈 곳이 갈 수 있다면(범위안에 들고, 중복 방문이 아닌경우), visited에 추가시켜 준다.

    3. 어떤경우에 종료조건이 되는가? 그리고 종료되면서 visited, sofar는 각 함수에서 pop하는데, 함수가 return이 되면서 visited, sofar의 배열들이 어떻게 변하는지 잘 알아보자.
        ->개인적으로 이부분이 가장 힘들었다. 일반적으로 문을 열어두어 모든 가능한 경로를 방문하는 dfs방식은, 가기전에 visited에 추가하고 return 조건에서 pop을 해서 하는
          사전지식이 있었다. 그래서 약간 감과 이러한 지식을 이용하여 코드를 짜서, 어찌어찌 맞았다. 하지만 이부분에 대하여 약간 보강을 해야할 것 같다.


"""
def go(i, j, dy, dx, visited, sofar):
    # visited
    global N, maap, results
    if (dy, dx) == (1, 1):
        next1 = (i+1, j+1)
        next2 = (i+1, j-1)
        if 0<=next1[0]<N and 0<=next1[1]<N and maap[next1[0]][next1[1]] not in visited:
            visited.append(maap[next1[0]][next1[1]])
            sofar.append('SE')
            go(next1[0], next1[1], 1,1, visited, sofar)
            sofar.pop()
            visited.pop()
        if visited and 0 <= next2[0] < N and 0 <= next2[1] <N and maap[next2[0]][next2[1]] not in visited:
            visited.append(maap[next2[0]][next2[1]])
            sofar.append('SW')
            go(next2[0], next2[1], 1, -1, visited, sofar)
            sofar.pop()
            visited.pop()
    elif (dy, dx) == (1, -1):
        next1 = (i+1, j-1)
        next2 = (i-1, j-1)
        if 0<=next1[0]<N and 0<=next1[1]<N and maap[next1[0]][next1[1]] not in visited:
            visited.append(maap[next1[0]][next1[1]])
            sofar.append('SW')
            go(next1[0], next1[1], 1, -1, visited, sofar)
            sofar.pop()
            visited.pop()
        if 0<=next2[0]<N and 0<=next2[1] <N and maap[next2[0]][next2[1]] not in visited:
            go(i, j, -1, -1, visited, sofar)

    elif (dy, dx) == (-1, -1):
        boool = True
        next = [i, j]
        _N = len(visited)
        for i in range(len(sofar)):
            if sofar[i] == 'SE':
                next = [next[0]-1, next[1]-1]
                if 0<=next[0]<N and 0<=next[1]<N and maap[next[0]][next[1]] not in visited:
                    visited.append(maap[next[0]][next[1]])
                else:
                    boool = False
                    break
            else:
                next = [next[0]-1, next[1]+1]
                if 0<=next[0]<N and 0<=next[1]<N and maap[next[0]][next[1]] not in visited:
                    visited.append(maap[next[0]][next[1]])
                else:
                    boool = False
                    break
        if boool:
            results.append(len(visited))
        while len(visited) != _N:
            visited.pop()
        return




test_cases = int(input())
for test_case in range(1, test_cases + 1):
    N = int(input())
    maap = []
    for _ in range(N):
        temp = [int(a) for a in input().split()]
        maap.append(temp)
    results = []
    for y in range(N):
        for x in range(N):
            go(y, x, 1, 1, [], [])
    if results:
        print('#{} {}'.format(test_case, max(results)))
    else:
        print('#{} {}'.format(test_case, -1))
