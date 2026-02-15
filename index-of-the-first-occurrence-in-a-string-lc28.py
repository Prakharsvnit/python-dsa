"""
===========================================================
Problem: Find the Index of the First Occurrence in a String
(LeetCode 28)
===========================================================

1. LeetCode Link:
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

-----------------------------------------------------------
2. DSA Pattern:
- String Matching
- Sliding Window (naive comparison)
- KMP (Knuth-Morris-Pratt) for optimal solution

Core Idea:
We try to match the pattern (needle) inside the text (haystack).
Brute force compares every possible starting position.
Optimal approach avoids rechecking characters using prefix info.

-----------------------------------------------------------
3. Brute Force Solution (Code)
-----------------------------------------------------------
"""
# haystack.find(needle) or haystack.index(needle)

def strStr_brute(haystack, needle):
    if needle == "":
        return 0

    n = len(haystack)
    m = len(needle)

    if m > n:
        return -1

    for i in range(n - m + 1):
        if haystack[i:i+m] == needle:
            return i

    return -1

## The Hidden Cost: String Slicing and Comparison

The **critical line** is:
```python
if haystack[i:i+m] == needle:
```

This looks like O(1), but it's **NOT**! Here's what happens:

### Step 1: String Slicing `haystack[i:i+m]`
- Creates a **new substring** of length `m`
- **Time: O(m)** - Must copy `m` characters
- **Space: O(m)** - Allocates memory for new string

### Step 2: String Comparison `substring == needle`
- Compares two strings of length `m` character by character
- **Time: O(m)** - Must compare up to `m` characters
- In Python, this is optimized but still O(m) in worst case

### Combined: O(m) + O(m) = O(m) per iteration

## Full Time Complexity Calculation

```
Total Time = (Number of iterations) × (Cost per iteration)
           = (n - m + 1) × O(m)
           = O((n - m) × m)
           = O(n × m)  when m << n
```
## Visual Example

Let's trace through: `haystack = "abcdefg"` (n=7), `needle = "def"` (m=3)

```
Iteration 0: i=0
  haystack[0:3] = "abc"  ← Create substring (O(3))
  "abc" == "def"         ← Compare (O(3))
  Total: O(3)

Iteration 1: i=1
  haystack[1:4] = "bcd"  ← Create substring (O(3))
  "bcd" == "def"         ← Compare (O(3))
  Total: O(3)

Iteration 2: i=2
  haystack[2:5] = "cde"  ← Create substring (O(3))
  "cde" == "def"         ← Compare (O(3))
  Total: O(3)

Iteration 3: i=3
  haystack[3:6] = "def"  ← Create substring (O(3))
  "def" == "def"         ← Compare (O(3)), MATCH!
  Total: O(3)

Total iterations: 5 (which is n - m + 1 = 7 - 3 + 1 = 5)
Total time: 5 × O(3) = O(15) = O(n × m)

**Your function is O(n × m) because:**

1. **Outer loop**: Runs `n - m + 1` times ≈ **O(n)**
2. **Slicing `[i:i+m]`**: Creates substring ≈ **O(m)**
3. **Comparison `== needle`**: Compares m characters ≈ **O(m)**
4. **Per iteration**: O(m) + O(m) = **O(m)**
5. **Total**: O(n) × O(m) = **O(n × m)**
"""
-----------------------------------------------------------
4. Time & Space (Brute) — Why?
-----------------------------------------------------------

Time Complexity: O(n * m)
- Outer loop runs up to n - m + 1 times
- Substring comparison takes O(m)

Space Complexity: O(1)
- No extra data structures used

-----------------------------------------------------------
Logical / Performance Issues
-----------------------------------------------------------

❌ Repeated comparisons of characters
❌ Worst case becomes slow for large strings
   Example:
   haystack = "aaaaaaaab"
   needle   = "aaab"
❌ Substring slicing creates new string each time (O(m))

-----------------------------------------------------------
5. Optimal Solution (Code) — KMP Algorithm
-----------------------------------------------------------
"""

def strStr_optimal(haystack, needle):
    if not needle:
        return 0

    # Step 1: Build LPS (Longest Prefix Suffix) array
    lps = [0] * len(needle)
    prev = 0
    i = 1

    while i < len(needle):
        if needle[i] == needle[prev]:
            prev += 1
            lps[i] = prev
            i += 1
        else:
            if prev != 0:
                prev = lps[prev - 1]
            else:
                lps[i] = 0
                i += 1

    # Step 2: Search using LPS
    i = j = 0
    while i < len(haystack):
        if haystack[i] == needle[j]:
            i += 1
            j += 1

            if j == len(needle):
                return i - j
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return -1


"""
-----------------------------------------------------------
7. Time & Space (Optimal) — Why?
-----------------------------------------------------------

Time Complexity: O(n + m)
- Build LPS array: O(m)
- Single pass search: O(n)

No character is reprocessed unnecessarily.

Space Complexity: O(m)
- LPS array of size m

Tradeoff:
We use extra memory to eliminate repeated comparisons.

-----------------------------------------------------------
8. Follow-Up Questions (Interview Style)
-----------------------------------------------------------

1) Why does KMP avoid rechecking characters?
   → Uses prefix information (LPS array) to skip shifts.

2) What is LPS array?
   → Longest Proper Prefix which is also Suffix.

3) Can this be done using rolling hash?
   → Yes, Rabin-Karp algorithm.

4) What if strings are extremely large?
   → Use KMP or Boyer-Moore.

5) What if we need all occurrences instead of first?
   → Continue searching after match instead of returning.

-----------------------------------------------------------
9. Edge Cases
-----------------------------------------------------------

- needle = ""
- haystack = ""
- needle longer than haystack
- Repeated characters
- Full match (needle == haystack)
- No match case

-----------------------------------------------------------
10. Mistakes to Avoid
-----------------------------------------------------------

❌ Looping until len(haystack) instead of len(haystack) - len(needle) + 1
❌ Ignoring empty needle case
❌ Recomputing prefix matches repeatedly
❌ Not understanding LPS logic
❌ Confusing substring matching with subsequence

Interview Flow:
1) Explain brute force
2) Analyze O(n*m)
3) Improve using KMP
4) Explain LPS clearly

===========================================================
End of Revision File
===========================================================
"""
