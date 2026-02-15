"""
===========================================================
Problem: Contains Duplicate
===========================================================

1. LeetCode Link:
https://leetcode.com/problems/contains-duplicate/

-----------------------------------------------------------
2. DSA Pattern:
- Hashing (Set)
- Early Exit Pattern
- Duplicate Detection via Hash Structure

Core Idea:
If number of unique elements < total elements,
then duplicates exist.

Better approach:
Scan once and stop immediately when duplicate found.

-----------------------------------------------------------
3. Brute Force Solution (Code)
-----------------------------------------------------------
"""

def contains_duplicate_brute(nums):
    n = len(nums)
    
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                return True
    
    return False


"""
-----------------------------------------------------------
4. Time & Space (Brute) — Why?
-----------------------------------------------------------

Time Complexity: O(n²)
- Two nested loops
- For each element, compare with remaining elements

Space Complexity: O(1)
- No extra data structures used

This approach will fail for large inputs.

-----------------------------------------------------------
5. Optimal Solution (Code)
-----------------------------------------------------------
"""

def contains_duplicate_optimal(nums):
    seen = set()
    
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    
    return False


"""
-----------------------------------------------------------
7. Time & Space (Optimal) — Why?
-----------------------------------------------------------

Time Complexity: O(n)
- Single pass through array
- Set lookup is O(1) average time

Space Complexity: O(n)
- In worst case, all elements stored in set

Tradeoff:
We reduce time complexity by using extra memory.

-----------------------------------------------------------
8. Follow-up Questions
-----------------------------------------------------------

1) What if memory is constrained?
   → Sort array first (O(n log n)), then check adjacent elements.

2) What if numbers are in limited range?
   → Use boolean array instead of set.

3) What if input is streaming data?
   → Maintain persistent set across insertions.

4) What if we must return the duplicate values?
   → Store duplicates separately and return list.

-----------------------------------------------------------
9. Edge Cases
-----------------------------------------------------------

- Empty array []
- Single element [1]
- All elements same [2,2,2,2]
- Negative numbers
- Very large input size

-----------------------------------------------------------
10. Mistakes to Avoid
-----------------------------------------------------------

❌ Using O(n²) solution in large constraints
❌ Forgetting early exit
❌ Confusing set size with list size incorrectly
❌ Not considering memory tradeoffs
❌ Sorting without checking if in-place modification allowed

Strong Interview Flow:
1) Mention brute force
2) Improve using set
3) Discuss constraints
4) Explain tradeoffs

===========================================================
End of Revision File
===========================================================
"""
