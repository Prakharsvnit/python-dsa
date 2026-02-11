# ============================================================
# 1. LeetCode link
# ============================================================
# https://leetcode.com/problems/reverse-string/


# ============================================================
# 2. DSA Pattern
# ============================================================
# Two Pointers
# Left pointer starts from beginning
# Right pointer starts from end
# Swap and move pointers inward


# ============================================================
# 3. Brute Force Solution (code)
# ============================================================
# Approach:
# - Create a new reversed list using slicing
# - Copy elements back (NOT in-place)

def reverseString_bruteforce(s):
    reversed_s = s[::-1]   # creates a new list
    for i in range(len(s)):
        s[i] = reversed_s[i]


# ============================================================
# 4. Time & Space (Brute) — explain why
# ============================================================
# Time Complexity: O(n)
# - Reversing the list takes O(n)
# - Copying elements back also takes O(n)
#
# Space Complexity: O(n)
# - Extra list created using slicing


# ============================================================
# 5. Optimal Solution (code)
# ============================================================
# Approach:
# - Use two pointers
# - Swap elements in-place
# - No extra memory used

def reverseString(s):
    left, right = 0, len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


# ============================================================
# 6. Dry Run (sample input)
# ============================================================
# Input:  s = ["h","e","l","l","o"]
#
# Step 1:
# left = 0, right = 4
# swap 'h' and 'o'
# s = ["o","e","l","l","h"]
#
# Step 2:
# left = 1, right = 3
# swap 'e' and 'l'
# s = ["o","l","l","e","h"]
#
# Step 3:
# left = 2, right = 2 → stop
#
# Output: ["o","l","l","e","h"]


# ============================================================
# 7. Time & Space (Optimal) — explain why
# ============================================================
# Time Complexity: O(n)
# - Each element is swapped once
#
# Space Complexity: O(1)
# - Only constant extra variables used
# - In-place modification


# ============================================================
# 8. Followup Question
# ============================================================
# Q1: Why is slicing (s[::-1]) not allowed?
# A: Because slicing creates a new array, violating in-place constraint
#
# Q2: What if input was a string instead of list?
# A: Strings are immutable, so we must convert to list first


# ============================================================
# 9. Edge Cases
# ============================================================
# - Empty list: []
# - Single character: ["a"]
# - Even length string
# - Odd length string


# ============================================================
# 10. Mistake to Avoid
# ============================================================
# - Returning inside the loop
# - Using slicing in in-place problems
# - Iterating beyond len(s)//2
# - Using extra arrays when not allowed
