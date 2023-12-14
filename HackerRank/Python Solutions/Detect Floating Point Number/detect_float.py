import re


class Main:
    def __init__(self):
        self.n = int(input())

        for i in range(self.n):
            self.s = input()
            print(bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$', self.s)))


if __name__ == '__main__':
    obj = Main()
