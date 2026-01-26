# Count frequency of elements
def count_freq(arr):
    freq = {}
    for x in arr:
        freq[x] = freq.get(x, 0) + 1
    return freq

# Prefix sum array for fast range queries
def prefix_sum(nums):
    n = len(nums)
    ps = [0] * (n + 1)
    for i in range(n):
        ps[i + 1] = ps[i] + nums[i]
    return ps
