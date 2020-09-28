N = None


def erase(block, board):
    cords = block[1]
    for y, x in cords:
        board[y][x] = 0


def canTerminated(block, board):
    id = block[0]
    cords = block[1]
    if id == 1:
        sy, sx = cords[2]
        boool = True
        for i in range(0, sy):
            if board[i][sx] != 0:
                boool = False

        sy, sx = cords[3]
        for i in range(0, sy):
            if board[i][sx] != 0:
                boool = False
        return boool

    elif id == 2:
        sy, sx = cords[3]
        boool = True
        for i in range(0, sy):
            if board[i][sx] != 0:
                boool = False
        return boool

    elif id == 3:
        sy, sx = cords[3]
        boool = True
        for i in range(0, sy):
            if board[i][sx] != 0:
                boool = False
        return boool
    elif id == 4:
        sy, sx = cords[2]
        boool = True
        for i in range(0, sy):
            if board[i][sx] != 0:
                boool = False

        sy, sx = cords[3]
        for i in range(0, sy):
            if board[i][sx] != 0:
                boool = False
        return boool
    else : ## id == 5
        sy, sx = cords[1]
        boool = True
        for i in range(0, sy):
            if board[i][sx] != 0:
                boool = False

        sy, sx = cords[3]
        for i in range(0, sy):
            if board[i][sx] != 0:
                boool = False
        return boool


def find_block(board, i, j, color):
    one = [(i, j), (i+1, j), (i+1, j+1), (i+1, j+2)]
    two = [(i, j), (i+1, j), (i+2, j), (i+2, j-1)]
    three = [(i, j),(i+1, j), (i+2, j), (i+2, j+1)]
    four = [(i, j),(i+1, j), (i+1, j-1), (i+1, j-2)]
    five = [(i, j),(i+1, j-1), (i+1, j), (i+1, j+1)]

    boool = True
    for y, x in one:
        if not (0<=y<N and 0<=x<N) or board[y][x] != color:
            boool = False
    if boool :
        return (1, one)

    boool = True
    for y, x in two:
        if not (0<=y<N and 0<=x<N) or board[y][x] != color:
            boool = False
    if boool:
        return (2, two)

    boool = True
    for y, x in three:
        if not (0<=y<N and 0<=x<N) or board[y][x] != color:
            boool = False
    if boool:
        return (3, three)

    boool = True
    for y, x in four:
        if not (0<=y<N and 0<=x<N) or board[y][x] != color:
            boool = False
    if boool:
        return (4, four)

    boool = True
    for y, x in five:
        if not (0<=y<N and 0<=x<N) or board[y][x] != color:
            boool = False
    if boool:
        return (5, five)

    return False



def solution(board):
    global N
    """

    :param board: [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,4,0,0,0],[0,0,0,0,0,4,4,0,0,0],[0,0,0,0,3,0,4,0,0,0],[0,0,0,2,3,0,0,0,5,5],[1,2,2,2,3,3,0,0,0,5],[1,1,1,0,0,0,0,0,0,5]]
    :return:
    """
    N = len(board)
    blocks = []
    for i in range(N):
        for j in range(N):
            if board[i][j] != 0:
                block = find_block(board, i, j, board[i][j])
                if block:
                    blocks.append(block)
    print('blocks : ',blocks)
    cnt = 0
    while True:
        garbages = []
        for block in blocks:
            if canTerminated(block, board):
                garbages.append(block)
        if garbages:
            for block in garbages:
                erase(block, board)
                blocks.remove(block)
                cnt += 1
        else:
            break

    return cnt

print(solution([[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,4,0,0,0],[0,0,0,0,0,4,4,0,0,0],[0,0,0,0,3,0,4,0,0,0],[0,0,0,2,3,0,0,0,5,5],[1,2,2,2,3,3,0,0,0,5],[1,1,1,0,0,0,0,0,0,5]]))