from collections import defaultdict


def find_me(page):
    tmp = page.split("<meta property=\"og:url\" content=")[1]
    tmp = tmp.split("/>")
    me = tmp[0][1:-1]
    return me


def find_href(page):
    tmp = page.split("<a href=\"")
    ret = []
    for str in tmp:
        if len(str) >5 and str[:5] == "https":
            me = str.split(">")[0][:-1]
            ret.append(me)
    return ret


def find_body(page):
    tmp = page.split("<body>")[1]
    tmp = tmp.split("<a href=")[0]
    return tmp


def find_basic_score(body, word):
    word = word.lower()
    words = []
    ret = 0
    tmp = ""
    for i in range(len(body)):
        if 'a' <= body[i] <= 'z' or 'A' <= body[i] <= 'Z':
            tmp += body[i]
        else:
            #words.append(tmp.lower())
            if word == tmp.lower():
                ret += 1
            tmp = ""
    # print(words)
    return ret


def solution(word, pages):
    basic_scores = {}
    graph = defaultdict(list)
    graph_nums = {}
    p2idx = {}
    p = []
    for i, page in enumerate(pages):
        me = find_me(page)
        refs = find_href(page)
        basic_score = find_basic_score(page, word)
        for ref in refs:
            graph[ref].append(me)
        graph_nums[me] = len(refs)
        basic_scores[me] = basic_score
        p2idx[me] = i
        p.append(me)
    ret = []
    for link in p:
        idx = p2idx[link]
        score = basic_scores[link]
        for ref in graph[link]:
            score += basic_scores[ref]/graph_nums[ref]
        ret.append((idx, score))
    ret.sort(key=lambda x: -x[1])
    return ret[0][0]


solution("Muzi", ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"])

