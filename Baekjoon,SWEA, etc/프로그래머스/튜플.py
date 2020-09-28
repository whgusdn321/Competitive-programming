def solution(s):
    sett = []
    for sub_str in s.split('}'):
        if sub_str == "" : continue
        temp = []
        for item in sub_str.split(','):
            real_item = ""
            for char in item:
                if char != "{":
                    real_item += char
            if real_item != "":
                temp.append(real_item)
        sett.append(temp)
        print("sett is : ", sett)
    answer = []
    return answer