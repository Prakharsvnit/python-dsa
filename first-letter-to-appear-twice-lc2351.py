"""
1. LeetCode link
https://leetcode.com/problems/first-letter-to-appear-twice/

2. DSA Pattern
- Hashing
- Frequency Counting
- Set for fast lookup (O(1) membership check)

Problem:
Given a string s consisting of lowercase English letters,
return the first letter to appear twice.

------------------------------------------------------------
3. Brute Force Solution (code) - Dictionary frequency (mine)
------------------------------------------------------------
"""

def first_letter_bruteforce(s: str) -> str:
    count_dict = {}

    for char in s:
        if char in count_dict:
            count_dict[char] += 1
            if count_dict[char] == 2:
                return char
        else:
            count_dict[char] = 1

    return None


"""
------------------------------------------------------------
4. Time & Space (Brute) — explain
------------------------------------------------------------

Time Complexity:
O(n)
We iterate through the string once.
Dictionary operations (insert & lookup) are O(1) average.

Space Complexity:
O(26) ≈ O(1)
At most 26 lowercase letters stored in dictionary.
In general case: O(n)

------------------------------------------------------------
5. Optimal Solution (code) - set() waala
------------------------------------------------------------
"""

def first_letter_optimal(s: str) -> str:
    seen = set()

    for char in s:
        if char in seen:
            return char
        seen.add(char)

    return None


"""
------------------------------------------------------------
7. Time & Space (Optimal) — explain
------------------------------------------------------------

Time Complexity:
O(n)
Single pass through the string.
Set lookup is O(1) average.

Space Complexity:
O(26) ≈ O(1)
Set stores at most 26 lowercase letters.
General case: O(n)

Why this is better:
- No need to maintain counts.
- Stops immediately when duplicate is found.
- Cleaner and more intuitive.

------------------------------------------------------------
8. Followup or Modification Question
------------------------------------------------------------

1. What if we need the index of the first letter to appear twice?
2. What if we need the first non-repeating character?
3. What if the string contains Unicode characters?
4. What if we must return all characters that appear more than once?

------------------------------------------------------------
9. Edge Cases
------------------------------------------------------------

1. s has length 1 → return None
2. All characters unique → return None
3. First two characters same → return immediately
4. Very large string
5. Case sensitivity (if uppercase allowed)

------------------------------------------------------------
10. Mistake to Avoid
------------------------------------------------------------

1. Returning the character with highest frequency instead of
   the first one that appears twice.
2. Forgetting to return immediately when count becomes 2.
3. Using nested loops → O(n^2) unnecessarily.
4. Not handling empty string.
"""
