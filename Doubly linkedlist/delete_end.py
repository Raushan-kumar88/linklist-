class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.back=None
class Dlinkedlist:
    def __init__(self):
        self.firstNode=None
    def insert(self,data):
        newNode=Node(data)
        if self.firstNode is None:
            self.firstNode=newNode
        else:
            temNode=self.firstNode
            while True:
                if temNode.next is None:
                    break
                else:
                    temNode=temNode.next
            temNode.next=newNode
            newNode.back=temNode
    def delete_end(self):
        if self.firstNode is None:
            print("linkedlist is empty can't delete")
        else:
            tempNode=self.firstNode
            while True:
                if tempNode.next is None:
                    privousNode.next=None
                    break
                else:
                    privousNode=tempNode
                    tempNode=tempNode.next
    def printdlinkedlist(self):
        if self.firstNode is None:
            print("the linkedlist is empty")
        else:
            tempNode=self.firstNode
            while True:
                print(tempNode.data)
                if tempNode.next is None:
                    break
                tempNode=tempNode.next

dlinkedlist=Dlinkedlist()
dlinkedlist.insert(10)
dlinkedlist.insert(20)
dlinkedlist.insert(30)
dlinkedlist.delete_end()
dlinkedlist.printdlinkedlist()