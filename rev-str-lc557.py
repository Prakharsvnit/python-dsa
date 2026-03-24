```python
# ============================================================
# 1. LeetCode Link / Problem Description
# ============================================================

# Problem Link:
# https://leetcode.com/problems/reverse-words-in-a-string-iii/

"""
Problem Summary:

Given a string `s`, reverse the characters of each word in the sentence
while preserving whitespace and the original word order.

Example:
Input:  s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Rules:
- Words are separated by spaces.
- The order of words must remain the same.
- Only characters inside each word should be reversed.
"""

# ============================================================
# 2. DSA Pattern Identification
# ============================================================

"""
Core Pattern: Two Pointers + String Manipulation

Why this pattern applies:
- Each word needs to be reversed in-place.
- Reversal is efficiently done using two pointers:
  - One pointer at the beginning
  - One pointer at the end
- Swap characters and move inward until pointers meet.

Steps:
1. Split the string into words.
2. Reverse each word using two pointers.
3. Join the words back with spaces.

Alternative Patterns:
- Pythonic string slicing: word[::-1]
- Stack-based reversal (less efficient and unnecessary)
- Character array traversal without splitting
"""

# ============================================================
# 3. Interview Critique of My Solution
# ============================================================

"""
Logic & Accuracy:
- Your solution correctly reverses each word using two pointers.
- Splitting the string and processing word-by-word is valid.
- The algorithm produces correct results for standard cases.

Minor inefficiencies:
- Converting the word to a list (`word_list = list(word)`) inside the loop
  is necessary for mutability, but reversing with slicing could be simpler.
- Using `split(' ')` may behave differently than `split()` if there are
  multiple consecutive spaces (though the problem guarantees single spaces).

Complexity Analysis:

Let:
n = total characters in string

Step-by-step:
1. split() → O(n)
2. For each word, reverse using two pointers → total O(n)
3. join() → O(n)

Time Complexity: O(n)

Space Complexity:
- Storing split words → O(n)
- Character lists during reversal → O(n)

Total Space Complexity: O(n)

Code Quality:

Good:
- Clear variable names (`left`, `right`, `word_list`)
- Logical structure is easy to follow

Could be improved:
- Function name should follow snake_case: `rev_str`
- More descriptive function name (e.g., `reverse_words`)
- Could simplify using Pythonic constructs

Interview Acceptability:
- Acceptable solution.
- However, interviewers often expect a cleaner or more concise approach.

Edge Cases:
- Empty string
- Single word
- Single character
- Multiple spaces (not required per problem constraints)
"""

# ============================================================
# 4. My Original Solution (As Provided)
# ============================================================

def revStr(s):
    s_list = s.split(' ')
    
    for index, word in enumerate(s_list):
        left = 0
        right = len(word) - 1
        word_list = list(word)

        while left < right:
            word_list[left], word_list[right] = word_list[right], word_list[left]
            left += 1
            right -= 1

        s_list[index] = ''.join(word_list)

    return ' '.join(s_list)


# ============================================================
# 5. Brute Force Solution (Interview Friendly)
# ============================================================

"""
Idea:

1. Split the sentence into words.
2. Reverse each word using Python slicing.
3. Join them back together.

This is the most intuitive and readable approach.
"""

def reverse_words_bruteforce(s: str) -> str:
    words = s.split(" ")
    
    reversed_words = []
    
    for word in words:
        # Reverse the word using slicing
        reversed_words.append(word[::-1])
    
    return " ".join(reversed_words)


"""
Brute Force Complexity Analysis:

Time Complexity: O(n)

Explanation:
- Splitting string → O(n)
- Reversing each word → total O(n)
- Joining words → O(n)

Total: O(n)

Space Complexity: O(n)

Explanation:
- Storing words list → O(n)
- Storing reversed words → O(n)
"""

# ============================================================
# 6. Optimal Solution (Interview Accepted Version)
# ============================================================

"""
Optimized Idea:

Instead of splitting words, we can iterate through the string and
reverse characters directly when we encounter a space or the end.

This reduces extra list allocations and demonstrates stronger
string traversal skills.
"""

def reverse_words_optimal(s: str) -> str:
    chars = list(s)
    start = 0
    
    for i in range(len(chars) + 1):
        
        # When we hit space OR end of string
        if i == len(chars) or chars[i] == " ":
            
            left = start
            right = i - 1
            
            # Reverse characters within the word
            while left < right:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1
            
            # Move start to next word
            start = i + 1
    
    return "".join(chars)


"""
Optimal Complexity Analysis:

Time Complexity: O(n)

Reasoning:
- Each character is visited once.
- Each character participates in at most one swap.

Space Complexity: O(n)

Reasoning:
- We convert the string into a character list for in-place modification.
"""

# ============================================================
# 7. Follow-up Questions (Interview Level)
# ============================================================

"""
Q1: What if the input string is extremely large (millions of characters)?

A1:
Avoid multiple copies of the string.
Process the string in a streaming fashion or operate directly on
a mutable character array to minimize memory overhead.

Q2: How would you solve this WITHOUT using split()?

A2:
Traverse the string with two pointers.
When you encounter a space, reverse the characters between
the previous space and current index.

This is exactly what the optimal solution demonstrates.

Q3: How would you reverse the WORD ORDER instead of reversing
characters in each word?

Example:
Input:  "hello world"
Output: "world hello"

Solution:
- Split the words
- Reverse the list
- Join them back

Time Complexity: O(n)
"""

# ============================================================
# 8. Edge Cases Checklist
# ============================================================

"""
✔ Empty input
✔ Single element
✔ All duplicates
✔ Extreme constraints
✔ Single word
✔ Words with length = 1
✔ Maximum input size
"""

# ============================================================
# 9. Mistakes to Avoid
# ============================================================

"""
- Forgetting to rejoin words with spaces.
- Reversing the order of words instead of characters.
- Off-by-one errors when reversing.
- Creating unnecessary temporary lists.
- Not handling the last word when scanning the string.
"""

# ============================================================
# 10. Final Takeaways
# ============================================================

"""
What interviewers are really testing:

1. Ability to recognize the two-pointer reversal pattern.
2. Comfort with string manipulation.
3. Writing clean and readable code.

Pattern Recognition Insight:

Whenever you see:
- Reverse characters
- Palindrome checks
- Symmetric swapping

Think:
→ Two pointers moving inward.

Where this pattern appears again:

- Reverse String
- Valid Palindrome
- Reverse Linked List
- Container With Most Water
"""
```
