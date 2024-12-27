def language(st):
    st = st.replace("е", "3")
    st = st.replace("Е", "3")
    st = st.replace("а", "4")
    st = st.replace("А", "4")
    return st
print(language("Иван - ученик 10г класса"))
