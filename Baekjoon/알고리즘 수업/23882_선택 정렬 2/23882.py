def selection_sort(arr: list, n: int, end: int):
    count = 0
    for i in range(n):
        max_num = max(arr[:n - i])
        if(max_num != arr[n - i - 1]):
            for j in range(n - i - 1):
                if(arr[j] == max_num):
                    count += 1
                    temp = arr[n - i - 1]
                    arr[n - i - 1] = arr[j]
                    arr[j] = temp
                    if(count == end):
                        return arr
    return [-1]

if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    answer = selection_sort(arr, n, m)
    print(' '.join(map(str, answer)))