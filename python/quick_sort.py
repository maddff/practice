def quick_sort(list, start, end):
    if start >= end:
        return
    left = start
    right = end
    flag = left
    while left < right:
        while right > left:
            if list[flag] > list[right]:
                list[flag], list[right] = list[right], list[flag]
                flag = right
                break
            right -= 1
        while left < right:
            if list[flag] < list[left]:
                list[flag], list[left] = list[left], list[flag]
                flag = left
                break
            left += 1
    quick_sort(list, start, flag)
    quick_sort(list, flag + 1, end)

list = [5, 3, 1, 3, 7, 9, 8]
quick_sort(list, 0, len(list)-1)
print(list)
