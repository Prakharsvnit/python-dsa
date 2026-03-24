# ============================================================
# 1. LeetCode Link / Problem Description
# ============================================================

# Problem Link:
# https://leetcode.com/problems/intersection-of-two-arrays/

"""
Problem Summary:

Given two integer arrays nums1 and nums2, return an array of their intersection.

Each element in the result must be UNIQUE.
You may return the result in ANY order.

Example:
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

Output: [9,4]  (order does not matter)

Important Notes:
- Result must contain UNIQUE elements.
- Even if an element appears multiple times, it should appear only once in the result.
"""


# ============================================================
# 2. DSA Pattern Identification
# ============================================================

"""
Primary Pattern:
Hashing / Set Lookup

Why this pattern applies:
- We need to quickly check whether elements from one array exist in another.
- A set provides O(1) average lookup time.
- Since the output must contain unique elements, sets are naturally suited.

Typical Approach:
1. Convert one array to a set.
2. Iterate over the other array.
3. Add matches to the result set.

Alternative Patterns:
1. Sorting + Two Pointers
   - Sort both arrays.
   - Use two pointers to find matches.
   - Useful when memory constraints restrict extra space.

2. Binary Search
   - Sort one array.
   - For each element in the other array perform binary search.

However, the Hash Set approach is the most optimal and simplest here.
"""


# ============================================================
# 3. Interview Critique of My Solution
# ============================================================

"""
Logic & Accuracy
----------------
Your approach:
1. Identify the larger array.
2. Iterate through the smaller array.
3. Check membership in the larger array.
4. Store results in a set.

This works correctly for the problem constraints.

However, there are inefficiencies:
- "num in greater" is O(n) because greater is a list.
- This results in nested scanning.

Better solution:
Convert the larger list into a set first.

Example:
greater_set = set(greater)

Then membership becomes O(1).

Complexity Analysis
-------------------

Your Implementation:

For each element in lesser:
    membership check in greater list

If:
n = len(nums1)
m = len(nums2)

Worst case:

Time Complexity:
O(n * m)

Because:
Each membership check scans the list.

Space Complexity:
O(k)

Where k is size of the intersection result.


Code Quality
------------

Strengths:
- Clean structure
- Correct use of set for unique values
- Easy to understand

Improvements:
- Variable names could be clearer
    greater -> larger_array
    lesser -> smaller_array

- Missing optimization: set conversion

- No input validation (optional but good practice)


Edge Cases
----------

Your code works for most cases but consider:

1. One array empty
2. Both arrays empty
3. Large inputs
4. All duplicates
5. No intersection
"""


# ============================================================
# 4. My Original Solution (As Provided)
# ============================================================

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

def intersec_arr(nums1,nums2):
    ptr = 0
    result_set = set()
    greater = max(nums1, nums2, key=len)
    lesser = min(nums1, nums2, key=len)
    
    for num in lesser:
        if num in greater:
            result_set.add(num)
    
    return list(result_set)
        

    
print(intersec_arr(nums1,nums2))

# ============================================================
# 6. Optimal Solution (Interview Accepted Version)
# ============================================================

"""
Key Optimization:
Convert one array to a set to allow O(1) membership checks.

Steps:
1. Convert nums1 to a set.
2. Iterate through nums2.
3. If element exists in set, add to result set.
4. Return result list.

We use sets twice:
- One for fast lookup
- One to maintain unique intersection
"""

def intersection_optimal(nums1, nums2):

    lookup_set = set(nums1)   # O(n)
    intersection = set()

    for num in nums2:         # O(m)
        if num in lookup_set: # O(1)
            intersection.add(num)

    return list(intersection)


# Example run
print("Optimal:", intersection_optimal(nums1, nums2))


"""
Optimal Complexity Analysis:

Time Complexity: O(n + m)

Step-by-step:
- Building set from nums1 → O(n)
- Iterating nums2 → O(m)
- Each lookup → O(1)

Total = O(n + m)


Space Complexity: O(n + k)

Where:
n = size of set(nums1)
k = intersection size
"""


# ============================================================
# 7. Follow-up Questions (Interview Level)
# ============================================================

"""
Q1: What if the arrays are extremely large and cannot fit into memory?

A1:
Use External Sorting or Streaming.

Approach:
1. Sort both arrays using external sort.
2. Use two-pointer technique to find intersections.

This reduces memory usage and allows disk-based processing.


------------------------------------------------------------

Q2: What if duplicates must be preserved?
(LeetCode 350 - Intersection of Two Arrays II)

Example:
nums1 = [1,2,2,1]
nums2 = [2,2]

Output:
[2,2]

Solution:
Use a hashmap frequency counter.

Algorithm:
1. Count frequency in nums1
2. Iterate nums2
3. If count > 0, add to result and decrement

Time Complexity: O(n + m)


------------------------------------------------------------

Q3: What if the arrays are already sorted?

A3:

Use Two Pointers.

Algorithm:
1. i = 0, j = 0
2. Compare nums1[i] and nums2[j]
3. Move pointers accordingly.

Example:

while i < n and j < m:
    if nums1[i] == nums2[j]:
        add to result
        i += 1
        j += 1
    elif nums1[i] < nums2[j]:
        i += 1
    else:
        j += 1

Time Complexity: O(n + m)
Space Complexity: O(1) extra
"""


# ============================================================
# 8. Edge Cases Checklist
# ============================================================

"""
Always test:

1. Empty arrays
nums1 = []
nums2 = []

2. One empty
nums1 = [1,2,3]
nums2 = []

3. Single element
nums1 = [1]
nums2 = [1]

4. No intersection
nums1 = [1,2,3]
nums2 = [4,5,6]

5. All duplicates
nums1 = [2,2,2]
nums2 = [2,2]

6. Large arrays
Up to problem constraints
"""


# ============================================================
# 9. Mistakes to Avoid
# ============================================================

"""
1. Forgetting uniqueness requirement
   (Using list instead of set)

2. Using list membership checks repeatedly
   O(n) instead of O(1)

3. Sorting unnecessarily
   Adds O(n log n)

4. Overcomplicating solution
   Hash sets solve it directly

5. Returning duplicates accidentally
"""


# ============================================================
# 10. Final Takeaways
# ============================================================

"""
What Interviewers Are Testing:

1. Recognition of Hash Set pattern
2. Understanding of membership complexity
3. Ability to optimize brute force solutions
4. Writing clean, readable code


Key Insight:

Whenever you see:

- "Find common elements"
- "Check membership quickly"
- "Return unique values"

Think:

SET LOOKUP


This pattern appears in:

- Two Sum
- Contains Duplicate
- Longest Consecutive Sequence
- Intersection problems
- Graph visited sets


Rule of Thumb:

If repeated membership checks are needed,
convert the structure to a SET.
"""