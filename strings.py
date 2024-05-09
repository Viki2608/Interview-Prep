# Length of string
# string = input()
# length = 0
# for i in string:
#     length += 1
# print(length)
# print(len(string))

# # Reverse the string

# print(string.split())
# l = [0, 8,0, 11, 0, 0,23, 24, 7, 9, 0]
# k=1
# # op = [8,11,23,24,7,9,0,0,0,0]

# for i in l:
#     if i == 0:
#         l.pop(l.index(i))
#         l.append(0)
#         print(l)

# print(l)
# i=0
# j=len(l)-1
# while i<=j:
#     if l[i] == 0 and l[j] != 0:
#         l[i],l[j] = l[j],l[i]
#     else:
#         j -= 1


# l.sort(reverse=True)
# print(l)
# print(l[-k])
# l1 = []
# l1.extend(l[k*-1:])
# l1.extend(l[:k*-1])
# print(l1)

def isAnagram(s: str, t: str) -> bool:
    if list(s).sort() == list(t).sort():
        print(list(s))
        print(list(t))
        return True
    else:
        print(list(s).sort())
        print(list(t).sort())
        return False

isAnagram("rat","car")

def longestConsecutive(nums: list[int]) -> int:
    if not nums:
        return 0

    nums.sort()
    longest_streak = 1
    current_streak = 1

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            if nums[i] == nums[i - 1] + 1:
                current_streak += 1
            else:
                longest_streak = max(longest_streak, current_streak)
                current_streak = 1

    return max(longest_streak, current_streak)

# Example usage
nums = [100, 4, 200, 1, 3, 2]
print(longestConsecutive(nums))  # Output: 4



longestConsecutive([0,3,7,2,5,8,4,6,0,1])


def first_missing_positive(nums):
    # Remove negative numbers and zeros
    nums = [num for num in nums if num > 0]

    # If no positive numbers remaining, return 1
    if not nums:
        return 1

    # Convert list to set for faster lookup
    nums_set = set(nums)

    # Find the smallest missing positive integer
    for i in range(1, len(nums) + 1):
        if i not in nums_set:
            return i

    # If all integers from 1 to len(nums) are present, return len(nums) + 1
    return len(nums) + 1

# Example usage
nums = [7,8,9,11,12,1]
print(first_missing_positive(nums))  # Output: 2
