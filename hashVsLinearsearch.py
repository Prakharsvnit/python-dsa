### If `nums` is a **list / array**

```python
if n in nums:
```

* **Time complexity: O(n)**
* Python checks elements **one by one** (linear search)
* Worst case: it scans the entire list

Why?
Lists are stored sequentially in memory, so membership requires comparing `n` with each element until found (or not found).

---

### If `nums` is a **set**

```python
if n in nums:
```

* **Average time complexity: O(1)**
* Implemented using a **hash table**
* Python computes `hash(n)` and directly jumps to the bucket

Why?
Sets use hashing, so lookup is constant time on average.

---

### ⚠️ Important Nuance

For sets:

* **Average case:** O(1)
* **Worst case:** O(n) (rare, due to hash collisions)

But in practice, Python’s hashing makes worst cases extremely uncommon.

---

### Quick Comparison

| Data Structure | Lookup `n in nums` |
| -------------- | ------------------ |
| List           | O(n)               |
| Set            | O(1) average       |
| Dictionary     | O(1) average       |

---


A hash collision happens when:

Two different values produce the same hash index.
When Are Collisions More Likely?
1️⃣ Small table size

If table is almost full → collisions increase.

2️⃣ Bad hash function

If many objects produce similar hashes.