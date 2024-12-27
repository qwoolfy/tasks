def v(n):
    s = 0
    for i in range(n):
        x = int(input(f"L1= {i+1} "))
        y = int(input(f"L2= {i + 1} "))
        z = int(input(f"L3= {i + 1} "))
        s += x*y*z
    return s
print(v(3))
