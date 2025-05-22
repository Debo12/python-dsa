# Time Complexity - O(1)
# Space Complexity - O(1)
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    # Time Complexity - O(1)
    # Space Complexity - O(1)
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # Time Complexity - O(1)
    # Space Complexity - O(1)   
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1
    
    # Time Complexity - O(1)
    # Space Complexity - O(1)   
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    # Time Complexity - O(N)
    # Space Complexity - O(1)   
    def insert(self, index, value):
        new_node = Node(value)
        if index<0 or index>self.length:
            return False
        elif index==0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head
            for _ in range(index-1):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
        self.length += 1
        return True

    # Time Complexity - O(N)
    # Space Complexity - O(1) 
    def traverse(self):
        temp_head = self.head
        while temp_head is not None:
            print(temp_head.value)
            temp_head = temp_head.next
    
    # Time Complexity - O(N)
    # Space Complexity - O(1)
    def search(self, target_value):
        temp = self.head
        index = 0
        while temp is not None:
            if temp.value == target_value:
                return index
            temp = temp.next
            index += 1
        return -1
    
    # Time Complexity - O(N)
    # Space Complexity - O(1)
    def get(self, index):
        if index == -1:
            return self.tail
        elif index<-1 or index>=self.length:
            return None
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp
    
    # Time Complexity - O(N)
    # Space Complexity - O(1)
    def set(self, index, value):
        get_node = self.get(index)
        if get_node:
            get_node.value = value
            return True
        return False
    
    # Time Complexity - O(1)
    # Space Complexity - O(1)
    def pop_first(self):
        temp = self.head
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
            return temp
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        return temp
    
    # Time Complexity - O(N)
    # Space Complexity - O(1)
    def pop(self):
        if self.length == 0:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            self.tail = temp
            temp.next = None
        self.length -= 1
        return popped_node
    
    def remove(self, index):
        if index == 0:
            self.pop_first()
        if index == self.length-1 or index==-1:
            self.pop()
        if index >= self.length or index<-1:
            return None
        prev_node = self.get(index-1)
        popped_node = prev_node.next
        prev_node.next = popped_node.next
        popped_node.next = None
        self.length -= 1
        return popped_node
    
    # Time Complexity - O(1)
    # Space Complexity - O(1)
    def remove_all(self):
        self.head = None
        self.tail = None

    def __str__(self):
        temp = self.head
        values = []
        while temp is not None:
            values.append(str(temp.value))
            temp = temp.next
        return "->".join(values)
        

ll = LinkedList()
ll.append(20)
ll.append(30)
ll.prepend(10)
# print(ll.head.value)
# print(ll.tail.value)
# print(ll.length)
# print(ll)
ll.insert(1, 15)
# ll.traverse()
# print(ll.search(25))
# print(ll.get(2).value)
print(ll)
ll.set(2, 44)
print(ll)
ll.pop_first()
print(ll)
ll.pop()
print(ll)
ll.remove(1)
print(ll)
