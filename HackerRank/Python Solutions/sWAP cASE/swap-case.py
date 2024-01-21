def swap_case(s):
    Output = '';
    for char in s:
        if(char.isupper()==True):
            Output += (char.lower());
        elif(char.islower()==True):
            Output += (char.upper());
        else:
            Output += char;
    return Output;

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
