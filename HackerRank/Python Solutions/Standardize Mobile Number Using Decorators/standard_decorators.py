def wrapper(f):
    def fun(l):
        f(["+91 "+c[-10:-5]+" "+c[-5:] for c in l])
    return fun
# or
#
# def wrapper(f):
#     def fun(l):
#         decorated_l = ['+91 {} {}'.format(n[-10: -5], n[-5:]) for n in l]
#         return f(decorated_l)
#     return fun


@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')


if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)
