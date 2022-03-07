arr=[12,34,67,23,21,78,99]
arr.sort()

search=int(input("Enter element to search:"))
low=0
count=0
high=len(arr)
while True:
    mid=(low+high)//2
    if arr[mid]==search:

        print("element found at ",mid)
        count+=1
        break
    elif arr[mid]>search:
        high=mid
    else:
        low=mid
if count>-1:
    print("ok input")
else:
    print("wrong input")

