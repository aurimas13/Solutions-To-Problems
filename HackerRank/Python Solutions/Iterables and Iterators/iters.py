from itertools import combinations

N = int(input())
char = input().split()
K = int(input())

count = 0;
total = 0;

for i in combinations(char, K):
    count += 'a' in i
    total += 1

print(count / total)
