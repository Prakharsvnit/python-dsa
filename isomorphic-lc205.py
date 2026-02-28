"""
========================================
1. LeetCode Link
========================================
https://leetcode.com/problems/isomorphic-strings/

========================================
2. DSA Pattern
========================================
Hash Map / Bijective Mapping
(Ensuring one-to-one character correspondence)

----------------------------------------
Key Concept:
Isomorphic strings require a BIJECTION.
That means:
- One character in s maps to exactly one character in t
- No two characters in s map to the same character in t
========================================
"""


# ========================================
# 3. Brute Force Solution
# ========================================
# Approach:
# Compare first occurrence pattern of both strings.
# If pattern matches, strings are isomorphic.

def is_isomorphic_bruteforce(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    for i in range(len(s)):
        # If first occurrence positions are different,
        # pattern differs → not isomorphic
        if s.index(s[i]) != t.index(t[i]):
            return False

    return True


"""
========================================
4. Time & Space Complexity (Brute Force)
========================================

Time Complexity: O(n^2)

Step-by-step justification:

Let n = length of string.

1. We iterate over string once → O(n)
2. For each character, we call:
       s.index(s[i])  → O(n)
       t.index(t[i])  → O(n)

Each index() scan is O(n).

So inside loop:
    O(n) work per iteration

Total:
    n * O(n) = O(n^2)

Space Complexity: O(1)

Why?
- No extra data structures used
- index() does not allocate additional memory
- Only a few variables

----------------------------------------
Interview note:
This solution is acceptable for small constraints,
but not scalable for very large inputs.
========================================
"""


# ========================================
# 5. Optimal Solution
# ========================================
# Approach:
# Use two hash maps to enforce bijection:
# s → t
# t → s

def is_isomorphic_optimal(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    s_to_t = {}
    t_to_s = {}

    for char_s, char_t in zip(s, t):

        # Forward mapping check
        if char_s in s_to_t and s_to_t[char_s] != char_t:
            return False

        # Reverse mapping check
        if char_t in t_to_s and t_to_s[char_t] != char_s:
            return False

        s_to_t[char_s] = char_t
        t_to_s[char_t] = char_s

    return True


"""
========================================
6. Time & Space Complexity (Optimal)
========================================

Time Complexity: O(n)

Step-by-step justification:

Let n = length of string.

1. Length check → O(1)
2. Single pass through both strings → O(n)
3. Dictionary lookup → O(1) average
4. Dictionary insert → O(1) average

Total:
    O(n)

Space Complexity: O(n)

Why?

Worst case:
All characters are unique.

Example:
    s = "abcdef"
    t = "uvwxyz"

We store n mappings in:
    s_to_t
    t_to_s

Total extra storage:
    O(n)

----------------------------------------
Interview justification:
We must inspect every character at least once,
so O(n) time is optimal.
========================================
"""


"""
========================================
7. Follow-up Questions (With Answers)
========================================

Q1: Why do we need two hash maps?
A:
Because isomorphic requires BIJECTION.
One map ensures:
    s → t consistency
Second map ensures:
    No two characters in s map to same character in t.

Without reverse map:
    s="ab", t="aa"
would incorrectly return True.


Q2: Can this be done with one hash map?
A:
Not safely. You also need to track used characters
(e.g., via a set), which is equivalent to reverse map.


Q3: Can this be done without extra space?
A:
Yes, using index pattern comparison:

    [s.index(c) for c in s] ==
    [t.index(c) for c in t]

But that is O(n^2) time.


Q4: What if strings are extremely large (10^7)?
A:
Use the O(n) hash map solution.
Avoid index() based approach.


Q5: What if input comes as a stream?
A:
Process character-by-character,
maintain two maps,
exit early if mismatch found.


Q6: Can this be extended to arrays of integers?
A:
Yes. Replace characters with integers.
Same logic applies.


Q7: What type of mapping is required?
A:
Bijective mapping (one-to-one and onto).
========================================
"""


"""
========================================
8. Edge Cases
========================================

1. Empty strings:
   s = "", t = "" → True

2. Different lengths:
   s = "a", t = "" → False

3. Same character repeated:
   s = "aaa", t = "bbb" → True

4. One-to-many mapping attempt:
   s = "ab", t = "aa" → False

5. Unicode characters:
   s = "纸纸", t = "aa" → True
   (Python dict handles Unicode safely)

6. Case sensitivity:
   "a" != "A"
   Function is case-sensitive by default.
========================================
"""


"""
========================================
9. Mistakes to Avoid
========================================

1. ❌ Not checking length first
   zip() silently truncates.

2. ❌ Using only one dictionary
   Fails bijection requirement.

3. ❌ Forgetting reverse check
   Leads to incorrect True cases.

4. ❌ Using index() in optimal solution
   Causes O(n^2).

5. ❌ Overcomplicating solution
   No need for fancy tricks.

6. ❌ Poor variable names
   Use meaningful names:
       s_to_t
       t_to_s
       char_s
       char_t

7. ❌ Not explaining complexity clearly in interview
   Always justify:
       - Why O(n)
       - Why O(n^2)
       - Why space is O(n)

========================================
End of File
========================================
"""