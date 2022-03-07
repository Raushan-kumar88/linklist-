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
    def delete_end(self):
        tempNode=self.firstNode
        while tempNode.next is not None:
            privousNode=tempNode
            tempNode=tempNode.next
        privousNode.next=None

    def printL(self):
        if self.firstNode is None:
            print("it is empty")
        else:
            tempNode=self.firstNode
            while True:
                print(tempNode.data)
                if tempNode.next is None:
                    break
                else:
                    tempNode=tempNode.next

linklist=Linkedlist()
linklist.insert_end(78)  # push method
linklist.insert_end(79)
linklist.insert_end(76)
linklist.insert_end(71)
linklist.insert_end(73)
linklist.delete_head()
linklist.delete_end()     #pop method
linklist.printL()



