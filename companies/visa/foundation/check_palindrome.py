import re

def checkPalindrome(s):
    # 1. Lowercase all characters of the string so that there is no case sensitivity
    s = s.lower()
    
    # 2. Include only alphabetic characters in the string 
    s = re.sub('[^a-z]', '', s)
    
    # 3. Let char_s be a list of characters that are in s
    char_s = list(s)
    
    # Loop through halfway to char_s. Halfway is only necessary because we can check subtract the current index from
    # len(char_s) - 1 to get the characters past halfway
    for i in range(len(char_s) // 2):
        # 4. Let end be the difference from the end of the string moving forwards as i increases
        end = len(char_s) - 1 - i
        
        # 5. If the characters at s[end] and s[i] are not equal, its not a palindrome because it cannot be 
        #   read forwards and backwards in this situation. Therefore, its safe to immediately return False
        if s[end] != s[i]:
            return False
    
    # 6. Return true if there is no character mismatch on each front and back of the string
    return True
