n = int(input())
s = set(map(int, input().split()))
N = int(input())
for i in range(N):
    code = input().split()
    if code[0] == "remove":
        s.remove(int(code[1]))
    elif code[0] == "discard":
        s.discard(int(code[1]))
    else:
        s.pop()
print(sum(list(s)))


