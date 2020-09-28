test_cases = int(input())
for test_case in range(test_cases):
    C, N = map(int, input().split())

    # answer = N combination C
    product = 1
    for _ in range(C):
        product *= N
        N -= 1

    product2 = 1
    for i in range(1, C+1):
        product2 *= i
    print(product//product2)