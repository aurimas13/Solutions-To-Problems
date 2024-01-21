if __name__ == '__main__':
    a = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        a.append([score, name])

    a.sort()
    b = a[1:]
    c = []

    for j in b:
        if j[0] == b[0][0]:
            c.append(j)

    for i in c:
        print(i[1])
