def reverseString(s):
    # 1. Let char_list be a list that contains the characters in string s
    char_list = list(s)
    
    # 2. Loop halfway through the string. The most efficient process of reversing a string involves
    #    flipping the characters 
    for i in range(len(char_list) // 2):
        # 3. Let end be the ending character needed to be swapped from s[i]
        #   This will keep decrementing from the end by i until halfway through the string
        #   s[end] will swap with s[i] to form the reversed string
        end = len(char_list) - 1 - i
        char_list[i], char_list[end] = char_list[end], char_list[i]
    
    # 4. Return the final resulting string
    return ''.join(char_list)