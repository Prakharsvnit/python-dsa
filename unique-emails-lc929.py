"""
1. LeetCode Link
https://leetcode.com/problems/unique-email-addresses/

Problem: 929. Unique Email Addresses
"""


"""
2. DSA Pattern
- String Manipulation
- Hashing (Set for uniqueness)
- Simulation
"""


"""
3. Brute Force Solution (Interview-Friendly)

Idea:
- For each email:
    - Split into local and domain
    - Process local part manually character by character
    - Ignore everything after '+'
    - Skip '.'
    - Build normalized string
- Store in a list
- At the end, convert list to set and return its length
"""


def numUniqueEmails_bruteforce(emails):
    normalized_emails = []

    for email in emails:
        local, domain = email.split("@")

        cleaned_local = ""
        for char in local:
            if char == "+":
                break
            if char == ".":
                continue
            cleaned_local += char

        normalized_emails.append(cleaned_local + "@" + domain)

    return len(set(normalized_emails))


"""
4. Time and Space Complexity of Brute Force

Let:
n = number of emails
m = average length of each email

Step-by-step:

Outer loop runs n times → O(n)

For each email:
- Splitting by '@' takes O(m)
- Iterating through local part takes O(m)
- Building cleaned string takes O(m)

So per email cost = O(m)

Total time = O(n * m)

Space Complexity:
- normalized_emails list stores n emails → O(n * m)
- set conversion also stores up to n unique emails → O(n * m)

Total space = O(n * m)
"""


"""
5. Optimal Solution (Interview-Friendly)

Optimization:
- Use a set directly instead of list
- Use string operations efficiently
- Avoid unnecessary storage
"""


def numUniqueEmails_optimal(emails):
    unique_emails = set()

    for email in emails:
        local, domain = email.split("@", 1)
        local = local.split("+", 1)[0]
        local = local.replace(".", "")
        unique_emails.add(local + "@" + domain)

    return len(unique_emails)


"""
6. Time and Space Complexity of Optimal

Let:
n = number of emails
m = average length of each email

Step-by-step:

For each email:
- split("@", 1) → O(m)
- split("+", 1) → O(m)
- replace(".", "") → O(m)

Each email processing = O(m)

Total time = O(n * m)

Space Complexity:
- set stores up to n normalized emails → O(n * m)

Total space = O(n * m)

Difference from brute force:
- Avoids extra list
- Cleaner logic
- Slightly more memory efficient
"""


"""
7. Follow-up Questions with Answers

Q1: What if domain rules also required normalization?
A:
    Apply similar transformation logic to domain before inserting into set.

Q2: Can we solve this without extra space?
A:
    If input can be modified:
        - Normalize in-place
        - Sort emails → O(n log n)
        - Count unique adjacent
    Space: O(1) (if sorting in-place allowed)

Q3: What if emails are extremely large (millions)?
A:
    - Process as streaming input
    - Avoid storing unnecessary intermediate lists
    - Set storage is unavoidable if counting unique

Q4: Why use split("@", 1) instead of split("@")?
A:
    It prevents errors if more than one '@' appears and avoids unnecessary splitting.
"""


"""
8. Edge Cases

- emails = [] → return 0
- All emails identical → return 1
- No '+' or '.' in local → should still work
- '+' at first position in local
- Local part entirely removed after '+' (e.g., "+abc@x.com")
- Large input size
"""


"""
9. Mistakes to Avoid

- Modifying domain part (rules apply only to local part)
- Forgetting to break after '+'
- Using list instead of set for uniqueness
- Not using maxsplit in split
- Over-optimizing with unreadable one-liners
- Ignoring edge cases like empty input
"""