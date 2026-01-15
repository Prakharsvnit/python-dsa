// Given an string, return true if is a palindrome, and false otherwise.

function isPalindrome(s) {
  return s === s.split('').reverse().join('');
}

// Time Complexity - O(n), Space Complexity - O(n)

// 1️) s.split('') - Converts the string into an array of characters. "abc" → ["a", "b", "c"]
// Time Complexity: O(n) → must visit each character once.
// Space Complexity: O(n) → creates a new array of n elements.

// 2) .reverse() - Reverses the array in-place. ["a", "b", "c"] → ["c", "b", "a"]
// Time Complexity: O(n) → swaps about n/2 pairs.
//Space Complexity: O(1) → reversed in-place, no extra data structure.

// 3) .join('') - Joins array back into a string.["c", "b", "a"] → "cba"
// Time Complexity: O(n) → must read each array element once.
// Space Complexity: O(n) → creates a new string of length n.

// 4️) s === ... Compares the two strings character by character.
// Time Complexity: O(n) (worst case, when all characters are same).
// Space Complexity: O(1)