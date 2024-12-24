def search(arr, x):
    index = -1
    for i in range(len(arr)):
        if arr[i] == x:
            index = i
    return index
            
    
print(search(arr=[1, 2, 3, 4],x= 3))
print(search(arr=[10, 8, 30, 4, 5], x = 5))

print(search(arr=[10, 8, 30], x = 6))
