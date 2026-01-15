// 	Reverse a String ("hello" → "olleh")

function reverseStringOptimized(s) {
  let arr = s.split('');
  let l = 0, r = arr.length - 1;
  while (l < r) {
    [arr[l], arr[r]] = [arr[r], arr[l]];
    l++;
    r--;
  }
  return arr.join('');
}

// Time complexity: O(n), Space complexity: O(n)

// | Step                             | Operation     | Complexity           |
// | -------------------------------- | ------------- | -------------------- |
// | Convert string → array (`split`) | O(n)          | One-time conversion  |
// | Loop through half of array       | O(n/2) ≈ O(n) | Swapping elements    |
// | Join array → string (`join`)     | O(n)          | Final reconstruction |
