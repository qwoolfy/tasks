import re
def suma(s):
    numbers = re.findall(r'd', s)
    total_sum = sum(int(num) for num in numbers)
    return total_sum
x = "1jdj5fbfh8"
print(suma(x))