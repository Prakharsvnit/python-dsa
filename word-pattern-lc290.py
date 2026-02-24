"""
================================================================================
1. LEETCODE LINK
================================================================================
https://leetcode.com/problems/word-pattern/
Problem 290: Word Pattern

Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match, such that there is a bijection between 
a letter in pattern and a non-empty word in s.

Example 1: pattern = "abba", s = "dog cat cat dog" → True
Example 2: pattern = "abba", s = "dog cat cat fish" → False
Example 3: pattern = "aaaa", s = "dog cat cat dog" → False

================================================================================
2. DSA PATTERN
================================================================================
- Hash Map (Dictionary) for Mapping/Bijection
- Two-way Mapping (Pattern Matching)
- String Processing

================================================================================
3. PYTHON METHODS USED
================================================================================
- str.split(): Split string into list of words
- dict: Hash map for O(1) lookup and storage
- enumerate(): Get index and value simultaneously
- len(): Get length of string/list
- zip(): Iterate over two sequences in parallel

================================================================================
4. WHAT INTERVIEWERS EXPECT
================================================================================
- Understanding of bijection (one-to-one AND onto mapping)
- Ability to handle TWO-WAY mapping (pattern→word AND word→pattern)
- Clean edge case handling
- Clear explanation of why single mapping is insufficient
- Time/Space complexity analysis

================================================================================
5. BRUTE FORCE SOLUTION
================================================================================
"""


def word_pattern_brute_force(pattern: str, s: str) -> bool:
    s_list = s.split(" ")
    
    if len(pattern) != len(s_list):
        return False
    
    word_dict = {}
    s_dict = {}
    
    for i, v in enumerate(pattern):
        if v in word_dict and word_dict[v] != s_list[i]:
            return False
        else:
            word_dict[v] = s_list[i]
            
    for i, v in enumerate(s_list):
        if v in s_dict and s_dict[v] != pattern[i]:
            return False
        else:
            s_dict[v] = pattern[i]
    
    return True


"""
================================================================================
6. TIME AND SPACE COMPLEXITY OF BRUTE FORCE
================================================================================

TIME COMPLEXITY: O(n + m)
Step-by-step breakdown:
1. s.split(" ") → O(m) where m is length of string s
   - Must traverse entire string to find spaces
2. len(pattern) → O(1)
3. len(words) → O(1)
4. First loop iterates n times (n = length of pattern)
   - Each dict lookup/insert → O(1) average
   - Total: O(n)
5. Second loop iterates n times
   - Each dict lookup/insert → O(1) average
   - Total: O(n)
6. Overall: O(m) + O(n) + O(n) = O(n + m)

Since n (pattern length) typically equals number of words:
→ Simplified: O(n + m) or O(m) where m is string length

SPACE COMPLEXITY: O(n + w)
Step-by-step breakdown:
1. words list → O(n) where n is number of words
2. pattern_to_word dict → O(k) where k is unique chars in pattern (max 26)
3. word_to_pattern dict → O(w) where w is unique words
4. Overall: O(n + k + w)
   - Since k ≤ 26 (constant), simplifies to O(n + w)

================================================================================
7. OPTIMAL SOLUTION
================================================================================
"""


def word_pattern_optimal(pattern: str, s: str) -> bool:
    """
    Optimal: Single pass with simultaneous two-way mapping validation.
    Uses zip() to iterate pattern and words together.
    """
    words = s.split(" ")
    
    # Edge case: lengths must match for valid bijection
    if len(pattern) != len(words):
        return False
    
    # Two dictionaries for bidirectional mapping
    char_to_word = {}
    word_to_char = {}
    
    # Single pass: validate both mappings simultaneously
    for char, word in zip(pattern, words):
        # Check pattern → word mapping
        if char in char_to_word:
            if char_to_word[char] != word:
                return False
        else:
            char_to_word[char] = word
        
        # Check word → pattern mapping
        if word in word_to_char:
            if word_to_char[word] != char:
                return False
        else:
            word_to_char[word] = char
    
    return True


# Alternative: Even more concise using set comparison
def word_pattern_optimal_v2(pattern: str, s: str) -> bool:
    """
    Alternative optimal solution using zip properties.
    Checks if the number of unique mappings equals unique chars and unique words.
    """
    words = s.split(" ")
    
    if len(pattern) != len(words):
        return False
    
    # Create pairs and check bijection property
    # For bijection: unique pairs == unique chars == unique words
    pairs = list(zip(pattern, words))
    
    return len(set(pairs)) == len(set(pattern)) == len(set(words))


"""
================================================================================
8. TIME AND SPACE COMPLEXITY OF OPTIMAL
================================================================================

TIME COMPLEXITY: O(n + m)
Step-by-step breakdown:
1. s.split(" ") → O(m) where m is length of string s
2. len(pattern), len(words) → O(1) each
3. zip(pattern, words) → O(1) creates iterator
4. Single loop iterates n times (n = pattern length)
   - Dictionary lookup: O(1) average
   - Dictionary insert: O(1) average
   - Two lookups + potential inserts per iteration: O(1)
   - Total loop: O(n)
5. Overall: O(m) + O(n) = O(n + m)

For V2 (set-based):
1. s.split(" ") → O(m)
2. zip + list → O(n)
3. set(pairs) → O(n)
4. set(pattern) → O(n)
5. set(words) → O(n)
6. Overall: O(n + m)

SPACE COMPLEXITY: O(n + w)
Step-by-step breakdown:
1. words list → O(n) to store n words
2. char_to_word dict → O(min(n, 26)) = O(1) since max 26 unique chars
3. word_to_char dict → O(w) where w is unique words
4. Overall: O(n + w)

For V2: O(n) for pairs list + O(n) for sets = O(n)

================================================================================
9. FOLLOW-UP QUESTIONS WITH ANSWERS
================================================================================

Q1: Why do we need TWO dictionaries? Can't we use just one?
A1: No! Single mapping fails for cases like:
    pattern = "abba", s = "dog dog dog dog"
    - pattern→word: a→dog, b→dog (no conflict detected!)
    - But this is WRONG because both 'a' and 'b' map to same word
    - We need word→pattern to catch: dog→a, then dog→b (CONFLICT!)
    This is the BIJECTION requirement: one-to-one AND onto.

Q2: What if words can contain spaces?
A2: The current split(" ") would break. Options:
    - Use a different delimiter
    - Pass words as a list instead of string
    - Use regex with specific word boundaries

Q3: What if pattern can have duplicate characters but different cases (A vs a)?
A3: Current solution treats them as different. If case-insensitive needed:
    pattern = pattern.lower()

Q4: How would you handle this for very large inputs (streaming)?
A4: Current solution requires O(n) space for words list.
    For streaming, process one word at a time from input stream.

Q5: What's the difference between this and Isomorphic Strings (LC 205)?
A5: Very similar! Both require bijection.
    - Word Pattern: pattern chars ↔ words
    - Isomorphic Strings: chars ↔ chars

================================================================================
10. EDGE CASES HANDLING
================================================================================
"""


def word_pattern_with_edge_cases(pattern: str, s: str) -> bool:
    """
    Comprehensive solution with explicit edge case handling.
    """
    # Edge Case 1: Empty pattern
    if not pattern:
        return s == ""  # Empty pattern matches only empty string
    
    # Edge Case 2: Empty string
    if not s:
        return pattern == ""  # Empty string matches only empty pattern
    
    words = s.split(" ")
    
    # Edge Case 3: Length mismatch
    # e.g., pattern = "ab", s = "dog" (1 word, 2 chars)
    if len(pattern) != len(words):
        return False
    
    # Edge Case 4: Single character/word
    # e.g., pattern = "a", s = "dog" → True
    
    # Edge Case 5: All same vs all different
    # pattern = "aaaa", s = "dog dog dog dog" → True
    # pattern = "abcd", s = "dog cat fish bird" → True
    # pattern = "aaaa", s = "dog cat cat dog" → False
    
    char_to_word = {}
    word_to_char = {}
    
    for char, word in zip(pattern, words):
        # Edge Case 6: Same char maps to different words
        if char in char_to_word:
            if char_to_word[char] != word:
                return False
        else:
            char_to_word[char] = word
        
        # Edge Case 7: Different chars map to same word
        if word in word_to_char:
            if word_to_char[word] != char:
                return False
        else:
            word_to_char[word] = char
    
    return True


"""
================================================================================
11. MISTAKES TO AVOID
================================================================================

MISTAKE 1: Using only ONE dictionary (most common!)
❌ WRONG:
    word_dict = {}
    for i, v in enumerate(pattern):
        if v in word_dict and word_dict[v] != s_list[i]:
            return False
        word_dict[v] = s_list[i]
    return True

This fails for: pattern = "abba", s = "dog dog dog dog"
- a→dog ✓, b→dog ✓, b→dog ✓, a→dog ✓
- Returns True but should return False!

✓ CORRECT: Use TWO dictionaries for bijection.

---

MISTAKE 2: Bug in original code - using s[i] instead of s_list[i]
❌ WRONG:
    word_dict[v] = s[i]  # s[i] is a character, not a word!

✓ CORRECT:
    word_dict[v] = s_list[i]  # Use the word from split list

---

MISTAKE 3: Forgetting length check
❌ WRONG: Skipping length validation
    - pattern = "ab", s = "dog" would cause index errors or wrong results

✓ CORRECT: Always check len(pattern) == len(words) first

---

MISTAKE 4: Not handling empty inputs
❌ WRONG: Assuming non-empty inputs

✓ CORRECT: Handle pattern = "" or s = "" explicitly

---

MISTAKE 5: Splitting on wrong delimiter
❌ WRONG: s.split()  # splits on any whitespace, handles multiple spaces
   This might be correct or wrong depending on problem constraints.

✓ CORRECT: s.split(" ")  # splits on single space as per problem

---

MISTAKE 6: Modifying dictionary during iteration
❌ WRONG: Complex logic that modifies while reading

✓ CORRECT: Simple read-then-write pattern

================================================================================
12. TEST CASES
================================================================================
"""


def run_tests():
    test_cases = [
        # (pattern, s, expected)
        ("abba", "dog cat cat dog", True),      # Basic bijection
        ("abba", "dog cat cat fish", False),    # Same pattern, different words
        ("aaaa", "dog cat cat dog", False),     # Different chars, same words
        ("abba", "dog dog dog dog", False),     # Different chars map to same word
        ("abc", "dog cat fish", True),          # All different
        ("aaa", "dog dog dog", True),           # All same
        ("a", "dog", True),                     # Single element
        ("ab", "dog", False),                   # Length mismatch
        ("", "", True),                         # Empty inputs
        ("jquery", "jquery", False),            # Each char maps to single word
    ]
    
    print("Running tests...\n")
    
    for pattern, s, expected in test_cases:
        result_brute = word_pattern_brute_force(pattern, s)
        result_optimal = word_pattern_optimal(pattern, s)
        result_v2 = word_pattern_optimal_v2(pattern, s)
        
        status = "✓" if result_optimal == expected else "✗"
        print(f"{status} pattern='{pattern}', s='{s}'")
        print(f"  Expected: {expected}, Got: {result_optimal}")
        
        if result_brute != result_optimal or result_optimal != result_v2:
            print(f"  WARNING: Solutions disagree!")
        print()


if __name__ == "__main__":
    run_tests()