def to_dict(lst):
    dt = {}
    for i in lst:
        dt[i] = i
    return dt
print(to_dict(["s","fig"]))

my_dict = {"first_one": "we can do it"}
def biggest_dict(**kwargs):
    global my_dict
    my_dict.update(**kwargs)
    return my_dict
print(biggest_dict(dog="Brock", cat="r"))

from collections import Counter
def count_it(sequence):
    counter_top3 = Counter(sequence).most_common(3)
    counter_top3 = dict(counter_top3)
    new_dict = {}
    for key, value in counter_top3.items():
        new_dict[int(key)] = value
    return new_dict
print(count_it("509362358910893746"))

dct = {"colour": "blue", "viperr": "mice", "movie": "marvel", "game": "dota", "language": "python"}
first = list(dct.values())[0]
second = list(dct.values())[-1]
dct[list(dct.keys())[0]] = second
dct[list(dct.keys())[-1]] = first
del(dct[list(dct.keys())[1]])
dct["new_key"] = "new_value"
print(dct)