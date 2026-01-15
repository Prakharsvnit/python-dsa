// Given an array of integers ,and `target`, return *indices* of the two numbers such that they add up to `target`.
// Use a HASHMAP to store number → index while traversing.For each element, check if (target - current) already exists in the map.

function twoSum(nums, target) {
  const map = new Map();
  for (let i = 0; i < nums.length; i++) {
    const complement = target - nums[i];
    if (map.has(complement)) {
      return [map.get(complement), i];
    }
    map.set(nums[i], i);
  }
}

// ==============X==============X==============X==============X==============X==============X==============X==============X==============

// Time Complexity: O(n),Space Complexity: O(n)

// | Step                      | Operation                   | Time Complexity |
// | ------------------------- | --------------------------- | ------------------ |
// | Single loop through array | Iterating all elements once | **O(n)**           | 
// | Hash lookup (`map.has()`) | Check if complement exists  | **O(1)** (average) | 
// | Hash insert (`map.set()`) | Store current element       | **O(1)** (average) | 

// Space Complexity - Uses a hash map that may store up to n elements.O(n)
