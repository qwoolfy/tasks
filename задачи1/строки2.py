def shortener(st):
    while "(" in st or ")" in st:
        left_s = st.rfind("(")
        right_s = st.find(")", left_s)
        st = st.replace(st[left_s:right_s + 1], "")
    return st
print(shortener("(рр)ni(ce)ne (hello g(os)(h)a) mi(n(i))ce(pls зачет)"))

def cleaned_str(st):
    clean_lst = []
    for s in st:
        if s != '@':
            clean_lst.append(s)
        elif s == '@' and clean_lst:
            clean_lst.pop()
    return ''.join(clean_lst)
print(cleaned_str("варенье@@@@@йогрут@@@@@питон@@@@ералаш@@@@рот@@"))
