class Stack(object):
    def __init__(self):
        self.data_list = []
    def insert(self, data):
        self.data_list.append(data)
    def pop(self):
        if len(self.data_list) == 0:
            return None
        data = self.data_list[-1]
        del self.data_list[-1]
        return data
    def size(self):
        return len(self.data_list)

stack = Stack()
print("before insert, stack size: " + str(stack.size()))
stack.insert("a")
stack.insert("b")
stack.insert("c")
stack.insert("d")
print("after insert, stack size: " + str(stack.size()))
print("pop stack data:")
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())