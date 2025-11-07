
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self,):
        self.head = None

    def __str__(self):
        return str(self.head)

    def pop(self):
        if self.isEmpty():
            return None
        else:
            data = self.head.data
            self.head = self.head.next
            return data


    def push(self, data):
        old_head = self.head
        self.head = Node(data, old_head)


    def isEmpty(self):
        return self.head is None


def main():
    stack = generateNodes(10)

    print(stack.head.data)

def generateNodes(n):
    stack = Stack()
    while n > 0:
        stack.push(Node(n))
        n -= 1
    return stack


main()
