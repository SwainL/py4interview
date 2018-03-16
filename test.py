import functools

arr = [1, 5, 2, 3, 8, 0]
arr.sort(key=functools.cmp_to_key(lambda a, b: a - b))



print(arr)