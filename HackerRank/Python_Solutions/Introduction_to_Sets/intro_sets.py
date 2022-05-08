def average(array):
    average_array = sum(set(array)) / len(list(set(array)))
    # print(sum(set(array)))
    # print(len(set(array)))
    return(format(average_array, ".3f"))

if __name__ == '__main__':
    n = int(input()) # size of array - n
    arr = list(map(int, input().split())) # array of n integers
    result = average(arr)
    print(result)