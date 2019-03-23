class Node:
    def __init__(self, data):

        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def isEmpty(self):
        # this block check the linked list

        if self.top == None:
            return True
        else:
            return False

    def push(self, data):

        # this block add the element into stack

        node = Node(data)
        node.next = self.top
        self.top = node

    def pop(self):

        # this block pop the element one by one

        if self.top is None:
            return "Stack empty"

        element = self.top
        self.top = self.top.next
        return element.data

    def size(self):

        # this block check the size of the linked list

        temp = self.top
        count = 0
        while temp != None:
            count += 1
            temp = temp.next
        return count

    def print(self):

        # this block print the element

        if self.top is None:
            print("Stack is empty!!!")
            return
        current = self.top
        while current != None:
            print(current.data)
            current = current.next
