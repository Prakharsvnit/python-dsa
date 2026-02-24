"""
1. LeetCode Link
https://leetcode.com/problems/majority-element/

2. DSA Pattern
- Hashing (Frequency Counting)
- Boyer–Moore Voting Algorithm
- Array Traversal

------------------------------------------------------------
3. Brute Force Solution
(Hash Map / Frequency Counting)
------------------------------------------------------------
"""

class SolutionBruteForce:
    def majorityElement(self, nums):
        counts = {}

        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        for key, value in counts.items():
            if value > len(nums) // 2:
                return key


"""
4. Time and Space Complexity (Brute Force)

Time Complexity: O(n)

Step-by-step reasoning:
- First loop runs n times → O(n)
- Second loop iterates over unique elements.
  In worst case (all elements distinct), dictionary size = n.
  So second loop = O(n)

Total = O(n) + O(n) = O(n)

Space Complexity: O(n)

Reason:
- In worst case (all elements different), dictionary stores n entries.
- So extra space grows linearly with input size.

------------------------------------------------------------
5. Optimal Solution
(Boyer–Moore Voting Algorithm)
------------------------------------------------------------

def majorityElement(nums):
    counts = {}
    major = nums[0]
    max_count = 0

    for num in nums:
        counts[num] = counts.get(num, 0) + 1

        if counts[num] > max_count:
            max_count = counts[num]
            major = num

    return major

class SolutionOptimal:
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate



6. Time and Space Complexity (Optimal)

Time Complexity: O(n)

Step-by-step reasoning:
- We traverse the array once.
- Each element is processed exactly once.
- No nested loops.
- No repeated scanning.

Total = O(n)

Space Complexity: O(1)

Reason:
- We only store two variables:
    count
    candidate
- No data structure grows with input size.
- Memory usage remains constant regardless of n.

------------------------------------------------------------
7. Follow-up Questions (With Answers)

Q1: What if the problem does NOT guarantee a majority element?
A:
- After Boyer-Moore pass, run a second pass to verify:
    count occurrences of candidate.
- Return candidate only if count > n//2.
- Otherwise return -1 (or raise error).

Q2: Can this be solved using sorting?
A:
Yes.
- Sort the array.
- Return nums[n//2].
Time: O(n log n)
Space: O(1) or O(n) depending on sort implementation.

Q3: Why does Boyer–Moore work?
A:
- Majority element appears more than n/2 times.
- Pairing different elements cancels them out.
- Majority element survives because it has more occurrences
  than all other elements combined.

Q4: Can this extend to elements appearing more than n/3 times?
A:
Yes.
- Modified Boyer-Moore.
- Keep two candidates and two counters.

------------------------------------------------------------
8. Edge Cases

- nums has only 1 element → return that element.
- nums has all identical elements.
- nums has majority element at the beginning.
- nums has majority element at the end.
- Large input size.
- If majority not guaranteed → must verify.

------------------------------------------------------------
9. Mistakes to Avoid

- Forgetting to verify candidate when majority isn't guaranteed.
- Returning most frequent element instead of checking > n//2.
- Using unnecessary extra passes.
- Not handling empty input (if constraints allow it).
- Confusing this with "find element appearing most times".

------------------------------------------------------------
"""