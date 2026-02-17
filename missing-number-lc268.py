# 1. LeetCode link
# https://leetcode.com/problems/missing-number/

# 2. DSA Pattern
# - Array
# - Mathematical formula (Sum of first N numbers)
# - Hashing (Set lookup optimization)

# 3. Brute Force Solution (code)

def missingNumber_bruteforce(nums):
    for i in range(len(nums) + 1):
        if i not in nums:   # O(n) lookup each time for array
            return i


# 4. Time & Space (Brute) — explain why
# Time: O(n²)
# - Outer loop runs n times
# - "i not in nums" scans entire list → O(n)
# - So total = n * n = O(n²)
#
# Space: O(1)
# - No extra data structure used


# 5. Better Solution (Using Set)

def missingNumber_set(nums):
    nums_set = set(nums)  # O(n) to build

    for i in range(len(nums) + 1):
        if i not in nums_set:  # O(1) average lookup
            return i


# 7. Time & Space (Set Approach)
# Time: O(n)
# - Building set → O(n)
# - Loop n times with O(1) lookup
# - Total = O(n)
#
# Space: O(n)
# - Extra set storage


# 5 (Optimal). Optimal Solution (Math Formula)

def missingNumber_optimal(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    return expected_sum - sum(nums)


# 7 (Optimal). Time & Space (Optimal) — explain why
# Time: O(n)
# - One pass to compute sum(nums)
#
# Space: O(1)
# - No extra data structure used
#
# Why it works:
# - Sum of numbers from 0 to n = n(n+1)/2
# - Subtracting actual sum gives missing number


# 8. Followup Question
# - Can you solve without extra space? (Use math or XOR)
# - What if numbers are not guaranteed 0..n?
# - What if array is read-only?


# 9. Edge Cases
# - nums = [0] → return 1
# - nums = [1] → return 0
# - Missing number is n (e.g., [0,1,2] → 3)
# - Missing number is 0


# 10. Mistake to Avoid
# - Using "i not in nums" inside loop → O(n²)
# - Forgetting range should go till len(nums) + 1
# - Integer division mistake (use // not /)
# - Ignoring empty input (though constraint usually n >= 1)
