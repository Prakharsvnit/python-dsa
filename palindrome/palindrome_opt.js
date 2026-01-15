// Given an string, return true if is a palindrome, and false otherwise.

function isPalindrome(s) {
  let l = 0, r = s.length - 1;
  while (l < r) {
    if (s[l] !== s[r]) return false;
    l++;
    r--;
  }
  return true;
}

// Time Complexity - O(n), Space Complexity - O(n)

// while (l < r) The loop runs until the two pointers meet in the middle.
// In each iteration:Compares two characters → O(1). Moves l forward and r backward → O(1)
// Since both pointers move one step per iteration, total iterations ≈ n / 2. simplifies to O(n).

// if (s[l] !== s[r]) return false. Comparison is constant time per iteration → O(1). 
// In the worst case (no mismatch), full scan = O(n)