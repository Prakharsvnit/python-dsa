"""
===========================================================
Problem: Two Sum
===========================================================

1. LeetCode Link:
https://leetcode.com/problems/two-sum/

-----------------------------------------------------------
2. DSA Pattern:
- Hashing (Dictionary)
- Complement Lookup Pattern
- One-pass hash map

Core Idea:
Instead of checking every pair (O(n²)),
store visited numbers and check if complement exists.

-----------------------------------------------------------
3. Brute Force Solution (Code)
-----------------------------------------------------------
"""

def two_sum_brute(nums, target):
    n = len(nums)
    
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    
    return None


"""
-----------------------------------------------------------
4. Time & Space (Brute) — Why?
-----------------------------------------------------------

Time Complexity: O(n²)
- Two nested loops
- For each element, we scan remaining elements

Space Complexity: O(1)
- No extra data structures used

-----------------------------------------------------------
5. Optimal Solution (Code)
-----------------------------------------------------------
"""

def two_sum_optimal(nums, target):
    seen = {}  # value -> index
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in seen:
            return [seen[complement], i]
        
        seen[num] = i
    
    return None


"""
-----------------------------------------------------------
7. Time & Space (Optimal) — Why?
-----------------------------------------------------------

Time Complexity: O(n)
- Single loop over array
- Dictionary lookup is O(1) average

Space Complexity: O(n)
- In worst case, store all elements in dictionary

Tradeoff:
We reduce time from O(n²) → O(n)
by using extra space.

-----------------------------------------------------------
8. Follow-up Questions
-----------------------------------------------------------

1) What if array is sorted?
   → Use Two Pointers (O(n), O(1) space)

2) What if multiple pairs exist?
   → Return all pairs (modify logic)

3) What if numbers arrive as a stream?
   → Maintain dictionary across inserts

4) What if memory is limited?
   → Trade space for time (back to brute force)

-----------------------------------------------------------
9. Edge Cases
-----------------------------------------------------------

- nums = [3,3], target = 6
- Negative numbers
- Large numbers
- No solution (if not guaranteed)
- Very small array (size < 2)

-----------------------------------------------------------
10. Mistakes to Avoid
-----------------------------------------------------------

❌ Off-by-one errors in loops
❌ Using len(nums) - 1 incorrectly
❌ Overwriting dictionary before checking complement
❌ Forgetting that indices must be different
❌ Not handling duplicate numbers properly

Correct Order:
1) Check complement
2) Then store current number

===========================================================
End of Revision File
===========================================================
"""
