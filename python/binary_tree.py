class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

'''
二叉树的每个节点最多有两个子节点
前序遍历: 根左右, 先访问根节点, 然后遍历左子树, 再遍历右子树
中序遍历: 左根右, 先遍历左子树, 然后根节点, 再遍历右子树
后序遍历: 左右根, 先遍历左子树, 然后右子树, 再根节点
'''
class BinaryTree(object):
    def __init__(self, root):
        self.root = root
    
    def pre_travelsal(self, root):
        if root:
            print(root.data)
        if root.left:
            self.pre_travelsal(root.left)
        if root.right:
            self.pre_travelsal(root.right)
    def in_travelsal(self, root):
        if root == None:
            return
        if root.left:
            self.in_travelsal(root.left)
        print(root.data)
        if root.right:
            self.in_travelsal(root.right)
    def post_travelsal(self, root):
        if root == None:
            return
        if root.left:
            self.post_travelsal(root.left)
        if root.right:
            self.post_travelsal(root.right)
        print(root.data)


root = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node8 = Node(8)
node9 = Node(9)

root.left = node2
root.right = node3
node2.left = node5
node2.right = node6
node3.left = node7
node7.left = node8
node7.right = node9

bt = BinaryTree(root)

print("pre-order travelsal: ")
bt.pre_travelsal(bt.root)
print("in-order travelsal: ")
bt.in_travelsal(bt.root)
print("post-order travelsal: ")
bt.post_travelsal(bt.root)

