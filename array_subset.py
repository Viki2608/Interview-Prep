def isSubset(a, b):
    # Convert array a into a set for O(1) lookups
    set_a = set(a)
    
    # Check if all elements of b are present in set_a
    for element in b:
        if element not in set_a:
            return False
    return True

print(isSubset([1, 2, 3, 4, 4, 5, 6],[1, 2, 4]))
print(isSubset([10, 5, 2, 23, 19],[19, 5, 3]))