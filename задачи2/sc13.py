def space(x):
    result = ''
    i_pred = ''
    result_kon = ''
    for i in x:
        if i != ' ' or i_pred != ' ':
            result += i
        i_pred = i
    for y in range(1, len(result)):
        result_kon += result[y]
    return (result_kon)
print(space('      Здравствуйте        ,     Георгий                                Владимирович          !'))