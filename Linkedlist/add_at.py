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
    def addAt(self,data,position):
        newNode=Node(data)
        currentposition=0
        tempNode=self.firstNode
        def length():
            len=0
            tempNode=self.firstNode
            while tempNode.next is not None:
                len+=1
                tempNode=tempNode.next
            return len
        if position>length() or position<0:
            print("sorry you have entered out of index")
        else:
            while True:
                if currentposition==position:
                    privousNode.next=newNode
                    newNode.next=tempNode
                    break
                else:
                    privousNode=tempNode
                    tempNode=tempNode.next
                    currentposition+=1


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
linkedlist.insert(40)
linkedlist.addAt(30,2)
linkedlist.printL()