class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preorder(root, path=""):
    """Root->Left->Right"""
    if root:
        path += str(root.data + "-")
        path = preorder(root.left, path)
        path = preorder(root.right, path)
    return path


def inorder(root, path=""):
    """Left->Root->Right"""
    if root:
        path = inorder(root.left, path)
        path += str(root.data + "-")
        path = inorder(root.right, path)
    return path


def postorder(root, path=""):
    """Left->Right->Root"""
    if root:
        path = postorder(root.left, path)
        path = postorder(root.right, path)
        path += str(root.data + "-")
    return path


if __name__ == '__main__':
    # Setup tree
    root = Node("A")
    root.left = Node("B")
    root.right = Node("C")
    root.left.left = Node("D")
    root.left.right = Node("E")
    root.right.left = Node("F")
    root.right.right = Node("G")
    root.left.left.left = Node("H")
    root.left.left.right = Node("I")

print("PreOrder")
print(preorder(root))
print("InOrder")
print(inorder(root))
print("PostOrder")
print(postorder(root))
