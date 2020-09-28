from collections import deque
def solution(cacheSize, cities):
    """

    :param cacheSize: 5
    :param cities: ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
    :return:
    """
    if cacheSize == 0:
        return len(cities)*5
    for i in range(len(cities)):
        cities[i] = cities[i].lower()
    cache = deque([])
    cnt = 0
    for city in cities:
        boool = False
        for i in range(len(cache)):
            if cache[i] == city:
                temp = cache[i]
                boool = True
                del cache[i]
                cache.append(temp)
                break
        if boool: #cache hit
            cnt += 1
        else:
            if len(cache) < cacheSize:
                cache.append(city)
            else:
                cache.popleft()
                cache.append(city)
            cnt += 5
    return cnt
