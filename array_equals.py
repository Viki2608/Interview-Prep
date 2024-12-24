def check(arr1, arr2) -> bool:
        #code here
        arr1 = sorted(arr1)
        arr2 = sorted(arr2)
        print(arr1)
        print(arr2)
        
        if arr1 == arr2:
            return True
        return False

print(check([1,2,4,4,0],[2,4,5,0,1]))