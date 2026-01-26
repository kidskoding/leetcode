'''
Sliding window template for Sums and Averages
'''

# Sliding window sum / average
def sliding_window(nums, k):
    window_sum = sum(nums[:k])  # initial window sum
    result = [window_sum]
    
    for i in range(k, len(nums)):
        # slide window: remove left, add new right
        window_sum += nums[i] - nums[i - k]
        result.append(window_sum)
    return result

# Longest substring with no repeating characters
def longest_unique_substring(s):
    left = 0  # left boundary of window
    seen = {}  # stores last index of each character
    max_len = 0
    for right, char in enumerate(s):
        if char in seen and seen[char] >= left:
            # move left if character repeats inside window
            left = seen[char] + 1
        seen[char] = right
        max_len = max(max_len, right - left + 1)  # update max
    return max_len