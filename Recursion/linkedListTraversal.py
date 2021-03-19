class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def travese(head):
    # Base Case
    if head is None:
        return
    # Recursive Case
    print(head.data)
    travese(head.next)


item1 = Node("Dog")
item2 = Node("Cat")
item3 = Node("Rat")
item1.next = item2
item2.next = item3

travese(item1)

head = Node("Owl", Node("Hen", Node(
    "Peacock", Node("Giraffe", Node("Donkey")))))
travese(head)
