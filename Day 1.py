# N Students of different heights are attending an assembly. The heights of the students are represented by an array H[]. The problem is that if a student has less or equal height than the student standing in front of him, then he/she cannot see the assembly. Find the minimum number of students to be removed such that maximum possible number of students can see the assembly.
 
# Example 1:

# Input:
# N = 6
# H[] = {9, 1, 2, 3, 1, 5}
# Output:
# 2
# Explanation:
# We can remove the students at 0 and 4th index.
# which will leave the students with heights
# 1,2,3, and 5.
# Example 2:
# Input:
# N = 3
# H[] = {1, 2, 3} 
# Output :
# 0
# Explanation:
# All of the students are able to see the
# assembly without removing anyone.

N =int(input())
l=[]
for i in range(N):
    l.append(int(input("Enter heights")))
total = 0
for i in range(N-1):
    if l[i] > l[i+1]:
        total += 1

print(total)