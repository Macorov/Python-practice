def solve(st,a,b):
    st = list(st)
    k = st[a]
    l = st[b]
    st = str(st)
    st.replace(a, l)
    st.replace(b, k)
    ''.join(st)
    return st
print(solve("codewars",1,5))