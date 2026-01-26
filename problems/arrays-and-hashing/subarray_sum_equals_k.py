def subarraySum(nums, k):
    count = 0
    sum = 0
    map = {0: 1}
    
    for x in nums:
        sum += x
        if sum - k in map:
            count += map[sum - k]
        map[sum] = map.get(sum, 0) + 1

    return count