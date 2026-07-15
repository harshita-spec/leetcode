# postfix to infix conversion using stack
def postfixToInfix(s):
    i=0
    st=[]
    for c in s:
        if c.isalnum():
            st.append(c)
        else:
            t1=st[-1]
            st.pop()
            t2=st[-1]
            st.pop()
            s='(' + t2 + c + t1 + ')'
            st.append(s)
    return st[-1]
s="ab+cde+**"
print(postfixToInfix(s))