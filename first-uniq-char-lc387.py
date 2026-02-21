"""
1. LeetCode Link
First Unique Character in a String
https://leetcode.com/problems/first-unique-character-in-a-string/

2. DSA Pattern
- Hash Map (Frequency Counter)
- Two-pass traversal
- String traversal


3. Brute Force Solution (code only, interview-friendly and realistically solvable)
"""

def firstUniqChar_bruteforce(s: str) -> int:
    n = len(s)

    for i in range(n):
        is_unique = True

        for j in range(n):
            if i != j and s[i] == s[j]:
                is_unique = False
                break

        if is_unique:
            return i

    return -1


"""
4. Time and Space Complexity of Brute Force

Time Complexity: O(n^2)

Step-by-step explanation:
- Outer loop runs n times.
- For each character, inner loop runs up to n times.
- In worst case (no unique character), inner loop fully executes for every i.
- Total comparisons ≈ n * n.
- Therefore, time complexity is O(n^2).

Space Complexity: O(1)

- Only a few variables are used (i, j, is_unique).
- No extra data structure proportional to input size.
- Hence constant space.
"""


"""
5. Optimal Solution (code only, interview-friendly and realistically solvable)
"""

def firstUniqChar_optimal(s: str) -> int:
    freq = {}

    # First pass: build frequency map
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    # Second pass: find first unique character
    for i, ch in enumerate(s):
        if freq[ch] == 1:
            return i

    return -1


"""
6. Time and Space Complexity of Optimal

Time Complexity: O(n)

Step-by-step explanation:
- First loop traverses the string once → O(n).
- Second loop traverses the string once → O(n).
- Dictionary lookup is O(1) on average.
- Total time = O(n) + O(n) = O(n).

Space Complexity: O(n) worst case

Step-by-step explanation:
- In worst case, all characters are unique.
- Dictionary will store n entries.
- Therefore space complexity is O(n).
- If character set is fixed (like lowercase English letters), space can be considered O(1).


7. Follow-up Questions with Answers

Q1: What if the string is very large and character set is limited (e.g., lowercase letters)?
A: Use an array of size 26 instead of a dictionary to reduce overhead.

Q2: Can this be solved in one pass?
A: Not reliably, because we don't know if a character will repeat later. We need at least two passes unless we use additional structures like a queue.

Q3: What if we need to return the character instead of index?
A: Return ch instead of i in the second loop.

Q4: What if input is a stream of characters?
A: Maintain:
   - A frequency map
   - A queue of potential unique characters
   Remove characters from the queue when their frequency becomes > 1.


8. Edge Cases

- Empty string → return -1
- All characters repeating → return -1
- Single character string → return 0
- Case sensitivity matters ("a" != "A")
- Very large input


9. Mistakes to Avoid

- Using s.count(ch) inside a loop (makes it O(n^2))
- Using s.index() repeatedly (adds unnecessary extra scans)
- Forgetting to return -1 when no unique character exists
- Assuming dictionary order without explanation
- Not clarifying space complexity reasoning
"""