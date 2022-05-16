K = int(input())
elements = list(map(int, input().strip().split()))
myset = set(elements)
print(((sum(myset)*K)-sum(elements))//(K-1))
# for i in elements:
#     if elements.count(i) == 1:
#         print(i)
