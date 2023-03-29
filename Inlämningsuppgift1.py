# Fisnik Ferizi-> Inlämningsuppgift del 1
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
   
    def __str__(self):
        return str(self.data)
        
        
class Storage:
    def __init__(self):
        self.head = None
       
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
       
    def pop(self):
        if self.head is None:  # stack is empty
            return None
        popped_data = self.head.data
        self.head = self.head.next
        return popped_data
   
    def peek(self):
        if self.head is None:  # stack is empty
            return None
        return self.head.data
   
    def isempty(self):
        return self.head is None
 