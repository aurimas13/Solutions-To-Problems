N, X = input().split()
total = list()

for _ in range(int(X)):
    marks = map(float, input().split())
    total.append(marks)

for mark in zip(*total):
    print(sum(mark)/len(mark))