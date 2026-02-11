"""
LeetCode: https://leetcode.com/problems/valid-palindrome/

DSA Pattern:
Two Pointers / String Processing
"""

# --------------------------------------------------
# Brute Force Solution
# --------------------------------------------------

def isPalindrome_brute(s: str) -> bool:
    filtered = []
    for ch in s:
        if ch.isalnum():
            filtered.append(ch.lower())

    filtered = "".join(filtered)
    return filtered == filtered[::-1]


"""
Time & Space Complexity (Brute):
Time: O(n)
- One pass to filter characters
- One pass to reverse string

Space: O(n)
- Extra string used to store filtered characters
"""

# --------------------------------------------------
# Optimal Solution
# --------------------------------------------------

def isPalindrome(s: str) -> bool:
    s1 = []
    for char in s:
        if char.isalnum():
            s1.append(char.lower())

    s1 = "".join(s1)
    return s1 == s1[::-1]


"""
Dry Run:
Input: "A man, a plan, a canal: Panama"

Filtered string: "amanaplanacanalpanama"
Reverse:          "amanaplanacanalpanama"

Result: True
"""

"""
Time & Space Complexity (Optimal):
Time: O(n)
- Single traversal to clean string
- Comparison with reversed string

Space: O(n)
- Extra space for cleaned string
"""

"""
Edge Cases:
- Empty string -> True
- String with only symbols ("!!!") -> True
- Single character -> True
- Mixed case letters
"""

"""
Mistake to Avoid:
- Forgetting to ignore non-alphanumeric characters
- Not converting characters to lowercase before comparison
"""
