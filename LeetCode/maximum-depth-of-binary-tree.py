"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""
# Python3 program to find the maximum depth of tree

# A binary tree node

# Compute the "maxDepth" of a tree -- the number of nodes
# along the longest path from the root node down to the
# farthest leaf node


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def treefy(m, root):
    m.left = Node(root.pop())
    m.right = Node(root.pop())


class Solution:
    def maxDepth(self, root):
        if root is None:
            return -1
        else:
            node = m = Node(root.pop())
            while root == []:
                treefy(m, root)
                m = m.lefy(m)
                treefy(m, root)
                m = m.right
            # Compute the depth of each subtree
            lDepth = self.maxDepth(node.left)
            rDepth = self.maxDepth(node.right)

            # Use the larger one
            if (lDepth > rDepth):
                return lDepth+1
            else:
                return rDepth+1


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

root = [1, 3, 4, 1, 2, 3, 4]

sol = Solution()
rs = sol.maxDepth(root)

print("Height of tree is %d" % (rs))
