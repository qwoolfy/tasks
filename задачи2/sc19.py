def massiv(x):
    a = []
    result = 0
    for i in x:
        result += i
        a.append(result)
    return (a)
print(massiv([1, 2, 3, 4, 5, 6, 7]))