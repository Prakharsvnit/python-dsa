// Given an array of integers ,and `target`, return *indices* of the two numbers such that they add up to `target`.

function twoSum(nums, target) {
  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      if (nums[i] + nums[j] === target) {
        return [i, j];
      }
    }
  }
}

// Time Complexity: O(n^2),Space Complexity: O(1)

// | Step       | Operation                         | Complexity |
// | ---------- | --------------------------------- | ---------- |
// | Outer loop | runs `n` times                    | O(n)       |
// | Inner loop | runs up to `n` times for each `i` | O(n)       |
// | Comparison | Constant time per iteration       | O(1)       |
// | **Total**  |                                   | **O(n^2)** |

// Space Complexity: Uses only loop counters (i, j).Complexity = O(1)

// ==============X==============X==============X==============X==============X==============X==============X==============X==============


// Solve the following variations of twosum with brute force,opt approach;time,space complexity

// 1) Two Sum II – Input Array Is Sorted 
// Given a **1-indexed** array of integers `numbers` that is already **sorted in non-decreasing order**, find two numbers such that they add up to a specific `target` number.
// Return the indices of the two numbers, `index1` and `index2`,

// 2) Count Pairs With Given Sum
// Given an array of integers `arr[]` and an integer `k`,
// return the **number of distinct pairs (i, j)** such that `arr[i] + arr[j] == k` and `i < j`.