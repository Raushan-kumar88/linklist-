arr=[12,34,67,23,21,78,99]
arr.sort()

search=int(input("Enter element to search:"))
low=0
high=len(arr)
if:
     while True:
    mid=(low+high)//2
    if arr[mid]==search:
        print("element found at ",mid)
        break
    elif arr[mid]>search:
        high=mid
    else:
        low=mid
else:
    print("element not found")
