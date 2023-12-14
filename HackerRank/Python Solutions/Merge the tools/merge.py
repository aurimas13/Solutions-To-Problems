from collections import OrderedDict


def merge_the_tools(value, size):
    str_size = len(value)
    for i in range(0, str_size, size):
        print(''.join(OrderedDict.fromkeys(value[i:i + size])))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

# import sys
# from collections import OrderedDict
#
# def merge_the_tools(string, k):
#     str_size, part_size = len(string), int(len(string)/k)
#     values = []
#
#     # if str_size % k != 0:
#     #     sys.exit()
#     # else:
#     #     part_size = int(part_size)
#
#     for i in range(0, str_size, part_size):
#         # print(string[i:i+part_size])
#         # print(i)
#         values.append(string[i:i+part_size])
#     # print(values)
#
#     for i in range(len(values)):
#         print(''.join(OrderedDict.fromkeys(values[i])))
#
# if __name__ == '__main__':
#     string, k = input(), int(input())
#     merge_the_tools(string, k)
