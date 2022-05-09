from collections import OrderedDict
N = int(input())
ordered_dictionary = OrderedDict()

for i in range(N):
    name_value = list(map(str, input().split()))
    price = int(name_value[-1])
    # if len(name_value) > 2:
    item_name = ' ' .join(name_value[:-1])
    # else:
    #     item_name = str(name_value[0])
    #     price = int(name_value[1])
    if item_name in ordered_dictionary.keys():
        ordered_dictionary[item_name] += price
    else:
        ordered_dictionary[item_name] = price

for i in ordered_dictionary:
    print(i, ordered_dictionary[i])

# print(ordered_dictionary)
