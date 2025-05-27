# Stack with Python List (without limit)
class Stack:
    def __init__(self):
        self.list = []
    
    def __str__(self):
        if self.list:
            values = [str(i) for i in reversed(self.list)]
            return "\n".join(values)
        return "No list found"
    
    def push(self, value):
        self.list.append(value)
        return "The element has been successfully inserted"

    def pop(self):
        if self.is_empty():
            return "There is no element in the stack"
        value = self.list.pop()
        return f"{value} popped from the list"

    def is_empty(self):
        if self.list == []:
            return True
        return False

    def peek(self):
        if self.is_empty():
            return "There is no element in the stack"
        return self.list[-1]

    def delete(self):
        if self.is_empty():
            return "There is no element in the stack"
        self.list = None

s1 = Stack()
s1.push(1)
s1.push(2)
s1.push(3)
# s1.pop()
s1.delete()
print(s1)