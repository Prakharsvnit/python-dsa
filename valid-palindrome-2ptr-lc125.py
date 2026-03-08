# ============================================================
# 1. LeetCode Link / Problem Description
# ============================================================

# Problem Link:
# https://leetcode.com/problems/valid-palindrome/description/

"""
Problem Summary:

Given a string s, determine if it is a palindrome, considering only
alphanumeric characters and ignoring cases.

A palindrome reads the same forward and backward.

Constraints:
- Ignore spaces, punctuation, and special characters.
- Comparison should be case-insensitive.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: True

Explanation:
After removing non-alphanumeric characters and converting to lowercase:
"amanaplanacanalpanama" which is a palindrome.

Example 2:
Input: s = "race a car"
Output: False

Example 3:
Input: s = " "
Output: True
"""

# ============================================================
# 2. DSA Pattern Identification
# ============================================================

"""
Core Pattern: Two Pointers

Why Two Pointers?

- We need to compare characters from both ends of the string.
- We move one pointer from the left and one from the right.
- Skip non-alphanumeric characters.
- Compare characters after converting to lowercase.

This avoids building a new string and allows in-place validation.

Key Idea:
left pointer  -> moves forward
right pointer -> moves backward

If characters mismatch -> not a palindrome.

Alternative Patterns:

1. String Filtering + Reverse
   - Clean the string (keep alphanumeric)
   - Compare with reversed string

2. Stack
   - Push characters and compare with pop
   - Not efficient compared to two pointers

3. Regular Expression Cleaning
   - Remove non-alphanumeric
   - Compare reversed

However, the Two Pointer approach is optimal in interviews because:
- O(n) time
- O(1) extra space
"""

# ============================================================
# 3. Interview Critique of My Solution
# ============================================================

"""
NOTE:
Since the user did not provide an implementation, this section
explains the typical issues interviewers see with candidate solutions.

Logic & Accuracy Issues (Common Problems):

1. Forgetting to skip non-alphanumeric characters
2. Not converting characters to lowercase
3. Incorrect pointer movement
4. Checking palindrome before filtering characters
5. Using extra memory unnecessarily

Complexity Analysis (Typical Candidate Approach):

If candidate builds a cleaned string first:

Time Complexity:
O(n)

Steps:
- Iterate through string to filter characters -> O(n)
- Reverse string -> O(n)
- Compare -> O(n)

Total -> O(n)

Space Complexity:
O(n)
because we store a new filtered string.

Code Quality Expectations:

Interviewers look for:

Good:
- clear variable names
- minimal extra memory
- readable logic
- proper edge case handling

Bad:
- nested conditions
- unnecessary string copying
- complicated logic

Edge Cases Often Missed:

- Empty string
- Only punctuation
- Single character
- Mixed casing
- Unicode characters
"""

# ============================================================
# 4. My Original Solution (As Provided)
# ============================================================

# NOTE: No code was provided by the user.
# Placeholder for where the original solution would appear.

# Example placeholder implementation (not used in analysis):

class PlaceholderSolution:
    def isPalindrome(self, s: str) -> bool:
        filtered = ""

        for c in s:
            if c.isalnum():
                filtered += c.lower()

        return filtered == filtered[::-1]


# ============================================================
# 5. Brute Force Solution (Interview Friendly)
# ============================================================

"""
Idea:

1. Remove all non-alphanumeric characters.
2. Convert everything to lowercase.
3. Check if the cleaned string equals its reverse.

This is easy to derive in an interview.
"""

class BruteForceSolution:

    def isPalindrome(self, s: str) -> bool:
        cleaned = []

        # Filter only alphanumeric characters
        for char in s:
            if char.isalnum():
                cleaned.append(char.lower())

        cleaned_str = "".join(cleaned)

        # Compare with reversed version
        return cleaned_str == cleaned_str[::-1]


"""
Brute Force Complexity Analysis:

Time Complexity: O(n)

Step-by-step:
1. Iterate through string -> O(n)
2. Create cleaned string -> O(n)
3. Reverse string -> O(n)

Total: O(n)

Space Complexity: O(n)

Reason:
- We store the cleaned version of the string.
"""

# ============================================================
# 6. Optimal Solution (Interview Accepted Version)
# ============================================================

"""
Optimal Strategy: Two Pointer Technique

Instead of creating a new string, we:

1. Use two pointers:
   left  -> start
   right -> end

2. Skip non-alphanumeric characters.

3. Compare lowercase characters.

4. Move pointers inward.

Advantages:
- No extra memory allocation
- More efficient for large inputs
"""

class OptimalSolution:

    def isPalindrome(self, s: str) -> bool:

        left = 0
        right = len(s) - 1

        while left < right:

            # Skip non-alphanumeric from the left
            while left < right and not s[left].isalnum():
                left += 1

            # Skip non-alphanumeric from the right
            while left < right and not s[right].isalnum():
                right -= 1

            # Compare characters
            if s[left].lower() != s[right].lower():
                return False

            # Move both pointers
            left += 1
            right -= 1

        return True


"""
Optimal Complexity Analysis:

Time Complexity: O(n)

Explanation:

Each character is visited at most once
by either left or right pointer.

Therefore total operations ≈ n.

Space Complexity: O(1)

Explanation:
We only use a few variables (left, right).
No extra data structures are created.
"""

# ============================================================
# 7. Follow-up Questions (Interview Level)
# ============================================================

"""
Q1: What if the input string is extremely large (GBs of data)?

A1:

We cannot store the whole cleaned string in memory.

Solution:
- Use streaming comparison
- Two pointer approach if random access is available
- If streaming only:
    - Use rolling buffers
    - Process chunks

In distributed systems:
- Use MapReduce style preprocessing.

------------------------------------------------

Q2: How would you check if a string can become a palindrome
by removing at most one character?

A2:

LeetCode Variant:
"Valid Palindrome II"

Approach:
- Two pointers
- When mismatch occurs:
    check skipping left OR skipping right

Time Complexity: O(n)

Pseudo logic:

if s[left] != s[right]:
    return check(left+1, right) or check(left, right-1)

------------------------------------------------

Q3: How would you check palindrome ignoring Unicode accents?

Example:
"é" == "e"

A3:

Use Unicode normalization:

import unicodedata

s = unicodedata.normalize("NFKD", s)

Then remove combining characters before palindrome check.

This is important for internationalized systems.
"""

# ============================================================
# 8. Edge Cases Checklist
# ============================================================

"""
Important Edge Cases:

✓ Empty string
Input: ""
Output: True

✓ Only punctuation
Input: "!!!"
Output: True

✓ Single character
Input: "a"
Output: True

✓ Mixed case
Input: "Aa"
Output: True

✓ Non-palindrome with punctuation
Input: "race a car"
Output: False

✓ Large string
Input length up to 2*10^5
"""

# ============================================================
# 9. Mistakes to Avoid
# ============================================================

"""
Common Pitfalls:

1. Not ignoring special characters
Example:
"A man, a plan..."

2. Case sensitivity errors

3. Using string concatenation repeatedly
This creates O(n^2) behavior in Python.

Bad:
filtered += char

Better:
use list + join

4. Incorrect pointer movement

5. Checking palindrome before filtering characters

6. Forgetting boundary conditions when skipping characters
"""

# ============================================================
# 10. Final Takeaways
# ============================================================

"""
What Interviewers Are Testing:

1. Pattern Recognition
   Recognizing the Two Pointer technique.

2. String Handling Skills
   Understanding built-in methods like:
   - isalnum()
   - lower()

3. Edge Case Awareness

4. Space Optimization
   Avoid unnecessary extra strings.

Key Insight:

Whenever you see:
"compare symmetric elements"

Think immediately:

TWO POINTERS.

This pattern appears in:

- Valid Palindrome
- Container With Most Water
- Two Sum II
- Reverse String
- 3Sum / 4Sum
- Remove Duplicates from Sorted Array
"""

if __name__ == "__main__":
    solver = OptimalSolution()

    test_cases = [
        "A man, a plan, a canal: Panama",
        "race a car",
        " ",
        "madam",
        "No lemon, no melon"
    ]

    for test in test_cases:
        print(f"Input: {test}")
        print("Is Palindrome:", solver.isPalindrome(test))
        print("-" * 40)