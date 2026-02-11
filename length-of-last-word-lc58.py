# ============================================================
# 1. LeetCode link
# ============================================================
# https://leetcode.com/problems/length-of-last-word/


# ============================================================
# 2. DSA Pattern
# ============================================================
# String Traversal
# Reverse Traversal
# Two-pointer / Backward scan


# ============================================================
# 3. Brute Force Solution (code)
# ============================================================
# Approach:
# - Split the string by whitespace
# - Return length of the last word

def lengthOfLastWord_bruteforce(s: str) -> int:
    words = s.split()
    return len(words[-1]) if words else 0


# ============================================================
# 4. Time & Space (Brute) — explain why
# ============================================================
# Time Complexity: O(n)
# - split() scans the entire string
#
# Space Complexity: O(n)
# - split() creates a list of words


# ============================================================
# 5. Optimal Solution (code)
# ============================================================
# Approach:
# - Traverse string from the end
# - Skip trailing spaces
# - Count characters until a space is found
# - No extra memory used

def lengthOfLastWord(s: str) -> int:
    length = 0
    i = len(s) - 1

    # Skip trailing spaces
    while i >= 0 and s[i] == ' ':
        i -= 1

    # Count last word characters
    while i >= 0 and s[i] != ' ':
        length += 1
        i -= 1

    return length


# ============================================================
# 6. Dry Run (sample input)
# ============================================================
# Input: "   fly me   to   the moon  "
#
# Step 1: Skip trailing spaces
# i points to 'n'
#
# Step 2: Count characters
# 'n' -> 'o' -> 'o' -> 'm'
# length = 4
#
# Output: 4


# ============================================================
# 7. Time & Space (Optimal) — explain why
# ============================================================
# Time Complexity: O(n)
# - Worst case we scan the string once
#
# Space Complexity: O(1)
# - Only constant variables used
# - No extra data structures


# ============================================================
# 8. Followup Question
# ============================================================
# Q1: Why is split(" ") discouraged?
# A: It creates empty strings for multiple spaces
#
# Q2: Why is isalpha() incorrect here?
# A: A word is defined as non-space characters, not alphabet-only
#
# Q3: Can this be solved in one pass?
# A: Yes, by scanning from the end


# ============================================================
# 9. Edge Cases
# ============================================================
# - Empty string: ""
# - String with only spaces: "    "
# - Single word: "hello"
# - Trailing spaces: "hello   "
# - Words with symbols: "hello!"


# ============================================================
# 10. Mistake to Avoid (Critique + Follow-up)
# ============================================================
# ❌ Using split(" ") instead of split()
# ❌ Using isalpha() to detect words
# ❌ Finding the longest word instead of the last word
# ❌ Creating unnecessary arrays
#
# Interviewer Follow-up:
# - Can you solve this if input is a character stream?
# - What changes if the input is very large?
# - How would you write this in C (null-terminated string)?
