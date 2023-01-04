# An element is called a peak element if its value is not smaller than the value of its adjacent elements(if they exists).
# Given an array arr[] of size N, Return the index of any one of its peak elements.
# Note: The generated output will always be 1 if the index that you return is correct. Otherwise output will be 0. 


# Example 1:

# Input: 
# N = 3
# arr[] = {1,2,3}
# Possible Answer: 2
# Generated Output: 1
# Explanation: index 2 is 3.
# It is the peak element as it is 
# greater than its neighbour 2.
# If 2 is returned then the generated output will be 1 else 0.
# Example 2:

# Input:
# N = 2
# arr[] = {3,4}
# Possible Answer: 1
# Output: 1
# Explanation: 4 (at index 1) is the 
# peak element as it is greater than 
# its only neighbour element 3.
# If 1 is returned then the generated output will be 1 else 0.

# N =int(input())
# l=[]
# for i in range(N):
#     l.append(int(input("Enter array elements")))
# op=0
# for i in range(N-1):
#     if l[i]<l[i+1]:
#         op=i+1
# print(op)


a,b=0,1
count=0
while (count<5):
    c=a+b
    a=b
    b=c
    print(c)
    count +=1