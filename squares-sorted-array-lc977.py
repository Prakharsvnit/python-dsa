# ============================================================
# 1. LeetCode Link / Problem Description
# ============================================================

# Problem Link:
# https://leetcode.com/problems/squares-of-a-sorted-array/description/

"""
Problem Summary:

Given an integer array nums sorted in non-decreasing order,
return an array of the squares of each number sorted in non-decreasing order.

Example:
Input:  [-4, -1, 0, 3, 10]
Output: [0, 1, 9, 16, 100]

Explanation:
Squaring the numbers gives:
[16, 1, 0, 9, 100]

But this is not sorted.
So we must return the squares in sorted order.
"""

# ============================================================
# 2. DSA Pattern Identification
# ============================================================

"""
Core Pattern:
Two Pointers (from both ends)

Why this pattern applies:

The array is already sorted by value, but NOT by absolute value.
Negative numbers when squared may become larger than positive numbers.

Example:
[-7, -3, 2, 3, 11]

Squares:
[49, 9, 4, 9, 121]

Largest squares will come from the numbers with the largest absolute value,
which are located at the beginning OR the end of the array.

Therefore:
We compare:
abs(left) vs abs(right)

Whichever is larger contributes the next largest square.

We fill the result array from the BACK.

Alternative Pattern:
- Brute force + sorting
- Transform then sort

However:
Sorting after squaring adds an unnecessary O(n log n) step.

Two-pointer solution achieves O(n).
"""

# ============================================================
# 3. Interview Critique of My Solution
# ============================================================

"""
Your Solution:

def sortsd(nums):
    nums = [num**2 for num in nums]
    return sorted(nums)

Logic & Accuracy
----------------

Your logic is correct.

Steps:
1. Square every element
2. Sort the result

This produces the correct answer.

However:
You ignored a key constraint in the problem:

The input array is ALREADY SORTED.

A strong candidate should recognize that we can leverage
this property to avoid sorting again.

Complexity Analysis
-------------------

Step 1: List comprehension
O(n)

Step 2: Sorting
O(n log n)

Total Time Complexity:
O(n log n)

Space Complexity:
O(n)

- New list created
- Sorting may use additional memory

Optimal solution can achieve:

Time Complexity: O(n)
Space Complexity: O(n)

Code Quality
------------

Pros:
- Clean
- Readable
- Pythonic

Cons:
- Function name "sortsd" is unclear
- Not descriptive

Better name:
sorted_squares()

Interview Acceptability
-----------------------

This solution would PASS in most interviews.

However:
Interviewers may ask:

"Can you do better than sorting?"

At that point they expect the two-pointer solution.

Edge Cases
----------

Your solution handles:

✔ negative numbers
✔ zero
✔ duplicates
✔ single element

No major logical failures.
"""

# ============================================================
# 4. My Original Solution (As Provided)
# ============================================================

def sortsd(nums):
    nums = [num**2 for num in nums]
    return sorted(nums)

# ============================================================
# 5. Brute Force Solution (Interview Friendly)
# ============================================================

"""
Idea:

1. Square every number
2. Store results
3. Sort the array

This is the most straightforward solution.

A candidate could derive this quickly in an interview.
"""

def sorted_squares_bruteforce(nums):
    result = []

    # Square each element
    for num in nums:
        result.append(num * num)

    # Sort the squared numbers
    result.sort()

    return result


"""
Brute Force Complexity Analysis:

Time Complexity: O(n log n)

Step 1: Squaring loop
O(n)

Step 2: Sorting
O(n log n)

Total:
O(n log n)

Space Complexity: O(n)

We store the squared numbers in a new list.
"""

# ============================================================
# 6. Optimal Solution (Interview Accepted Version)
# ============================================================

"""
Key Insight:

Largest square comes from the number with the largest absolute value.

Since the array is sorted:
- Left side contains large negative numbers
- Right side contains large positive numbers

Compare absolute values from both ends.

Build result array from the back.
"""

nums = [-7,-3,2,3,11]

def sorted_squares(arr):
    left = 0
    right = len(arr) - 1
    result = [0] * len(arr)
    pos = len(arr) - 1
    
    while left <= right:
        
        if abs(arr[left]) > abs(arr[right]):
            result[pos] = arr[left] ** 2
            left += 1
        else:
            result[pos] = arr[right] ** 2
            right -= 1
        
        pos -= 1
        
    return result
    
print(sorted_squares(nums))


"""
Optimal Complexity Analysis:

Time Complexity: O(n)

Each element is processed exactly once.

We move either:
left pointer OR right pointer each iteration.

Total iterations = n.

Space Complexity: O(n)

We create a new result array of size n.

Note:
Some languages may require this space.
In Python this is standard for this problem.
"""

# ============================================================
# 7. Follow-up Questions (Interview Level)
# ============================================================

"""
Q1: What if the array was NOT sorted?

A1:

Then the two-pointer strategy would not work.

We would need:

Option 1:
Square everything then sort
Time: O(n log n)

Option 2:
Use a heap or balanced tree
Still around O(n log n)

Sorting becomes unavoidable.

------------------------------------------------------------

Q2: Can we do this in-place?

A2:

In-place is difficult because:

Squaring changes the ordering relationship.

Example:
[-5, -3, -1, 4]

Squaring:
[25, 9, 1, 16]

The values must be rearranged heavily.

Thus:
A separate result array is the cleanest solution.

------------------------------------------------------------

Q3: What if the input size is extremely large (millions)?

A3:

Two-pointer solution is still optimal.

Reasons:
- Single pass O(n)
- Sequential memory access (cache friendly)
- No sorting overhead

For extremely large data streams:
You might process chunks if memory constrained.

But algorithmic complexity remains O(n).
"""

# ============================================================
# 8. Edge Cases Checklist
# ============================================================

"""
Important edge cases:

✔ Empty input
[]

✔ Single element
[5]

✔ All negative numbers
[-9, -7, -3]

✔ All positive numbers
[1, 2, 3]

✔ Many zeros
[0, 0, 0]

✔ Mixed with large negatives
[-10000, -3, 0, 5]

✔ Maximum constraint size
10^5 elements
"""

# ============================================================
# 9. Mistakes to Avoid
# ============================================================

"""
Common pitfalls:

1. Forgetting that squaring changes order.

Example mistake:
Returning squared array without sorting.

2. Using absolute values but forgetting to square.

3. Two-pointer but filling result from the front instead of back.

This breaks ordering.

4. Off-by-one errors in pointer movement.

5. Overengineering with heaps or trees when two pointers suffice.
"""

# ============================================================
# 10. Final Takeaways
# ============================================================

"""
What interviewers are really testing:

1. Pattern Recognition

Recognize that:
Largest square comes from largest absolute value.

2. Ability to optimize

Move from:
O(n log n) -> O(n)

3. Two Pointer Mastery

This pattern appears in many problems:

- Container With Most Water
- Two Sum (sorted)
- 3Sum
- Remove Duplicates from Sorted Array
- Merge Sorted Arrays

Key Insight:

Whenever a problem involves:
"sorted array" + "extreme values"

Think:
TWO POINTERS.
"""

# ============================================================
# Quick Local Test
# ============================================================

if __name__ == "__main__":

    nums = [-4, -1, 0, 3, 10]

    print("Original:", nums)

    print("Your Solution:", sortsd(nums))
    print("Brute Force:", sorted_squares_bruteforce(nums))
    print("Optimal:", sorted_squares_optimal(nums))