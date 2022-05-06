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
#
#

from collections import OrderedDict

def merge_the_tools(string, k):
    str_size = len(string)
    for i in range(0, str_size, k):
        print(''.join(OrderedDict.fromkeys(string[i:i + k])))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
