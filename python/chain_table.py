class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class ChainTable(object):
    def __init__(self):
        self.head = None
        self.__length = 0

    def insert(self, node):
        self.__length += 1
        if self.head == None:
            self.head = node
            return
        find_node = self.head
        while find_node.next != None:
            find_node = find_node.next
        find_node.next = node

    def find(self, index):
        if index > self.__length:
            return None
        now_index = 0
        find_node = self.head
        while now_index < index:
            find_node = find_node.next
            now_index += 1
        return find_node

ct = ChainTable()
ct.insert(Node("a"))
ct.insert(Node("b"))
ct.insert(Node("c"))
ct.insert(Node("d"))

node = ct.find(1)
print("find node:" + node.data)