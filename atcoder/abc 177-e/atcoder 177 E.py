n = int(input())
arr = [int(a) for a in input().split()]

max_elem = max(arr)
duplicate_mode = False
sett = set([])

for elem in arr:
    if elem in sett and elem != 1:
        duplicate_mode = True
    sett.add(elem)

if not duplicate_mode:
    pos = True
    pos2 = True

    for cand in range(2, max_elem+1):
        cnt = 0
        for cand_ in range(cand, max_elem+1, cand):
            if cand_ in sett:
                cnt += 1

        if cnt == 0 or cnt == 1:
            continue
        elif cnt == len(sett):
            print("not coprime")
            pos2 = False
            break
        else:  # cnt >= 2
           pos &= False

    if pos2:
        if pos:
            print("pairwise coprime")
        else:
            print("setwise coprime")
else:
    pos = True
    for cand in range(2, max_elem+1):
        cnt = 0
        for cand_ in range(cand, max_elem+1, cand):
            if cand_ in sett:
                cnt += 1

        if cnt == len(sett):
            print("not coprime")
            pos = False
            break
    if pos:
        print("setwise coprime")

