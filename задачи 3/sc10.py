def money(lst):
    if len(lst) % 3 == 0: return "можно"
    return "нельзя"
print(money(["coin", "coin", "coin", "coin", "coin"]))
print(money(["coin", "coin", "coin", "coin", "coin", "coin"]))