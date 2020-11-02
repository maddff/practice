class Queue(object):
    def __init__(self):
        self.data_list = []

    def insert(self, data):
        self.data_list.append(data)
    def pop(self):
        if len(self.data_list) == 0:
            return None
        data = self.data_list[0]
        del self.data_list[0]
        return data
    def size(self):
        return len(self.data_list)

queue = Queue()
print("before insert, queue size: " + str(queue.size()))
queue.insert("a")
queue.insert("b")
queue.insert("c")
queue.insert("d")
print("after insert, queue size: " + str(queue.size()))

print("pop queue data:")
print(queue.pop())
print(queue.pop())
print(queue.pop())
print(queue.pop())