// Reverse Entire Array ([1,2,3,4] → [4,3,2,1]).

function reverseArrayBrute(arr) {
  let n = arr.length;
  let rev = new Array(n);
  for (let i = 0; i < n; i++) {
    rev[i] = arr[n - 1 - i];
  }
  return rev;
}

// Time Complexity: O(n),Space Complexity: O(n)

// | Step                   | Operation         | Complexity |
// | ---------------------- | ----------------- | ---------- |
// | Loop through array     | O(n)              | O(n)       |
// | Extra array allocation | Stores n elements | O(n)       |
