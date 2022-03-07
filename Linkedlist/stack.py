from xml.dom.minidom import Element


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack:
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
            print("Stsack is empty.......")
        else:
            tempNode=self.firstNode
            while True:
                print(tempNode.data)
                if tempNode.next is None:
                    break
                else:
                    tempNode=tempNode.next
stack=Stack()
while True:
    choice=int(input("\n 1---> push \n 2 ----> pop \n 3 ---> show \n 4 ----> exit \n"))
    if choice==1:
        ele=int(input("enter Element ="))
        stack.push(ele)
    elif choice==2:
        stack.pop()
    elif choice==3:
        stack.printL()
        break
    elif choice==4:
        break
    else:
        print("Invalid choice")

