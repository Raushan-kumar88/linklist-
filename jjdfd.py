class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.firstNode=None
    def insert_end(self,data):
        newNode=Node(data)
        if self.firstNode is None:
            self.firstNode=newNode
        else:
            tempNode=self.firstNode
            while True:
                if tempNode.next is None:
                    break
                else:
                    tempNode=tempNode.next
            tempNode.next=newNode
    def delete_head(self):
        tempNode=self.firstNode
        self.firstNode=None
        self.firstNode=tempNode.next

    def printL(self):
        if self.firstNode is None:
            print("Linked list is empty")
        else:
            tempNode=self.firstNode
            while True:
                print(tempNode.data)
                if tempNode.next is None:
                    break
                else:
                    tempNode=tempNode.next

    
    

linkist=Linkedlist()
linkist.insert_end(23)
linkist.insert_end(34)
linkist.insert_end(45)
linkist.insert_end(83)
linkist.insert_end(444)
linkist.insert_end(115)
linkist.printL()
print("--------------------------------")
linkist.delete_head()
linkist.delete_head()
linkist.delete_head()
linkist.printL()
