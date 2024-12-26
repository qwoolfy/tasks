def search_substr(subst, st):
    if subst.lower in st.lower:
        print('Есть контакт!')
    else:
        print("Мимо!")


def first_last(letter, st):
    first = st.find(letter)
    if first < 0:
        return None, None
    last = st.rfind(letter)
    return first, last
print(first_last('A','Artem'))


from collections import Counter
def top3(st):
    counter_top3 = Counter(st.replace(' ', '')).most_common(3)
    print(counter_top3)
    return ', '.join([f'{letter} - {cnt}' for letter, cnt in counter_top3])
top3("fbehfuhwjdiwojdibvywghe  hufn ij ;dkdwl ;")


def camel(st):
    result = ''
    if st[0] == st[0].lower():
        x = 0
    else:
        x = 1
    for i in st:
        if i != ' ':
            if x == 0:
                result += i.upper()
                x = 1

            elif x == 1:
                result += i.lower()
                x = 0
        else:
            result += i

    return result
print(camel('viperr vip'))
