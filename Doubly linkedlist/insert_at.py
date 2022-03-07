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
    def insert_at(self,data,position):
        newNode=Node(data)
        currentPosition=0
        tempNode=self.firstNode
        while True:
            if currentPosition==position:
                privousNode.next=newNode
                newNode.back=privousNode
                newNode.next=tempNode
                break
            else:
                privousNode=tempNode
                tempNode=tempNode.next
                currentPosition+=1


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
dlinkedlist.insert(40)
dlinkedlist.insert_at(30,2)
dlinkedlist.printdlinkedlist()