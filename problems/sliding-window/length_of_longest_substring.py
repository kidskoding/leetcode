def lengthOfLongestSubstring(s):
    start = 0
    max_len = 0
    state = {}

    for end in range(len(s)):
        char = s[end]
        state[char] = state.get(char, 0) + 1

        while state[char] > 1:
            state[s[start]] -= 1
            start += 1

        max_len = max(max_len, end - start + 1)

    return max_len

print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))