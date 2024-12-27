def remake(st):
    st = list(st)
    for i in range(len(st)):
        if st[i] == st[i].lower():
            st[i] = st[i].upper()
        else:
            st[i] = st[i].lower()
    st = st[::-1]
    return "".join(st)
print(remake("!РРЕПЙАВ ИЖАКс"))