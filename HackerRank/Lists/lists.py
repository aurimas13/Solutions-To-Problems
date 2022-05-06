if __name__ == '__main__':
    N = int(input())
    Output = [];
    for i in range(0, N):
        ip = input().split();
        if ip[0] == "print":
            print(Output)
        elif ip[0] == "insert":
            Output.insert(int(ip[1]), int(ip[2]))
        elif ip[0] == "remove":
            Output.remove(int(ip[1]))
        elif ip[0] == "pop":
            Output.pop();
        elif ip[0] == "append":
            Output.append(int(ip[1]))
        elif ip[0] == "sort":
            Output.sort();
        else:
            Output.reverse();

    # Output = [];
    # for i in range(0,N):
    #     ip = input().split();
    #     match ip[0]:
    #     case 'insert':
    #         Output.insert(int(ip[1]), int(ip[2]))
    #     case 'remove':
    #         Output.remove(int(ip[1]))
    #     case 'pop':
    #         Output.pop(int(ip[1]))
    #     case 'append':
    #         Output.append(int(ip[1]))
    #     case 'sort':
    #         Output.sort()
    #     case 'print':
    #         print(Output)
    #     case _:
    #         Output.reverse()
    #     };