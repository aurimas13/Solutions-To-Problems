from collections import deque

a_deque = deque()

N = int(input())
for i in range(N):
    line = list(map(str, input().split()))
    if line[0] == 'append':
        a_deque.append(line[1])
    elif line[0] == 'appendleft':
        a_deque.appendleft(line[1])
    elif line[0] == 'popleft':
        a_deque.popleft()
    elif line[0] == 'pop':
        a_deque.pop()

print(' '.join(a_deque))