def solution(skill, skill_trees):
    N= len(skill)
    possibles = [skill[0:N-i] for i in range(len(skill)) ] # 가능한 문자열 생성 skill = "CBD"라면, ["CBD", "CB", "C"] 이런순서로 와야됨
    cnt = 0
    for s in skill_trees:
        masked = ""
        for char in s:
            if char in skill:
                masked += char
        if masked:
            if masked in possibles:
                cnt += 1
        else:
            cnt += 1
    return cnt