# Template for prefix sum
def prefixSumTemplate1(lst):
    prefixSum = []
    
    for i in range(1, len(prefixSum)):
        prefixSum[i] = prefixSum[i - 1] + lst[i]
        
    return prefixSum

# Can also modify existing array
def prefixSumTemplate2(lst):
    for i in range(1, len(lst)):
        lst[i] = lst[i - 1] + lst[i]
        
    return lst