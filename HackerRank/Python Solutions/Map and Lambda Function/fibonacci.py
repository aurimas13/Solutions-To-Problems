cube = lambda x: x**3

def fibonacci(n):
    a = 0
    b = 1
    fibo = []
    fibo.append(a)
    for _ in range(n-1):
        if n > 0:
            a, b = b, a+b
            fibo.append(a)
    if n == 0:
        fibo.remove(a)
        return fibo
    else:
        return fibo


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))

# or

# fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
# print(list(map(lambda x: x**3, fib[:int(input())])))