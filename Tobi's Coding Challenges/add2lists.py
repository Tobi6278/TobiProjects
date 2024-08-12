class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class Linked_List():
    def __init__(self):
        self.head = Node(data=None)
    
    def insert(self,value):
        new_node = Node(value)
        curr_node = self.head

        while curr_node.next != None:
            curr_node = curr_node.next
        
        curr_node.next = new_node

    def display(self):
        curr_node = self.head
        while curr_node.next != None:
            print(curr_node.data)
            curr_node = curr_node.next
        print(curr_node.data)
        

l_list = Linked_List()

l_list.insert(5)
l_list.display()
