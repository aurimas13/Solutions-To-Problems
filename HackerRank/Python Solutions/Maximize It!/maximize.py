import itertools

NUMBER_OF_LISTS, MODULUS = map(int, input().split())
LISTS_OF_LISTS = []
for i in range(0, NUMBER_OF_LISTS):
    new_list = list(map(int, input().split()))
    del new_list[0]
    LISTS_OF_LISTS.append(new_list)


def squared(element):
    return element ** 2


COMBS = list(itertools.product(*LISTS_OF_LISTS))
RESULTS = []
for i in COMBS:
    result1 = sum(map(squared, [a for a in i]))
    result2 = result1 % MODULUS
    RESULTS.append(result2)
print(max(RESULTS))

# or
#
# from itertools import product
# args = list(map(int, input().split()))
# print(max([third.py([y**2 for y in x])%args[1] for x in product(*[map(int,input().split()[1:]) for _ in range(args[0])])]))

