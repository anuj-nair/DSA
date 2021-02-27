"""
Converting list to binary tree
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.node = Node(None)

    def nodify(self, node, root):
        try:
            node.left = Node(root.pop())
            node.right = Node(root.pop())
            self.nodify(node.left, root)
            self.nodify(node.right, root)

        except IndexError:
            return

    def treeify(self, root):
        root = list(reversed(root))
        self.node = Node(root.pop())
        r = self.node
        self.nodify(self.node, root)
        return r

    def print_tree(self, node):
        try:
            self.print_tree(node=node.left)
            print(node.data, end=' ')
            self.print_tree(node=node.right)
        except AttributeError:
            return


root = [1, 2, 3, 4, 5, 6, 7]
sol = Solution()
r = sol.treeify(root)
sol.print_tree(r)
