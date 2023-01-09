# Given a vector of N positive integers and an integer X. The task is to find the frequency of X in vector.

# Example 1:

# Input:
# N = 5
# vector = {1, 1, 1, 1, 1}
# X = 1
# Output: 
# 5
# Explanation: Frequency of 1 is 5.

n=int(input("Enter number of array elements"))
l=[]
for i in range(n):
    l.append(int(input("Enter array elements")))
x=int(input("Enter X value"))
count =0
for i in range(n):
    if l[i]==x:
        count +=1
print(count)