def пароль(p):
    ad = 0
    is_number = False
    is_letter = False
    is_upper = False
    if len(p) >= 8:
        ad += 1
    if "@" in p or "_" in p or "*" in p or "&" in p or "#" in p:
        ad += 1
    for item in p:
        try:
            if int(item) in range(0,10):is_number = True
        except ValueError:
            if item == item.upper(): is_upper = True
            is_letter = True
    if is_number: ad += 1
    if is_letter: ad += 1
    if is_upper: ad += 1
    return f"{ad} / 5"
print(пароль("Ivan_2008"))
print(пароль("Ivan2008"))
print(пароль("Ivan08"))
print(пароль("ivan08"))
print(пароль("ivan"))