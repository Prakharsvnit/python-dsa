# ============================================================
# 1. LeetCode Link / Problem Description
# ============================================================

# Problem: 350. Intersection of Two Arrays II
# Link: https://leetcode.com/problems/intersection-of-two-arrays-ii/
#
# Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result must appear as many times as it shows in both arrays.
# You may return the result in any order.
#
# Example:
# nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]

# ============================================================
# 2. DSA Pattern Identification
# ============================================================

"""
Core Pattern: Hash Map (Frequency Counting)

Why it applies:
- We need to count occurrences of elements.
- Intersection requires respecting duplicate counts.
- Hash map allows O(1) lookup and update.

Alternative Patterns:
- Two Pointers (after sorting both arrays)
- Binary Search (if one array is sorted)
"""


# ============================================================
# 5. Brute Force Solution (Interview Friendly)
# ============================================================

"""
Idea:
- Iterate through nums1
- For each element, check if it exists in nums2
- If yes:
    - Add to result
    - Remove it from nums2 (to handle duplicates correctly)
"""

def intersect_bruteforce(nums1, nums2):
    result = []
    nums2_copy = nums2[:]  # Avoid modifying original input
    
    for num in nums1:
        if num in nums2_copy:
            result.append(num)
            nums2_copy.remove(num)  # Remove one occurrence
    
    return result


"""
Brute Force Complexity Analysis:

Time Complexity: O(n * m)
- `num in nums2_copy` → O(m)
- remove() → O(m)
- Total: O(n * m)

Space Complexity: O(m)
- Copy of nums2
"""


# ============================================================
# 7. Follow-up Questions (Interview Level)
# ============================================================

"""
Q1: What if the arrays are already sorted?
A1:
- Use Two Pointers:
  - i, j start at 0
  - Compare nums1[i] and nums2[j]
  - Move pointers accordingly
- Time: O(n + m)
- Space: O(1)

--------------------------------------------------

Q2: What if nums1 is much smaller than nums2?
A2:
- Build hash map on smaller array
- Iterate over larger array
- Reduces memory footprint

--------------------------------------------------

Q3: What if data is too large to fit into memory?
A3:
- Use external sorting (disk-based)
- Or chunk processing + hashing
- Or MapReduce approach:
  - Map: count frequencies
  - Reduce: compute intersection
"""

# ============================================================
# 8. Edge Cases Checklist
# ============================================================

"""
- Empty input → return []
- One array empty → return []
- Single element arrays
- All elements same
- No intersection
- Large inputs
"""

# ============================================================
# 9. Mistakes to Avoid
# ============================================================

"""
- Ignoring duplicate counts ❌
- Using `in` repeatedly → O(n^2) ❌
- Modifying input arrays unintentionally
- Not handling empty inputs
- Overcomplicating instead of using hashmap
"""

# ============================================================
# 10. Final Takeaways
# ============================================================

"""
- This is a classic Frequency Map problem.
- Interviewers test:
  - Understanding of duplicates
  - Efficient lookup (hashing)
  - Ability to optimize brute force

Key Insight:
👉 Whenever counts/duplicates matter → Think HASH MAP

Also remember:
- Sorting + Two Pointers is a strong alternative
- Choose approach based on constraints
"""
