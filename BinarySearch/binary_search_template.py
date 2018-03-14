def find(arr, key):
    """
    二分查找，找到该值在数组中的下标，否则为-1
    :param arr:
    :param key:
    :return:
    """
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] > key:
            end = mid - 1
        elif arr[mid] < key:
            start = mid + 1
        else:
            return mid
    return -1

def findFirstElememtByKey(arr, key):
    """
    查找第一个与key相等的元素
    :param arr:
    :param key:
    :return:
    """
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] >= key:
            end = mid - 1
        else:
            start = mid + 1
    return start if start < len(arr) else -1

def findLastElementByKey(arr, key):
    """
    查找最后一个与key相等的元素
    :param arr:
    :param key:
    :return:
    """
    start, end = 0, len(arr) -1
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] <= key:
            start = mid + 1
        else:
            end = start - 1
    return end if end >= 0 else -1

def findLastElementLessOrEqualThanKey(arr, key):
    """
    查找最后一个等于或者小于key的元素
    :param arr:
    :param key:
    :return:
    """
    start, end = 0, len(arr) -1
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] > key:
            end = mid - 1
        else:
            start = mid + 1
    return end

def findLastElementLessThanKey(arr, key):
    """
    查找最后一个小于key的元素
    :param arr:
    :param key:
    :return:
    """
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] >= key:
            end = mid - 1
        else:
            start = mid + 1
    return end

arr = [10, 15, 20, 20, 20, 24, 28, 30, 30, 56]

print(list(zip([i for i in range(len(arr))], arr)))
print(find(arr, 20))
print(findFirstElememtByKey(arr, 20))
print(findLastElementByKey(arr, 30))
print(findLastElementLessOrEqualThanKey(arr, 29))
print(findLastElementLessThanKey(arr, 30))
