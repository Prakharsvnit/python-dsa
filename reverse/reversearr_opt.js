// Reverse Entire Array ([1,2,3,4] → [4,3,2,1]).

function reverseArrayOptimized(arr) {
  let l = 0, r = arr.length - 1;
  while (l < r) {
    [arr[l], arr[r]] = [arr[r], arr[l]];
    l++;
    r--;
  }
  return arr;
}

// Time Complexity: O(n),Space Complexity: O(n)

// | Step                     | Operation     | Complexity |
// | ------------------------ | ------------- | ---------- |
// | Two-pointer swaps        | O(n/2) ≈ O(n) | O(n)       |
// | In-place, no extra array | O(1) space    | O(1)       |
