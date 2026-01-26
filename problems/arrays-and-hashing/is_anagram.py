def isAnagram(s, t):
    if len(s) != len(t):
        return False
    
    count = {}
    
    for x in s:
        count[x] = count.get(x, 0) + 1
    
    for x in t:
        if x not in count:
            return False
        
        count[x] -= 1
        if count[x] < 0:
            return False
            
    return True

print(isAnagram(s = "racecar", t = "carrace"))
print(isAnagram(s = "jar", t = "jam"))