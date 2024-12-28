def a(st):
    s = st.replace("+", "")
    ll = 0
    for i in range(1, len(st)-1):
        if st[i] != "+" and st[i-1] == "+" and st[i+1] == "+":
            ll += 1
    return True if len(s) == ll else False
print(a("+v+i+p+e+r+r+++++++++"))
print(a("+v+i+p+e+rr++"))