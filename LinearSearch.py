def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return None
target=40
arr=[10,20,30,40,50,60,70,80,90,100]
print(linear_search(arr,target))