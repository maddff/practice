'''
堆的特点:
1. 堆是一个二叉树
2. 叶子节点只存在最下两层
3. 堆的根节点到倒数第二层是一个完全二叉树(除了叶子节点, 其他节点都有两个节点)
4. 一个节点不可能只有右子节点
5. 大顶堆: 父节点必大于子节点. 小顶堆: 父节点必小于子节点 
'''
class Heap(object):
    def __init__(self):
        self.data_list = []

    def size(self):
        return len(self.data_list)
    def left_child_index(self, root_index):
        return root_index * 2 + 1
    def right_child_index(self, root_index):
        return root_index * 2 + 2
    def father(self, node):
        return (node - 1) // 2
    def heapify(self, root_index):
        if root_index >= self.size():
            return
        left_index = self.left_child_index(root_index)
        right_index = self.right_child_index(root_index)
        largest = root_index
        if left_index < self.size():
            if self.data_list[left_index] > self.data_list[largest]:
                largest = left_index
        if right_index < self.size():
            if self.data_list[right_index] > self.data_list[largest]:
                largest = right_index
        if largest != root_index:
            self.data_list[root_index], self.data_list[largest] = self.data_list[largest], self.data_list[root_index]
            self.heapify(largest)
    def build(self):
        for i in range(self.size()//2, 0, -1):
            self.heapify(i)
    def get_max(self):
        if self.size() == 0:
            return None
        max = self.data_list[0]
        self.data_list[0] = self.data_list[-1]
        del self.data_list[-1]
        self.heapify(0)
        return max
    def insert(self, data):
        self.data_list.append(data)
        if self.size() == 1:
            return
        now_index = self.size() - 1
        father_index = self.father(now_index)
        while self.data_list[father_index] < data and now_index != 0:
            self.data_list[father_index], self.data_list[now_index] = self.data_list[now_index], self.data_list[father_index]
            now_index = father_index
            father_index = self.father(now_index)

heap = Heap()
heap.insert(9)
heap.insert(10)
heap.insert(7)
heap.insert(12)
heap.insert(3)
heap.insert(4)
print(heap.get_max())
print(heap.get_max())
print(heap.get_max())
print(heap.get_max())
print(heap.get_max())
print(heap.get_max())
print(heap.get_max())
heap.insert(10)
heap.insert(9)
heap.insert(8)
heap.insert(7)
heap.insert(7)
heap.insert(12)
print(heap.get_max())
heap.data_list = [None, 1, 2, 3, 4, 5, 6, 7]
heap.build()
print(heap.get_max())