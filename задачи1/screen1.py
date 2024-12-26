# https://github.com/gogadantes/Tasks
# 1
# list=[2,5,9,3,4,5,7]
# list. reverse()
# print(list)

#2
# def change(list):
#     first=list.pop()
#     last=list.pop (0)
#     list.append(last)
#     list.insert(0, first)
#     return list
# print (change (['к', 'п', 'и', 'с', 'о', 'с']))
# print (change ([1, 2, 3]))

# 3
# def to_list(*args):
#     return list(args)
# print(to_list(4, 22,7,5,4,1,9))

#4
# def useless(lst):
#     return max(lst) / len(lst)
# print(useless ([2,125,3,4,62]))

#5
# def list_sort(lst):
#     lst. sort (key=lambda x: abs(x), reverse=True)
#     return lst
# print(list_sort ([-2,0.3,5,22, -0.23]))

#6
# new_num = []
# words = ['viperr', 'kaiangel', '9mice']
# def all_eq(words) :
#     bigger_len = len (max(words, key=len))
#     for change in words:
#         if len (change) == bigger_len:
#             new_num. append (change)
#         else:
#             while len(change) != bigger_len:
#                 change = change + "_"
#                 if len (change) == bigger_len:
#                     new_num. append (change) 
#     return (new_num)
# print(all_eq(words))
