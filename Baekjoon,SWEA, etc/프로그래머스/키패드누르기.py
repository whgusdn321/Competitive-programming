def solution(numbers, hand):
    yx = {'1':(0,0), '2':(0,1), '3':(0,2),
          '4':(1,0), '5':(1,1), '6':(1,2),
          '7': (2, 0), '8': (2, 1), '9': (2, 2),
          '*': (3, 0), '0': (3, 1), '#': (3, 2),
          }
    l = '*'
    r = '#'
    ans = ""
    for num in numbers:
        if num in (1, 4, 7):
            ans += 'L'
            l = str(num)
        elif num in (3,6,9):
            ans += 'R'
            r = str(num)
        else:
            tmp1 = (yx[l][0] - yx[str(num)][0], yx[l][1] - yx[str(num)][1])
            tmp2 = (yx[r][0] - yx[str(num)][0], yx[r][1] - yx[str(num)][1])
            ldist = 0
            rdist = 0
            ldist = abs(tmp1[0]) + abs(tmp1[1])
            rdist = abs(tmp2[0]) + abs(tmp2[1])
            if ldist< rdist:
                ans += 'L'
                l = str(num)
            elif rdist < ldist:
                ans += 'R'
                r = str(num)
            else:
                if hand == 'left':
                    ans += 'L'
                    l = str(num)
                else:
                    ans += 'R'
                    r = str(num)
    return ans

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5] , "right"))
