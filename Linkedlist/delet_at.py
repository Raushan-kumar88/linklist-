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
    def deletAt(self,positon):
        currentPosition=0
        tempNode=self.firstNode
        while True:
            if currentPosition==positon:
                privousNode.next=None
                privousNode.next=tempNode.next
                break
                
            privousNode=tempNode
            tempNode=tempNode.next
            currentPosition+=1

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
linkedlist.deletAt(1)
linkedlist.printL()