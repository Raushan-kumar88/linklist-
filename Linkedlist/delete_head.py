class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.firstNode=None
    def insert(self,data):
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

    def deleteHead(self):
        tempNode=self.firstNode
        self.firstNode=None
        self.firstNode=tempNode.next

    def printL(self):
        if self.firstNode is None:
            print("the linkedlist is empty")
        else:
            tempNode=self.firstNode
            while True:
                print(tempNode.data)
                if tempNode.next is None:
                    break
                else:
                    tempNode=tempNode.next
linkedlist=Linkedlist()
linkedlist.insert(10)
linkedlist.insert(20)
linkedlist.insert(30)
linkedlist.deleteHead()
linkedlist.printL()