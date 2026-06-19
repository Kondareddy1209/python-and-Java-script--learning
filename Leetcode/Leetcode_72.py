"""
LeetCode 76. Minimum Window Substring
=====================================

Problem Statement
-----------------
Given two strings `s` and `t`, return the minimum window substring
of `s` such that every character in `t` (including duplicates)
is included in the window.

If no such substring exists, return an empty string "".

Examples
--------
Input:
    s = "ADOBECODEBANC"
    t = "ABC"

Output:
    "BANC"

Input:
    s = "a"
    t = "a"

Output:
    "a"

Input:
    s = "a"
    t = "aa"

Output:
    ""

Approach
--------
Sliding Window + Frequency Counter

1. Store character frequencies of string `t` using Counter.
2. Expand the right pointer and decrease the required count.
3. Once all characters are found (count == 0):
   - Try shrinking the window from the left.
   - Update the minimum window if a smaller valid window is found.
4. Continue until the entire string is processed.

Key Observation
---------------
Counter values represent how many more occurrences of each character
are still required.

Positive Value  -> Character still needed.
Zero Value      -> Exact requirement satisfied.
Negative Value  -> Extra occurrences present in the current window.

Time Complexity
---------------
O(n)

Each character is visited at most twice:
- Once by the right pointer.
- Once by the left pointer.

Space Complexity
----------------
O(m)

where m = number of unique characters in t.

"""


from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # Edge Case
        if len(s) < len(t):
            return ""

        # Frequency map of characters needed
        n = Counter(t)

        # Left pointer
        l = 0

        # Total characters still needed
        count = len(t)

        # Minimum window length
        ans = float('inf')

        # Starting index of answer
        start = 0

        # Expand window using right pointer
        for i in range(len(s)):

            if s[i] in n:
                n[s[i]] -= 1

                # Required character found
                if n[s[i]] >= 0:
                    count -= 1

            # Valid window found
            while count == 0:

                # Update minimum window
                if i - l + 1 < ans:
                    ans = i - l + 1
                    start = l

                # Remove left character
                if s[l] in n:
                    n[s[l]] += 1

                    # Window becomes invalid
                    if n[s[l]] > 0:
                        count += 1

                l += 1

        if ans == float('inf'):
            return ""

        return s[start:start + ans]


# ============================================================
# Dry Run
# ============================================================

"""
Input:
s = "ADOBECODEBANC"
t = "ABC"

Initial:
n = {'A':1, 'B':1, 'C':1}
count = 3
l = 0

------------------------------------------------------------
i = 0 -> 'A'

n['A'] = 0
count = 2

Window = "A"

------------------------------------------------------------
i = 3 -> 'B'

n['B'] = 0
count = 1

Window = "ADOB"

------------------------------------------------------------
i = 5 -> 'C'

n['C'] = 0
count = 0

Window = "ADOBEC"

Valid Window Found

Length = 6
ans = 6
start = 0

Try Shrinking

Remove 'A'
n['A'] = 1

n['A'] > 0
count = 1

Stop Shrinking

------------------------------------------------------------
Continue Expanding

i = 10 -> 'A'

n['A'] = 0
count = 0

Window Valid Again

Try Shrinking

Remove D
Remove O
Remove B
Remove E

Window = "CODEBA"

Remove C

n['C'] = 1
count = 1

Stop

------------------------------------------------------------
i = 12 -> 'C'

n['C'] = 0
count = 0

Window = "BANC"

Length = 4

ans = 4
start = 9

Try Shrinking

Remove B

n['B'] = 1
count = 1

Stop

------------------------------------------------------------

Answer:
s[9:13]

= "BANC"

Output:
"BANC"
"""

# ============================================================
# Example Usage
# ============================================================

if __name__ == "__main__":
    solution = Solution()

    print(solution.minWindow("ADOBECODEBANC", "ABC"))
    print(solution.minWindow("a", "a"))
    print(solution.minWindow("a", "aa"))


"""
Interview Explanation
---------------------

Why do we decrement n[s[i]]?

Because the character has entered the current window.

Example:
Need:
A : 1

After finding one A:
A : 0

Requirement satisfied.

------------------------------------------------

Why check n[s[i]] >= 0 ?

Because only required occurrences should reduce count.

Example:

Need:
A : 1

Window:
A A A

Counter values:

0
-1
-2

Only the first A contributes toward satisfying t.

------------------------------------------------

Why increment n[s[l]] while shrinking?

Because that character leaves the window.

If its count becomes positive,
the window no longer contains enough copies of that character.

------------------------------------------------

Why does this work in O(n)?

Each character:
- enters the window once
- leaves the window once

Hence total operations are linear.

O(n)
"""