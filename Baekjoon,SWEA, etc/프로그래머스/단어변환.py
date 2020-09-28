from collections import defaultdict, deque
def diff(word1, word2):
    n = len(word1)
    cnt = 0
    for i in range(n):
        if word1[i] != word2[i]:
            cnt += 1
    return cnt


def solution(begin, target, words):
    N = len(words)
    visited = [False for _ in range(N)]
    queue = deque([(begin, 0)])
    while queue:
        node, cnt = queue.popleft()
        if node == target:
            return cnt
        for i in range(N):
            if not visited[i] and diff(words[i], node) == 1:
                queue.append((words[i], cnt+1))
                visited[i] = True
    return 0
print(solution('hit', 'cog' , ['hot', 'dot', 'dog', 'lot', 'log', 'cog']))