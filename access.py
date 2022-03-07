#linear Search Experiment:-
def linear(list,x):
    length = len(list)
    for i in range(0,n):
        if list[i] == x:
            print("Found at ","index",i,"Search Successful")
            return
    print("Search Unsuccessful ")
    return

print("Linear Sorting program\n")
list = []
n = int(input("Enter the number of element = "))
for i in range(0,n):
    ele = int(input())
    list.append(ele)
x=int(input("Enter the number to be searched = "))
linear(list,x)

#Binary search:-
def Binary(list,x):
    l = len(list)
    low = 0
    high = l-1 
    while low<= high:
        mid = (low+high)//2
        if list[mid] == x:
            print("Element is found at ",mid)
            return
        elif mid <x:
            low = mid+1
        else:
            high = mid+1
    print("Element is Not found ")
    return

print("Binary Sorting program\n")
list = []
n = int(input("Enter the size of list = "))
for i in range(0,n):
    ele = int(input())
    list.append(ele)
x=int(input("Enter the number to be serched = "))
result = Binary(list,x)
             
#insertion Sorting

def insertion(list):
    length = len(list)
    for i in range(0,length):
        key = list[i]
        j = i-1
        while j>=0 and key < list[j]:
            list[j+1]=list[j]
            j = j-1
        list[j+1]= key
    print(list)


print("Insertion Sorting program\n")
list = []
n = int(input("Enter the size of list = "))
for i in range(0, n):
   ele = int(input())
   list.append(ele)
insertion(list)


#Selection sorting
def Selection(list):
    length = len(list)
    for i in range(0,length-1):
        min = i
        for j in range(i+1,length):
            if list[j] <list[min]:
                min = j
        list[i],list[min]= list[min],list[i]
    print(list)
print("Selection sorting program\n")
list = []
n = int(input("Enter the size of list = "))
for i in range(0, n):
   ele = int(input())
   list.append(ele)
Selection(list)
