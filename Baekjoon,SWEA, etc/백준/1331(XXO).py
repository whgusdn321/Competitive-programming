from collections import deque
opers = []
for _ in range(36):
    opers.append(input())

visited = [[False] * 6 for _ in range(6)]
'''
이 문제를 보는순간, 일반적인 방법으로도 풀 수 있지만, bfs를 활용하여 풀 수도 있을것 같았다.
왜냐하면, 부모가 있고(현재 나이트가 있는 위치), 갈수 있는 자식들을 조사한다음에, 갈수있으면 가고, 
못가면(이미 방문했거나, 나이트가 갈수 있는 범위가 아닐때), queue에 아무것도 enque를 안해서
그 순간 queue가 비게 되서, cnt가 전체 순회를 한것이 아니기 때문에 36보다 작은값으로 끝마치게 되게 한다.
만약 전체다 돌았다면, cnt 는 36이 되게 한다.
이문제는 생각보다 시간이 많이 걸렸다.

'''


def position(char):
    row = char[0]
    colum = char[1]
    row = ord(row) - 65
    colum = int(colum) - 1
    return colum, row


def possible_next(pos):
    y = pos[0]
    x = pos[1]
    possible_next = [(y-2, x-1), (y-2, x+1), (y+2, x-1), (y+2, x+1),\
                     (y+1, x-2), (y+1, x+2), (y-1, x-2), (y-1, x+2)]
    return possible_next


cur_pos = position(opers[0]) #(0, 0)
visited[cur_pos[0]][cur_pos[1]] = True
queue = deque([0])
cnt = 1

while queue:
    cur = queue.popleft()
    cur_pos = position(opers[cur]) #'A1'
    next = cur + 1
    next_pos = position((opers[next%36])) #'B3'
    if next_pos in possible_next(cur_pos):
        if not visited[next_pos[0]][next_pos[1]]:
            visited[next_pos[0]][next_pos[1]] = True
            queue.append(next)
            cnt += 1

if cnt == 36:
    if position(opers[-1]) in possible_next(position(opers[0])):
        print('Valid')
    else:
        print('Invalid')
else:
    print("Invalid")
