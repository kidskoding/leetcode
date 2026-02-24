from collections import Counter

def isAnagram(s, t):
    # 1. Create two frequency HashMaps
    #   Let freq_s be a Counter that counts the frequencies of characters in string s
    #   Let freq_t be a Counter that counts the frequencies of characters in string t
    freq_s = Counter(s)
    freq_t = Counter(t)
    
    # 2. Check if the counters are equal
    #   If they are, return True because we know two words are an anagram where each character appears
    #   the same number of times in both strings
    #
    #   Otherwise, return False
    return freq_s == freq_t