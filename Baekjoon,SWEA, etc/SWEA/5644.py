T = int(input())
for tc in range(1, T+1):
    M, A = map(int, input().split())
    _A = [int(char) for char in input().split()]
    _B = [int(char) for char in input().split()]
    APs = []
    for _ in range(A):
        x, y, c, p = map(int, input().split())
        APs.append((y, x, c, p))
    time = len(_A)

    t = 0
    Ay, Ax = 1, 1
    By, Bx = 10, 10
    power = 0
    Alist = []
    Blist = []

    while t <= time:
        # inspect possible charges
        Alist = []
        Blist = []
        for i in range(len(APs)):
            apy, apx, apc = APs[i][0], APs[i][1], APs[i][2]
            if abs(apy - Ay) + abs(apx - Ax) <= apc:
                Alist.append(i)
            if abs(apy - By) + abs(apx - Bx) <= apc:
                Blist.append(i)
        sett = set([])
        for idx in Alist:
            sett.add(idx)
        for idx in Blist:
            sett.add(idx)
        ablist = sorted(sett, key=lambda x:APs[x][3], reverse=True)

        if len(ablist) == 0:
            pass
        elif len(ablist) == 1:
            power += APs[ablist[0]][3]
        else: # >= 2
            if len(Alist) == 0 or len(Blist) == 0:
                power += APs[ablist[0]][3]
            else:
                if ablist[0] in Alist:
                    t = 1
                    while t < len(ablist) and ablist[t] in Alist and ablist[t] not in Blist:
                        t += 1
                    power += APs[ablist[0]][3]
                    power += APs[ablist[t]][3]
                else:
                    t = 1
                    while t < len(ablist) and ablist[t] in Blist and ablist[t] not in Alist:
                        t += 1
                    power += APs[ablist[0]][3]
                    power += APs[ablist[t]][3]

        # Alist.sort(key=lambda x: APs[x][3], reverse=True)
        # Blist.sort(key=lambda x: APs[x][3], reverse=True)
        # if len(Alist) == 1 and len(Blist) == 1 and Alist[0] == Blist[0]:
        #     Apower += (APs[Alist[0]][3]//2)
        #     Bpower += (APs[Blist[0]][3]//2)
        # elif len(Alist) >= 1 and len(Blist) == 0:
        #     Apower += APs[Alist[0]][3]
        # elif len(Blist) >= 1 and len(Alist) == 0:
        #     Bpower += APs[Blist[0]][3]
        # elif len(Blist) == 0 and len(Alist) == 0:
        #     pass
        # elif Alist[0] != Blist[0]:
        #     Apower += APs[Alist[0]][3]
        #     Bpower += APs[Blist[0]][3]
        # elif len(Alist) == 1 and len(Blist) >= 2:
        #     Apower += APs[Alist[0]][3]
        #     Bpower += APs[Blist[1]][3]
        # elif len(Blist) == 1 and len(Alist) >= 2:
        #     Apower += APs[Alist[1]][3]
        #     Bpower += APs[Blist[0]][3]
        # else:
        #     if APs[Alist[1]][3] > APs[Blist[1]][3]:
        #         Apower += APs[Alist[1]][3]
        #         Bpower += APs[Blist[0]][3]
        #     else:
        #         Apower += APs[Alist[0]][3]
        #         Bpower += APs[Blist[1]][3]

        # print('t : ', t)
        # print('Ay, Ax : ', Ay, Ax)
        # print('Apower : ', Apower)
        # print('By, Bx : ', By, Bx)
        # print('Bpower : ', Bpower)
        # print()

        if t < time:
            adir = _A[t]
            bdir = _B[t]
            if adir == 0:
                pass
            elif adir == 1:
                Ay -= 1
            elif adir ==2:
                Ax += 1
            elif adir ==3: #하
                Ay += 1
            else:
                Ax -=1
            #print('bdir : ', bdir)
            if bdir == 0:
                pass
            elif bdir ==1 :
                By -= 1
            elif bdir ==2:
                Bx += 1
            elif bdir ==3: #하
                By += 1
            else:
                Bx -= 1
        t += 1
    print('#{} {}'.format(tc, power))



"""
T = int(input())
for tc in range(1, T+1):
    M, A = map(int, input().split())
    _A = [int(char) for char in input().split()]
    _B = [int(char) for char in input().split()]
    APs = []
    for _ in range(A):
        x, y, c, p = map(int, input().split())
        APs.append((y, x, c, p))
    time = len(_A)

    t = 0
    Ay, Ax = 1, 1
    By, Bx = 10, 10
    Apower = 0
    Bpower = 0
    Alist = []
    Blist = []

    while t <= time:
        # inspect possible charges
        Alist = []
        Blist = []
        for i in range(len(APs)):
            apy, apx, apc = APs[i][0], APs[i][1], APs[i][2]
            if abs(apy - Ay) + abs(apx - Ax) <= apc:
                Alist.append(i)
            if abs(apy - By) + abs(apx - Bx) <= apc:
                Blist.append(i)
        #print("Alist : ", Alist)
        #print("Blist : ", Blist)
        Alist.sort(key=lambda x: APs[x][3], reverse=True)
        Blist.sort(key=lambda x: APs[x][3], reverse=True)
        if len(Alist) == 1 and len(Blist) == 1 and Alist[0] == Blist[0]:
            Apower += (APs[Alist[0]][3]//2)
            Bpower += (APs[Blist[0]][3]//2)
        elif len(Alist) >= 1 and len(Blist) == 0:
            Apower += APs[Alist[0]][3]
        elif len(Blist) >= 1 and len(Alist) == 0:
            Bpower += APs[Blist[0]][3]
        elif len(Blist) == 0 and len(Alist) == 0:
            pass
        elif Alist[0] != Blist[0]:
            Apower += APs[Alist[0]][3]
            Bpower += APs[Blist[0]][3]
        elif len(Alist) == 1 and len(Blist) >= 2:
            Apower += APs[Alist[0]][3]
            Bpower += APs[Blist[1]][3]
        elif len(Blist) == 1 and len(Alist) >= 2:
            Apower += APs[Alist[1]][3]
            Bpower += APs[Blist[0]][3]
        else:
            if APs[Alist[1]][3] > APs[Blist[1]][3]:
                Apower += APs[Alist[1]][3]
                Bpower += APs[Blist[0]][3]
            else:
                Apower += APs[Alist[0]][3]
                Bpower += APs[Blist[1]][3]

        # print('t : ', t)
        # print('Ay, Ax : ', Ay, Ax)
        # print('Apower : ', Apower)
        # print('By, Bx : ', By, Bx)
        # print('Bpower : ', Bpower)
        # print()

        if t < time:
            adir = _A[t]
            bdir = _B[t]
            if adir == 0:
                pass
            elif adir == 1:
                Ay -= 1
            elif adir ==2:
                Ax += 1
            elif adir ==3: #하
                Ay += 1
            else:
                Ax -=1
            #print('bdir : ', bdir)
            if bdir == 0:
                pass
            elif bdir ==1 :
                By -= 1
            elif bdir ==2:
                Bx += 1
            elif bdir ==3: #하
                By += 1
            else:
                Bx -= 1
        t += 1
    print('#{} {}'.format(tc, Apower+Bpower))


"""





