def topKFrequent(nums, k):
    map = {}
    for x in nums:
        map[x] = map.get(x, 0) + 1

    lst = list(map.items())
    lst.sort(key=lambda x: x[1], reverse=True)
    res = [x[0] for x in lst[:k]]

    return res

