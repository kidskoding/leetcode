def isValid(s):
    lst = []
    for c in s:
        if c == '(' or c == '[' or c == '{':
            lst.append(c)
        elif c == ')' or c == ']' or c == '}':
            if len(lst) == 0: return False
            top = lst.pop()
            if (c == ')' and top != '(') or (c == ']' and top != '[') or (c == '}' and top != '{'):
                return False
    return len(lst) == 0