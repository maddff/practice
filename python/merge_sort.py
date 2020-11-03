def merge_sort(list, start, end):
    if end <= start:
        return
    mid = (start + end) // 2
    merge_sort(list, start, mid)
    merge_sort(list, mid + 1, end)
    left = start
    right = mid + 1
    temp_list = []
    while left <= mid and right <= end:
        if list[left] < list[right]:
            temp_list.append(list[left])
            left += 1
        if list[left] >= list[right]:
            temp_list.append(list[right])
            right += 1
    if left <= mid:
        temp_list += list[left:mid+1]
    if right <= end:
        temp_list += list[right:end+1]
    for i in range(0, len(temp_list)):
        list[i+start] = temp_list[i]

list = [5, 3, 1, 3, 7, 9, 8]
merge_sort(list, 0, len(list)-1)
print(list)