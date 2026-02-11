# ALSO TODO: followup: valindrome number without converting tos tring

# =========================================================
# 1. LeetCode link
# =========================================================
# https://leetcode.com/problems/palindrome-number/


# =========================================================
# 2. DSA Pattern
# =========================================================
# String manipulation / Two-pointer / Math-based reversal


# =========================================================
# 3. Brute Force Solution (code)
# =========================================================
# Idea:
# Convert the number to string, reverse it, and compare.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        b = list(str(x))
        return b == b[::-1]


# =========================================================
# 4. Time & Space (Brute) — explain why
# =========================================================
# Time Complexity:
# O(n) — where n is the number of digits in x
# - Converting to string takes O(n)
# - Reversing the list takes O(n)
#
# Space Complexity:
# O(n) — extra space used to store the list of digits


# =========================================================
# 5. Optimal Solution (code)
# =========================================================
# Idea:
# Reverse only HALF of the number using math.
# Avoid string conversion and extra space.

class SolutionOptimal:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers and numbers ending with 0 (except 0) cannot be palindrome
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0

        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        # For even digits: x == reversed_half
        # For odd digits: x == reversed_half // 10
        return x == reversed_half or x == reversed_half // 10


# =========================================================
# 6. Dry Run (sample input)
# =========================================================
# Input: x = 1221
#
# Step 1:
# x = 1221, reversed_half = 0
#
# Step 2:
# reversed_half = 1, x = 122
#
# Step 3:
# reversed_half = 12, x = 12
#
# Loop stops (x == reversed_half)
#
# Return True


# =========================================================
# 7. Time & Space (Optimal) — explain why
# =========================================================
# Time Complexity:
# O(n) — processes half the digits (still linear)
#
# Space Complexity:
# O(1) — only integer variables used, no extra data structures


# =========================================================
# 8. Followup Question
# =========================================================
# Q1: Can you solve it without converting the number to a string?
# Q2: Can you reverse the number fully and compare?
# Q3: What happens with very large integers?


# =========================================================
# 9. Edge Cases
# =========================================================
# x = 0        → True
# x = -121     → False (negative sign)
# x = 10       → False (leading zero issue)
# x = 7        → True (single digit)


# =========================================================
# 10. Mistake to Avoid
# =========================================================
# ❌ Forgetting that negative numbers are never palindromes
# ❌ Ignoring numbers ending with 0
# ❌ Using extra space when interviewer asks for O(1)
# ❌ Reversing the entire number unnecessarily
