def binary_search(list, target):
    left = 0
    right = len(list) - 1
    while left <= right:
        mid = (left + right) // 2
        if list[mid] < target:
            left = mid + 1
            continue
        if list[mid] == target:
            return mid
        if list[mid] > target:
            right = mid - 1
    return None

list = [1, 3, 4, 6, 8, 9]
print(binary_search(list, 5))
print(binary_search(list, 1))
print(binary_search(list, 3))
print(binary_search(list, 4))
print(binary_search(list, 6))
print(binary_search(list, 8))
print(binary_search(list, 9))