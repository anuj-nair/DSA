"""
Converting list to binary tree
"""

#from collections import deque


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        #        return len(self.items) == 0
        return not self.items

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        self.items.reverse()
        p = self.items.pop()
        self.items.reverse()
        return p

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[0]

    def __str__(self):
        return str(self.items)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.node = Node(None)
        self.q = Queue()
        self.list = []

    def nodify(self):
        if self.q.is_empty() or not self.list:
            return
        else:
            node = self.q.dequeue()
            node.left = Node(self.list.pop())
            if not self.list:
                return
            self.q.enqueue(node.left)
            node.right = Node(self.list.pop())
            self.q.enqueue(node.right)
            self.nodify()

    def treeify(self, root):
        self.list = list(reversed(root))
        self.node = Node(self.list.pop())
        r = self.node
        self.q.enqueue(r)
        self.nodify()
        return r

    def print_tree(self, node):
        try:
            self.print_tree(node=node.left)
            print(node.data, end=' ')
            self.print_tree(node=node.right)
        except AttributeError:
            return


root = [1, 2, 3, 4, 5, 6, 7, 8]
sol = Solution()
r = sol.treeify(root)
sol.print_tree(r)
