integers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
opts = ['*', '#']
fac = {'S':1, 'D':2, 'T':3}

# def solution(dartResult):
#     """
#     dartResult : "1D2S#10S"
#     """
#     nums = []
#     options = []
#     N = len(dartResult)
#
#     while i < N:
#         if dartResult[i] in integers:
#             if dartResult[i] == '1':
#                 if dartResult[i + 1] == '0':
#                     num = int(dartResult[i:i + 2])
#                     i += 2
#                 else:
#                     num = int(dartResult[i])
#                     i += 1
#             else:
#                 num = int(dartResult[i])
#                 i += 1
#             if dartResult[i] == 'S':
#                 None
#             elif dartResult[i] == 'D':
#                 num = num ** 2
#             else:
#                 num = num ** 3
#             nums.append(num)
#
#         if i + 1 < len(dartResult) and dartResult[i + 1] in opts:
#             options.append(dartResult[i + 1])
#         else:
#             options.append(0)
#         i += 1
#
#     for i in range(3):
#         if options[i] == '*':
#             nums[i] *= 2
#             if i - 1 >= 0:
#                 nums[i - 1] *= 2
#         elif options[i] == '#':
#             nums[i] *= -1
#         else:
#             None
#     answer = sum(nums)
#
#     return answer


def solution(dartResult):
    """
    dartResult : "1D2S#10S"
    """
    nums = []
    options = []
    N = len(dartResult)

    # while i < N:
    #     if dartResult[i] in integers:
    #         if dartResult[i] == '1':
    #             if dartResult[i + 1] == '0':
    #                 num = int(dartResult[i:i + 2])
    #                 i += 2
    #             else:
    #                 num = int(dartResult[i])
    #                 i += 1
    #         else:
    #             num = int(dartResult[i])
    #             i += 1
    #         if dartResult[i] == 'S':
    #             None
    #         elif dartResult[i] == 'D':
    #             num = num ** 2
    #         else:
    #             num = num ** 3
    #         nums.append(num)
    #
    #     if i + 1 < len(dartResult) and dartResult[i + 1] in opts:
    #         options.append(dartResult[i + 1])
    #     else:
    #         options.append(0)
    #     i += 1

    i = 0
    string = dartResult
    j = 0
    for i in range(3):
        option = None
        if string[j] in integers and string[j+1] in integers:
            num = int(string[j:j+2])
            j += 2
        else:
            num = int(string[j:j+1])
            j += 1
        factor = fac[string[j]]
        j += 1
        if j < N and string[j] not in integers:
            option = string[j]
            j += 1
        nums.append(num ** factor)
        options.append(option)

    for i in range(3):
        if options[i] == '*':
            nums[i] *= 2
            if i - 1 >= 0:
                nums[i - 1] *= 2
        elif options[i] == '#':
            nums[i] *= -1
        else:
            None
    answer = sum(nums)

    return answer

print(solution("1S2D*3T"))