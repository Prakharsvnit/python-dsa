"""
===========================================================
Problem: Concatenation of Array
(LeetCode 1929)
===========================================================

1. LeetCode Link:
https://leetcode.com/problems/concatenation-of-array/

-----------------------------------------------------------
2. DSA Pattern:
- Basic Array Manipulation
- Array Construction
- Index Mapping

Core Idea:
Create a new array 'ans' of size 2n such that:
ans[i] = nums[i]
ans[i + n] = nums[i]

-----------------------------------------------------------
3. Brute Force Solution (Code)
-----------------------------------------------------------
"""

def getConcatenation_brute(nums):
    ans = []

    # Append elements twice manually
    for num in nums:
        ans.append(num)

    for num in nums:
        ans.append(num)

    return ans


"""
-----------------------------------------------------------
4. Time & Space (Brute) — Why?
-----------------------------------------------------------

Time Complexity: O(n)
- Two loops over n elements → 2n → O(n)

Space Complexity: O(n)
- New array of size 2n created

-----------------------------------------------------------
5. Optimal Solution (Code)
-----------------------------------------------------------
"""

def getConcatenation_optimal(nums):
    return nums + nums

def getConcatenation(nums):
    n = len(nums)
    ans = [0] * (2 * n)  #-->Important

    for i in range(n):
        ans[i] = nums[i]
        ans[i + n] = nums[i]

    return ans

"""
-----------------------------------------------------------
7. Time & Space (Optimal) — Why?
-----------------------------------------------------------

Time Complexity: O(n)
- List concatenation copies elements once

Space Complexity: O(n)
- New list of size 2n created

Note:
Even though code is shorter, complexity remains O(n).

-----------------------------------------------------------
8. Follow-up Questions
-----------------------------------------------------------

1) Can we do this without creating new array?
   → Only if modifying input allowed:
     nums *= 2

2) What if memory is constrained?
   → Cannot avoid O(n) space since output size is 2n.

3) What if nums is extremely large?
   → Memory usage doubles.

-----------------------------------------------------------
9. Edge Cases
-----------------------------------------------------------

- Empty array []
- Single element [1]
- Negative numbers
- Large arrays

-----------------------------------------------------------
10. Mistakes to Avoid
-----------------------------------------------------------

❌ Modifying input when not allowed
❌ Assuming concatenation is O(1)
❌ Forgetting that output size is 2n

Interview Strategy:
For easy problems:
- Write clean solution
- Explain complexity
- Mention constraints
- Show understanding of memory

===========================================================
End of Revision File
===========================================================
"""
