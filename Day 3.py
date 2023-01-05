# You are given a string s. You need to reverse the string.

# Example 1:

# Input:
# s = Geeks
# Output: skeeG
# Example 2:

# Input:
# s = for
# Output: rof

def reverseWord(s):
    print(s[::-1])

reverseWord("Geeks")
reverseWord("for")

# Given an array arr[] and an integer K where K is smaller than size of array, the task is to find the Kth smallest element in the given array. It is given that all array elements are distinct.

# Example 1:

# Input:
# N = 6
# arr[] = 7 10 4 3 20 15
# K = 3
# Output : 7
# Explanation :
# 3rd smallest element in the given 
# array is 7.
# Example 2:

# Input:
# N = 5
# arr[] = 7 10 4 20 15
# K = 4
# Output : 15
# Explanation :
# 4th smallest element in the given 
# array is 15.

n=int(input("Enter number of array elements"))
l=[]
for i in range(n):
    l.append(int(input("Enter array elements:")))
k=int(input("Enter K element"))
l.sort()
print(l[k-1])

# Given an array A of size N of integers. Your task is to find the minimum and maximum elements in the array.

 

# Example 1:

# Input:
# N = 6
# A[] = {3, 2, 1, 56, 10000, 167}
# Output:
# min = 1, max =  10000
 

# Example 2:

# Input:
# N = 5
# A[]  = {1, 345, 234, 21, 56789}
# Output:
# min = 1, max = 56789

def getMinMax( a, n):
    a.sort()
    print(f"Min:{a[0]},Max:{a[-1]}")

getMinMax([1, 345, 234, 21, 56789],5)