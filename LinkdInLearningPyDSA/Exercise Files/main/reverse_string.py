"""
Python Data Structures - A Game-Based Approach
Stack challenge
"""

import stack

string = "gninraeL nIdekniL htiw tol a nraeL"
reversed_string = ""
s = stack.Stack()

# Your solution here.
for l in string:
    s.push(l)

while not s.is_empty():
    reversed_string += str(s.pop())


print(reversed_string)
