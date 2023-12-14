from collections import Counter
X = int(input())
shoes = Counter(map(int, input().split()))
N = int(input())
income = 0

for i in range(N):
    size, price = map(int, input().split())
    if shoes[size]:
        shoes[size] -= 1
        income += price

print(income)

# for i in range(N):
#     size, price = map(int, input().split())
#     if size in li and li[size] > 0:
#         li[size] -= 1
#         income += price