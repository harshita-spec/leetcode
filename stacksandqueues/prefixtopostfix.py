# prefix to postfix conversion using stack
def prefixtopostfix(s):
    i=len(s)-1
    st=[]
    while i>=0:
        if s[i].isalnum():
            st.append(s[i])
        else:
            t1=st.pop()
            t2=st.pop()
            s1=t1+t2+s[i]
            st.append(s1)
        i-=1
    print(st[-1])
s="*+PQ-MN"
prefixtopostfix(s)