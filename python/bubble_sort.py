def bubble_sort(list):
    for i in range(1, len(list)):
        for j in range(0, len(list) - i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]

list = [5, 3, 1, 7, 9, 8]
bubble_sort(list)
print(list)