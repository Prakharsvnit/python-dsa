"""
===========================================
1. LeetCode Link
===========================================
Valid Anagram
https://leetcode.com/problems/valid-anagram/


===========================================
2. DSA Pattern
===========================================
Hashing (Frequency Counting)


===========================================
3. Brute Force Solution
(Interview-friendly, realistic approach)
===========================================
"""

def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
        
    freq = {}
        
    for char_s in s:
        if char_s in freq:
            freq[char_s] += 1
        else:
            freq[char_s] = 1

    for char_t in t:
        if char_t not in freq:
            return False
        else:
            freq[char_t] -= 1

    for value in freq.values():
        if value != 0:
            return False
    return True    


def isAnagram_bruteforce(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    s_sorted = sorted(s)
    t_sorted = sorted(t)

    return s_sorted == t_sorted


"""
===========================================
4. Time and Space Complexity of Brute Force
===========================================

Time Complexity:

Step 1: Check length → O(1)

Step 2: Sort string s
- Sorting takes O(n log n)

Step 3: Sort string t
- Sorting takes O(n log n)

Step 4: Compare sorted lists
- Takes O(n)

Total:
O(n log n) + O(n log n) + O(n)
= O(n log n)

Sorting dominates.

Space Complexity:

- sorted() creates new lists of size n
- So extra space = O(n)
"""


"""
===========================================
5. Optimal Solution
(Using Hash Map / Frequency Counting)
===========================================
"""

def isAnagram_optimal(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    freq = {}

    # Count characters in s
    for char in s:
        freq[char] = freq.get(char, 0) + 1

    # Subtract using t
    for char in t:
        if char not in freq:
            return False

        freq[char] -= 1

        if freq[char] < 0:
            return False

    return True


"""
===========================================
6. Time and Space Complexity of Optimal
===========================================

Time Complexity:

Step 1: Length check → O(1)

Step 2: First loop over s
- Runs n times → O(n)

Step 3: Second loop over t
- Runs n times → O(n)

Total:
O(n) + O(n)
= O(n)

There are no nested loops.

Space Complexity:

Worst case:
- All characters are unique.
- Dictionary stores n entries.

So space = O(n)

If input is guaranteed lowercase English letters:
- Maximum 26 characters.
- Space = O(1)
"""


"""
===========================================
7. Follow-up Questions (With Answers)
===========================================

Q1: What if strings contain Unicode characters?
A: Dictionary approach works without modification.

Q2: What if input size is extremely large?
A: Use fixed-size array (26 for lowercase letters) to reduce overhead.

Q3: Can we solve in one pass?
A: Yes, increment for s and decrement for t in same loop.

Q4: What if case-insensitive?
A: Convert both strings to lower() before processing.

Q5: What if spaces or punctuation should be ignored?
A: Preprocess strings to remove unwanted characters.
"""


"""
===========================================
8. Edge Cases
===========================================

- s = "", t = "" → True
- s = "a", t = "a" → True
- Different lengths → False
- Repeated characters
- All identical characters
- Large input size
- Unicode input
"""


"""
===========================================
9. Mistakes to Avoid
===========================================

- Forgetting length check
- Returning inverted boolean logic
- Printing instead of returning
- Not checking negative frequency
- Saying space is O(1) without clarifying alphabet constraint
- Using unclear variable names
"""


# Optional: Local Testing
if __name__ == "__main__":
    test_cases = [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("aab", "aaa", False),
        ("", "", True),
        ("abc", "cba", True),
    ]

    for s, t, expected in test_cases:
        result = isAnagram_optimal(s, t)
        print(f"s={s}, t={t}, Output={result}, Expected={expected}")