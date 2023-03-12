# 205. Isomorphic Strings
# Easy
# 6.3K
# 1.3K
# Companies
# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
# Example 1:
# Input: s = "egg", t = "add"
# Output: true
# Example 2:

# Input: s = "foo", t = "bar"
# Output: false
# Example 3:

# Input: s = "paper", t = "title"
# Output: true

def isIsomorphic(s: str, t: str) -> bool:
    if len(s) != len(t) :
        return False
    else:
        all_freq = {}
        all_freq_1 = {}
        for i in s:
            if i in all_freq:
                all_freq[i] += 1
            else:
                all_freq[i] = 1
        for k in t:
            if k in all_freq_1:
                all_freq_1[k] += 1
            else:
                all_freq_1[k] = 1
        if list(all_freq.values()).sort() == list(all_freq_1.values()).sort():
            return True
        else:
            return False
print(isIsomorphic("paper","title"))
print(isIsomorphic("egg","add"))
print(isIsomorphic("eeg","add"))