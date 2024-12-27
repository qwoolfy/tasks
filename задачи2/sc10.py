def xy (x,y):
    lst_xy = []
    for i in range(len(x)):
        tr = (x[i], y[i])
        lst_xy.append(tr)
    return lst_xy
print(xy([666,888,777],[6,8,7]))