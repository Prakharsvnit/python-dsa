"""
Python Lists & Strings — Best Practices Summary

Core rules:
1. Use append() to add ONE item to a list
2. Use extend() or += to add MANY items
3. NEVER build strings using += inside loops
4. Build strings using list + join() for performance
"""

# --------------------------------------------------
# 1. Add ONE item to a list → append()
# --------------------------------------------------

items = []
items.append("apple")
items.append("banana")

# Correct output:
# ['apple', 'banana']


# ❌ Common mistake (adds characters individually)
# items += "apple"
# Result: ['a', 'p', 'p', 'l', 'e']


# --------------------------------------------------
# 2. Build string in loop → ❌ DON'T
# --------------------------------------------------

# ❌ Bad (strings are immutable → O(n^2))
result = ""
for word in ["I", "love", "Python"]:
    result += word + " "

# Works, but inefficient and slow for large data


# --------------------------------------------------
# 3. Build string efficiently → list + join()
# --------------------------------------------------

words = []
for word in ["I", "love", "Python"]:
    words.append(word)

result = " ".join(words)

# Correct output:
# "I love Python"


# --------------------------------------------------
# 4. Add MANY items to a list → extend() or +=
# --------------------------------------------------

a = [1, 2]
b = [3, 4, 5]

a.extend(b)
# a = [1, 2, 3, 4, 5]

# Same behavior
a = [1, 2]
a += [3, 4, 5]


# ❌ Common mistake
a = [1, 2]
a.append([3, 4, 5])
# Result: [1, 2, [3, 4, 5]]


# --------------------------------------------------
# Mental Model (remember this)
# --------------------------------------------------
# append(x)  → add ONE box
# extend(xs) → pour ITEMS from iterable
# += list    → same as extend
# += string  → creates NEW string (slow in loops)


# --------------------------------------------------
# Bonus: String split() with no argument
# arr = s.split() #No argument passed

# Splits on any whitespace(space, tab, newline)
# Ignores leading & trailing spaces

s = "  hello   world  this   is  python  "
arr = s.split()
print(arr) # Output: ['hello', 'world', 'this', 'is', 'python']


