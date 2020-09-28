import sys
sys.setrecursionlimit(10**6)
results1 = []
results2 = []


def preorder(parent, Tree):
    global results1

    results1.append(parent)
    if Tree[parent][0] != 0: #왼쪽자식이 있으면
        preorder(Tree[parent][0], Tree)
    if Tree[parent][1] != 0: #오른쪽 자식이 있으면
        preorder(Tree[parent][1], Tree)


def postorder(parent, Tree):
    global results2

    if Tree[parent][0] != 0: #왼쪽자식이 있으면
        postorder(Tree[parent][0], Tree)
    if Tree[parent][1] != 0: #오른쪽 자식이 있으면
        postorder(Tree[parent][1], Tree)
    results2.append(parent)


def update_children(nodeinfo):
    children = []
    max_i = 0
    same_idx = []
    for i in range(len(nodeinfo)):
        if nodeinfo[i][1] == nodeinfo[max_i][1]:
            same_idx.append(i)
        elif nodeinfo[i][1] > nodeinfo[max_i][1]:
            max_i = i
            same_idx = []

    same_idx.append(max_i)
    for idx in same_idx:
        if nodeinfo[idx][1] != -1:
            children.append((nodeinfo[idx][0], idx + 1))
            nodeinfo[idx][1] = -1
    return children


def compare(elem):
    return elem[0]


def solution(nodeinfo):
    N = len(nodeinfo)
    Tree = {}
    for i in range(1, N+1):
        Tree[i] = [0, 0]

    max_i = 0
    for i in range(len(nodeinfo)):
        if nodeinfo[i][1] > nodeinfo[max_i][1]:
            max_i = i

    parents = [(nodeinfo[max_i][0], max_i+1)]  # [(x좌표, Node)]
    First = parents[0][1]
    nodeinfo[max_i][1] = -1  # y 좌표를 -1로 만들어 준다.

    children = update_children(nodeinfo)

    while children:
        print('parents : ', parents)
        print('children : ', children)
        for child in children:
            x = child[0]
            cnt = 0
            i = 0
            while i < len(parents) and x > parents[i][0]:
                cnt += 1
                i += 1
            if cnt == 0:
                Tree[parents[0][1]][0] = child[1]
            elif cnt == len(parents):
                Tree[parents[len(parents)-1][1]][1] = child[1]
            else:
                if Tree[parents[cnt-1][1]][1] == 0:
                    Tree[parents[cnt-1][1]][1] = child[1]
                else:
                    Tree[parents[cnt][1]][0] = child[1]
        for child in children:
            parents.append(child)
        parents.sort(key=compare)
        children = update_children(nodeinfo)
    print('Tree :',Tree)

    preorder(First, Tree)
    postorder(First, Tree)

    answer = [results1, results2]
    return answer


print(solution([[11,5],[3,5],[8,6]]))