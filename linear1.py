print("Raushan kumar")
"""def linear(list,e):
    for i in range(len(list)):
        if(list[i]==e):

            print("element is found",i)
            return
    print("element is not found")
    return
        

list=[]
n=int(input("enter the size of list="))
for i in range(0,n):
    ele=int(input())
    list.append(ele)
e=int(input("enter the element to be search="))
linear(list,e)
"""
def binary(list,e):
  length=len(list)
  low=0
  high=length-1
  while low<=high:
    mid=(low+high)//2
    if list[mid]==e:
      print("found at index",mid)
      return
    elif low<mid:
      low=mid+1
    else:
      high=mid+1
  print("element is not found")

list=[]
n=int(input("enter the size of list="))
for i in range(0,n):
  ele=int(input())
  list.append(ele)
e=int(input("which element you want to found="))
binary(list,e)
  
