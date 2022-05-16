T = int(input())
for x in range(T):
    lines = list(map(str, input().split()))
    try:
        print(int(int(lines[0])/int(lines[1])))
    except ZeroDivisionError:
        print('Error Code: integer division or modulo by zero')
    except ValueError as e:
        print('Error Code:', e)
