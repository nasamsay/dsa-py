import re
from tkinter import SEL_FIRST


class Stack():
    def __init__(self):
        self.items = []
    def push(self, item):
        return self.items.append(item)
    def pop(self):
        return self.items.pop()
    def is_empty(self):
        return self.items == []
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    
#Book stacks
'''myBookStacks = Stack()
print(myBookStacks.is_empty())
myBookStacks.push("School girl")
myBookStacks.push("No Longer A Human")
print(myBookStacks.peek())
myBookStacks.push("Kafka on the Shore")
myBookStacks.push("Out")
print(myBookStacks.items)
print(myBookStacks.peek())
myBookStacks.pop()
print(myBookStacks.peek())'''
