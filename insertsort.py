def insertSort(arr):
    for i in range(1, len(arr)):
        cur = arr[i]
        j = i
        while arr[j - 1] > cur and j >= 1:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = cur

arr = [54,26,93,17,77,31,44,55,20, 4, 7, 2, 10, 5, 1, 89, 200]


insertSort(arr)
print(arr)