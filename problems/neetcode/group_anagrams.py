from collections import defaultdict
from typing import List

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    anagrams = defaultdict(list)
    for s in strs:
        key = str(sorted(s))
        anagrams[key].append(s)
    return list(anagrams.values())

print(groupAnagrams(strs = ["act","pots","tops","cat","stop","hat"]))
print(groupAnagrams(strs = ["x"]))
print(groupAnagrams(strs = [""]))