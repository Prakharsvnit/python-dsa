# Two Pointers & Sliding Window Patterns

## TWO POINTERS PATTERN

Using two pointers/indices to traverse data structure(s) instead of nested loops, reducing time complexity from O(n²) to O(n).

### Types

#### Type A: Opposite Direction
Both pointers start at opposite ends and move toward each other.

#### Type B: Same Direction
Both pointers start at the same end, one moves faster than the other.

#### Type C: Different Arrays
One pointer per array (useful in merging).

---

## SLIDING WINDOW PATTERN

Maintain a window (subarray/substring) that slides through the array while keeping track of window properties. Optimizes problems asking for "contiguous elements".

### Types

#### Type A: Fixed Size Window

#### Type B: Dynamic Size Window

---

## When to Use TWO POINTERS

✅ Array/string is **sorted** (opposite direction)  
✅ Need to find **pairs** with certain property  
✅ Need to **partition/remove** elements in-place  
✅ Comparing elements from **two arrays**  

**Keywords:** "pair", "triplet", "sorted array", "remove duplicates", "partition"

---

## When to Use SLIDING WINDOW

✅ Deal with **contiguous** subarrays/substrings  
✅ Keywords: "subarray", "substring", "consecutive", "window of size K"  
✅ Need to find **max/min/longest/shortest** in subarrays  
✅ Looking for **optimal range**  

**Keywords:** "longest", "shortest", "maximum sum", "minimum length", "contains", "K size"