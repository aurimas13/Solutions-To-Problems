if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

li = list(arr)
def runner_up(arr):
    max_value = -100
    second_max_value = -100
    for item in arr:
        if item > max_value and item > second_max_value:
            second_max_value = max_value
            max_value = item
        elif item < max_value and item > second_max_value:
            second_max_value = item
    return second_max_value

print(runner_up(li))
