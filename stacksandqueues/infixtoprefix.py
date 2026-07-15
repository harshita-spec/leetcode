# infix to prefix conversion using stack
def prec(c):
    if c == '^':  
        return 3
    elif c == '/' or c == '*':  
        return 2
    elif c == '+' or c == '-':  
        return 1
    else:
        return -1
    
def reverse(s):
    s = list(s)
    s.reverse() 
    for i in range(len(s)):
        if s[i] == '(':
            s[i] = ')'
        elif s[i] == ')':
            s[i] = '('
    return ''.join(s)

def infixToPrefix(s):
    s = reverse(s)
    
    st = []
    res = ""

    for c in s:
        if c.isalnum():
            res += c
        elif c == '(':
            st.append(c)
        elif c == ')':
            while st and st[-1] != '(':
                res += st.pop()
            st.pop()  
        else:
            while st and (prec(c) < prec(st[-1]) or 
                          (prec(c) == prec(st[-1]) and c != '^')):
                res += st.pop()
            st.append(c)

    while st:
        res += st.pop()

    return reverse(res)

s = "(a+b)*(c-d)+e"
print(infixToPrefix(s))
