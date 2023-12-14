T = int(input())
for i in range(T):
    A_elements = int(input())
    A = set(map(int, input().split()))
    B_elements = int(input())
    B = set(map(int, input().split()))
    if A.issubset(B):
        print('True')
    else:
        print('False')
