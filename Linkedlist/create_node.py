class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def inset(self,newNode):
        if self.head is None:
            self.head=newNode
        else:
            temp=self.head
            while True:
                if temp.next is None:
                    break
                else:
                    temp=temp.next
            temp.next=newNode
    def printlinkedlist(self):
        if self.head is None:
            print("the linked list is empty")
        else:
            temp=self.head
            while temp is not None:
                temp=temp.next
        print(temp.data)
firstNode=Node(1)
linkedlist=Linkedlist()
linkedlist.inset(firstNode)
linkedlist.printlinkedlist        