# 1. LeetCode Link
# https://leetcode.com/problems/ransom-note/

'''
2. DSA Pattern
   --------
   Hashing / Frequency Count
   We count frequencies of characters in magazine and check if ransomNote can be formed.

3. Brute Force Solution (code only)
'''

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Brute force freq count
        freq_mag = {}
        for ch in magazine:
            freq_mag[ch] = freq_mag.get(ch, 0) + 1
        
        # try to use chars for ransomNote
        for ch in ransomNote:
            if ch not in freq_mag or freq_mag[ch] == 0:
                return False
            freq_mag[ch] -= 1
        
        return True


'''
4. Time and Space Complexity of Brute Force

   Let n = len(magazine), m = len(ransomNote).

   Step-by-step:
   - Building freq_mag by iterating magazine:
       O(n) time
       We add at most n entries in worst case (unique chars), so space = O(min(n, k))
       where k = size of alphabet (here 26 lower letters).
   - Looping ransomNote:
       We do m iterations, each dictionary lookup and decrement is O(1) average.
       So time = O(m)
   - Total time = O(n + m)
   - Total space = O(k) where k <= 26 for lowercase alphabet
     (or O(min(n, m)) in a general character set)

   Explanation:
   We read every magazine character once to count it and check every ransom note
   character once; all dictionary ops are average O(1).

5. Optimal Solution (code only)

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # optimal using fixed-size array for lowercase letters
        counts = [0]*26
        
        base = ord('a')
        for ch in magazine:
            counts[ord(ch) - base] += 1
        
        for ch in ransomNote:
            idx = ord(ch) - base
            counts[idx] -= 1
            if counts[idx] < 0:
                return False
        
        return True


'''
6. Time and Space Complexity of Optimal

   Let n = len(magazine), m = len(ransomNote).

   Time:
   - Build letter counts array from magazine: O(n)
   - Check ransomNote against counts: O(m)
   - Total = O(n + m)

   Space:
   - We use a fixed size array of length 26 -> O(1) constant space.
   - We don’t allocate based on input size beyond that.

   Explanation:
   Since alphabet size is fixed (26 lowercase), the array size does not grow
   with input, so space is constant.

7. Follow-up Questions with answers
   ----------------------------------
   Q1: What if magazine includes uppercase or non-alphabetic characters?
   A: We’d expand counts to fit possible characters (e.g., size 52 or use a dict).

   Q2: What if ransomNote and magazine were extremely long (huge inputs)?
   A: The optimal solution is already linear and scales well, no better
       asymptotic exists, but we’d ensure streaming or chunk reading if memory limited.

   Q3: Can we early stop while counting magazine?
   A: We could stop counting magazine only if
       all required ransomNote chars are counted enough, but verifying this
       dynamically complicates logic without big benefit.

8. Edge Cases
   -------------
   • ransomNote empty → always True (no chars needed).
   • magazine empty but ransomNote non-empty → False.
   • magazine and ransomNote same string → True.
   • ransomNote has characters not in magazine → False.
   • Large repeated characters within limits → should return True.

9. Mistakes to Avoid
   --------------------
   • Not decrementing counts properly → may overestimate availability.
   • Using nested loops (e.g., for each ransom char loop magazine) → leads
     to O(m×n) time, too slow.
   • Assuming uppercase behaves same as lowercase without converting/handling.
   • Forgetting to reset frequency for multiple test runs.
'''