from itertools import combinations

def minion_game(string):
    consonants = 'BCDFGHJKLMNPQRSTVXZWY'
    vowels = 'AEIOU'

    kevin = [string[x:y] for x, y in combinations(range(len(string) + 1), r = 2) if string[x] in vowels]
    kevin_count = len(kevin)
    stuart = [string[x:y] for x, y in combinations(range(len(string) + 1), r=2) if string[x] in consonants]
    stuart_count = len(stuart)

    if stuart_count > kevin_count:
        print('Stuart', stuart_count)
    elif kevin_count > stuart_count:
        print('Kevin', kevin_count)
    elif kevin_count == stuart_count:
        print('Draw')
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)

    # kevin_count = 0
    # stuart_count = 0

    # for n in range(len(string)):
    #     if string[n].lower() in vowels.lower():
    #         for m in range(n + 1, len(string) + 1):
    #             print(m)
    #             string[n:m]
    #             kevin_count += 1
    #     elif string[n].upper() in consonants.upper():
    #         for m in range(n + 1, len(string) + 1):
    #             print('Hi')
    #             string[n:m]
    #             stuart_count += 1

    # print(kevin)
    # print(stuart)
    # for n in range(len(string)):
    #     for m in range(n + 1, len(string) + 1):
    #         if string[n] in vowels:
    #             kevin_count += 1
    #         elif string[n] in consonants:
    #             stuart_count += 1
    #
