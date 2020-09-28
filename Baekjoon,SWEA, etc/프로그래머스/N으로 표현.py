def solution(N, number):
    arr = [[] for _ in range(9)]
    arr[1].append(N)
    arr[1].append(-N)
    n = N
    for i in range(2, 9):
        """
        1->(1)
        2->(1,1) 
        3->(1, 2), (2, 1) <> (a@b)@c | a@(b@c)
        4->(1,3), (2, 2), (3, 1)
        """
        to_append = arr[i]
        n = n * 10 + N
        to_append.append(n)
        to_append.append(-n)
        temp = set([])
        for a in range(1, i):
            b = i - a
            for num1 in arr[a]:
                for num2 in arr[b]:
                    temp.add(num1+num2)
                    temp.add(num1-num2)
                    temp.add(num1*num2)
                    if num2 != 0:
                        temp.add(num1 // num2)
        for item in temp:
            to_append.append(item)
        for item in to_append:
            if item == number:
                return i

    return -1