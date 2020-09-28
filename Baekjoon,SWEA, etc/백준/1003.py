import sys
read = lambda :sys.stdin.readline().rstrip()
test_cases = int(read())

arr = [[1,0], [0, 1], [1, 1]]
for i in range(38):
    temp = [0, 0]
    temp[0] = arr[-1][0] + arr[-2][0]
    temp[1] = arr[-1][1] + arr[-2][1]
    arr.append(temp)

for test_case in range(test_cases):
    n = int(read())
    print('{} {}'.format(arr[n][0], arr[n][1]))