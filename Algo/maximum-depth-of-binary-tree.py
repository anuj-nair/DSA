"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


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
            data = self.list.pop()
            if data is not None:
                node.left = Node(data)
                if not self.list:
                    return
                self.q.enqueue(node.left)
            data = self.list.pop()
            if data is not None:
                node.right = Node(data)
                if node.data is not None:
                    self.q.enqueue(node.right)
            self.nodify()

    def treeify(self, root):
        r = 0
        self.list = list(reversed(root))
        data = self.list.pop()
        if data is not null:
            self.node = Node(data)
            r = self.node
            self.q.enqueue(r)
            self.nodify()
        return r

    def maxDepth(self, node):
        if not node:
            return 0
        else:
            if type(node) == list:
                node = self.treeify(node)

            if node == 0:
                return node
            # Compute the depth of each subtree
            lDepth = self.maxDepth(node.left)
            rDepth = self.maxDepth(node.right)

            # Use the larger one
            if (lDepth > rDepth):
                return lDepth+1
            else:
                return rDepth+1

    def print_tree(self, node):
        try:
            self.print_tree(node=node.left)
            print(node.data, end=' ')
            self.print_tree(node=node.right)
        except AttributeError:
            return


null = None
root = [3, 9, 20, null, null, 15, 7]
sol = Solution()
rs = sol.maxDepth(root)

print("Height of tree is %d" % (rs))
