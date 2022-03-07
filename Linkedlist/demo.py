class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.firstNode=None
    def push(self,data):
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
    def pop(self):
        tempNode=self.firstNode
        while tempNode.next is not None:
            privousNode=tempNode
            tempNode=tempNode.next
        privousNode.next=None
    def printL(self):
        if self.firstNode is None:
            print("Linkedlist is empty")
        else:
            tempNode=self.firstNode
            while True:
                print(tempNode.data)
                if tempNode.next is None:
                    break
                else:
                    tempNode=tempNode.next
linkedlist=Linkedlist()




while(True):
    print("enter you choice ")
    print("1 for push ")
    print("2 for pop")
    print("3 for show linkedlist")
    print("4 for exit")
    choice=int(input())

    if(choice==1):
        data=int(input("enter the data :"))
        linkedlist.push(data)
    elif(choice==2):
        linkedlist.pop()
    elif(choice==3):
        linkedlist.printL()
    elif(choice==4):
        break
    else:
        
        print("you have enter invalid no ")

        
