# ============================================================
# 1. LeetCode Link / Problem Description
# ============================================================

# Problem Link:
# https://leetcode.com/problems/is-subsequence/

"""
Problem Summary:

Given two strings s and t, return True if s is a subsequence of t,
otherwise return False.

A subsequence of a string is a new string formed from the original
string by deleting some (or no) characters without changing the
relative order of the remaining characters.

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: True

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: False

Constraints:
0 <= s.length <= 100
0 <= t.length <= 10^4
s and t consist only of lowercase English letters.

Follow-up:
If there are lots of incoming s queries (say billions), how would
you check them efficiently?
"""

# ============================================================
# 2. DSA Pattern Identification
# ============================================================

"""
Primary Pattern:
Two Pointers

Why this pattern applies:
- We are comparing characters from two sequences.
- We only move forward in both sequences.
- We never revisit earlier characters.

The key observation:
To check if s is a subsequence of t, we scan t once and
attempt to match characters from s in order.

This naturally maps to a two-pointer technique:
- One pointer iterates over s
- One pointer iterates over t

Alternative Patterns:
1. Greedy
   - Always match the earliest possible character.

2. Binary Search + Preprocessing
   - Used in the follow-up scenario when t is fixed and
     many s queries must be answered efficiently.

3. Dynamic Programming (NOT ideal)
   - Could treat this as a special case of LCS
   - But DP would be overkill for this problem.
"""

# ============================================================
# 3. Interview Critique of My Solution
# ============================================================

"""
Logic & Accuracy
----------------
Your solution uses Python's built-in string method `find()` to locate
each character of s inside t starting from a given index.

Key idea:
- Search for each character of s inside t.
- Ensure we search forward only using `t_ptr_start`.

Strengths:
- Correct logic.
- Maintains order constraint.
- Uses Python built-in efficiently.

Potential issues:
- Repeated `find()` calls internally scan portions of t repeatedly.
- Slightly less optimal than a pure two-pointer approach.

But logically it is correct.

Complexity Analysis
-------------------

Let:
m = len(s)
n = len(t)

Time Complexity:
O(m * n) in the worst case.

Reason:
Each call to t.find() can scan up to O(n) characters.

Worst case example:
s = "aaaaaa"
t = "bbbbbbbbbbbbbbbbbbbbba"

Each find() scans nearly the entire string.

Space Complexity:
O(1)

No additional data structures used.

Code Quality
------------

Positive:
- Clear pointer naming.
- Proper boundary conditions.
- Correct loop structure.

Possible Improvements:
- Slightly clearer variable naming.
- Explicit handling of empty s.

Overall Interview Acceptability:
Yes, this would be accepted in most interviews.

However, a senior interviewer would expect the
two-pointer O(n) solution.

Edge Cases
----------

Your solution handles:

✔ s empty
✔ t empty
✔ repeated characters
✔ subsequence at end of t
✔ subsequence at beginning of t

Edge cases implicitly handled by Python's find().

"""

# ============================================================
# 4. My Original Solution (As Provided)
# ============================================================

def isSubsequence(s, t):
    s_ptr = 0
    t_ptr_start = 0
    
    while s_ptr < len(s):
        t_ptr = t.find(s[s_ptr], t_ptr_start)
        
        if t_ptr != -1:
            s_ptr += 1
            t_ptr_start = t_ptr + 1
        else:
            return False
            
    return True


# ============================================================
# 5. Brute Force Solution (Interview Friendly)
# ============================================================

"""
Idea:

For every character in s:
- Scan t starting from the last matched index.
- Find a matching character manually.

This avoids using built-in `find()` and shows
clear reasoning in an interview.

Steps:
1. Maintain pointer for t.
2. For each character in s:
   search forward in t.
3. If found → move forward.
4. If not found → return False.
"""

def isSubsequence_bruteforce(s, t):
    t_index = 0

    for char in s:

        found = False

        while t_index < len(t):

            if t[t_index] == char:
                found = True
                t_index += 1
                break

            t_index += 1

        if not found:
            return False

    return True


"""
Brute Force Complexity Analysis:

Time Complexity: O(m * n)

Explanation:
Worst case:
- For each character in s
- We scan a large part of t

However, in practice it behaves closer to O(n).

Space Complexity: O(1)

Only pointer variables are used.
"""


# ============================================================
# 6. Optimal Solution (Interview Accepted Version)
# ============================================================

"""
Optimal Approach: Two Pointers

Idea:
Scan through t while matching characters in s.

Algorithm:
1. Maintain pointer i for s.
2. Maintain pointer j for t.
3. Move j every iteration.
4. If s[i] == t[j], move i.
5. If i reaches len(s), subsequence found.

Why optimal?
Each character in t is visited only once.

Key advantage:
Time complexity becomes O(n).
"""

def isSubsequence_optimal(s, t):

    s_index = 0
    t_index = 0

    while s_index < len(s) and t_index < len(t):

        if s[s_index] == t[t_index]:
            s_index += 1

        t_index += 1

    return s_index == len(s)


"""
Optimal Complexity Analysis:

Time Complexity: O(n)

Explanation:
- Each character of t is visited once.
- Pointer movements are linear.

Space Complexity: O(1)

Only two integer pointers used.
"""


# ============================================================
# 7. Follow-up Questions (Interview Level)
# ============================================================

"""
Q1: Suppose t is fixed but there are billions of s queries.
How would you optimize?

A1:

Preprocess t.

Create a dictionary mapping:
character -> sorted list of indices where it appears.

Example:
t = "ahbgdc"

{
'a': [0],
'h': [1],
'b': [2],
'g': [3],
'd': [4],
'c': [5]
}

For each character in s:
- Use binary search to find the next valid index.

This reduces query time to:

O(len(s) * log n)

Preprocessing cost:
O(n)


Q2: How would you check if s is a subsequence of multiple strings?

A2:

If multiple t strings exist:
- Build the above preprocessing for each t.

Or use:
Trie / suffix automaton / indexing structures
depending on scale.


Q3: System Design Twist

Suppose:
- t is extremely large (GBs)
- many s queries arrive continuously.

Approach:

1. Preprocess t into index lists.
2. Store in memory-efficient structures.
3. Use binary search for each query.
4. Potentially shard by character range.

This allows millions of subsequence queries per second.
"""


# ============================================================
# 8. Edge Cases Checklist
# ============================================================

"""
Always verify:

✔ s = ""
✔ t = ""
✔ s longer than t
✔ repeated characters
✔ s equals t
✔ characters appear but in wrong order
✔ subsequence occurs at end
✔ subsequence occurs at beginning
"""


# ============================================================
# 9. Mistakes to Avoid
# ============================================================

"""
Common traps:

1. Resetting t pointer incorrectly.

2. Allowing backward matches.

3. Using nested loops unnecessarily.

4. Off-by-one errors with indices.

5. Forgetting empty string edge cases.

6. Overengineering with dynamic programming.
"""


# ============================================================
# 10. Final Takeaways
# ============================================================

"""
What interviewers are testing:

1. Pattern recognition
   - Identify the two-pointer pattern quickly.

2. Greedy thinking
   - Match earliest valid character.

3. Efficiency awareness
   - Avoid unnecessary scanning.

4. Follow-up scalability
   - Handle billions of queries.

Key Insight:

Subsequence problems almost always reduce to:
"scan the larger sequence once while matching the smaller one."

Recognizing this pattern quickly is a strong signal
of algorithmic maturity.
"""


# ============================================================
# Simple Test Harness
# ============================================================

if __name__ == "__main__":

    tests = [
        ("abc", "ahbgdc"),
        ("axc", "ahbgdc"),
        ("", "ahbgdc"),
        ("abc", ""),
        ("aaaa", "aaabaa")
    ]

    print("Testing Original Solution")
    for s, t in tests:
        print(s, t, "->", isSubsequence(s, t))

    print("\nTesting Brute Force")
    for s, t in tests:
        print(s, t, "->", isSubsequence_bruteforce(s, t))

    print("\nTesting Optimal Solution")
    for s, t in tests:
        print(s, t, "->", isSubsequence_optimal(s, t))