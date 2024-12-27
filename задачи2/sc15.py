def s(st):
    st = st.split(", ")
    sum = 1
    for i in range(len(st)):
        sum *= int(st[i])
    return sum
print(s("2, 4, 3"))
