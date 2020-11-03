def insert_sort(list):
    sorted_list = []
    for i in range(0, len(list)):
        if len(sorted_list) == 0:
            sorted_list.append(list[i])
            continue
        for j in range(len(sorted_list) - 1, -1, -1):
            if sorted_list[j] <= list[i]:
                sorted_list.insert(j+1, list[i])
                break
            if j == 0:
                sorted_list.insert(0, list[i])
    list[:] = sorted_list[:]

list = [5, 3, 1, 7, 9, 8]
insert_sort(list)
print(list)