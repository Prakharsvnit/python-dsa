"""
1. LeetCode Link or Problem Summary
LeetCode 344 - Reverse String

Problem:
Write a function that reverses a string. The input is given as an array of characters s.
You must modify the input array in-place with O(1) extra memory.
Do not return anything.
"""

# 2. Interviewer Critique of My Submitted Solution
"""
Your Submitted Solution:

def reverseString(self, s: List[str]) -> None:
    l = 0
    r = len(s) - 1
    
    while l < r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1
        
    return s

Logic & Accuracy:
- The two-pointer approach is correct.
- The swap logic is correct.
- The loop condition (l < r) is correct.
- However, the function incorrectly returns s.
  The problem explicitly requires in-place modification with NO return value.
  Returning s violates the specification (even though it may still pass locally).

Complexity Analysis:
Time Complexity: O(n)
- Each element is swapped at most once.
- The loop runs n/2 times.
- Therefore, time complexity is O(n).

Space Complexity: O(1)
- Only two pointers are used.
- No additional data structures are created.

Code Quality:
- Variable names 'l' and 'r' are acceptable but not ideal in interviews.
  Prefer 'left' and 'right' for clarity.
- Minor formatting issue: add space after comma (s[l], s[r]).
- Returning s contradicts the function signature (-> None).

Edge Cases:
- Empty list → handled correctly.
- Single element → loop never runs, correct behavior.
- Even length → works.
- Odd length → middle element untouched, correct.
- Very large input → efficient (O(n), O(1)).
"""

# 3. Corrected Version of My Solution (Brute Force Version)
"""
- Logic remains the same because it is already optimal.
- Removed the incorrect return statement.
- Improved variable names for readability.
- Added explanatory comments.
"""

from typing import List

def reverseString(s: List[str]) -> None:
    """
    Reverses the list of characters in-place.
    This corrected version fixes the return issue and improves readability.
    """
    left = 0
    right = len(s) - 1

    # Swap characters moving toward the center
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

    # No return statement (in-place modification)


"""
4. Time and Space Complexity of Corrected (Brute Force) Version

Time Complexity: O(n)
- The loop runs until pointers meet.
- Each iteration performs constant-time swap.
- Total operations proportional to n/2 → O(n).

Space Complexity: O(1)
- Only two integer variables used.
- No extra data structures allocated.
"""

# 5. Optimal Solution
"""
In this problem, the two-pointer solution is already optimal.

There is no faster-than-O(n) approach because every element must be touched at least once.
Space cannot be reduced below O(1) because in-place modification is required.

Below is a slightly more Pythonic but still interview-safe version.
"""

def reverseString_optimal(s: List[str]) -> None:
    """
    Optimal in-place two-pointer reversal.
    Clean, readable, interview-ready.
    """
    left, right = 0, len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


"""
6. Time and Space Complexity of Optimal Solution

Time Complexity: O(n)
- Each character is swapped once.
- Loop runs n/2 times.
- Therefore O(n).

Space Complexity: O(1)
- Only constant extra space for pointers.
"""

"""
7. Follow-up Interview Questions & Answers

Q1: What if the input were an immutable Python string instead of List[str]?
A1:
Strings in Python are immutable, so we cannot modify them in-place.
We would need to:
- Convert to a list → reverse → join back (O(n) space)
OR
- Use slicing: s[::-1] (also O(n) space).
Time complexity remains O(n), but space becomes O(n).

Q2: How would you reverse only vowels in the string?
A2:
Use a two-pointer approach.
Move left pointer until vowel found.
Move right pointer until vowel found.
Swap them.
Continue until pointers cross.
Time: O(n)
Space: O(1) if modifying list, O(n) if immutable string.

Q3: Can this be parallelized for very large data?
A3:
Yes conceptually.
Split the array into chunks and swap symmetric blocks.
However, synchronization is required to avoid race conditions.
In practice, overhead likely outweighs benefit unless extremely large data.
"""

"""
8. Edge Cases Checklist

- Empty input → []
- Single element → ["a"]
- Even length → ["a","b","c","d"]
- Odd length → ["a","b","c"]
- All identical characters → ["a","a","a"]
- Very large input (performance check)
"""

"""
9. Mistakes to Avoid

- Returning the list when problem specifies in-place modification only.
- Using extra space (e.g., creating another list unnecessarily).
- Incorrect loop condition (using <= instead of <).
- Off-by-one errors in pointer initialization.
- Forgetting to import List if using type hints outside LeetCode.
"""