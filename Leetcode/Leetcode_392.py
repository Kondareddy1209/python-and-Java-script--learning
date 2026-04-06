class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        LeetCode 392 - Is Subsequence

        Goal:
        Check if string 's' is a subsequence of string 't'.

        A subsequence means:
        Characters of 's' appear in 't' in the same order,
        but not necessarily continuously.
        """

        i = 0  # pointer for string s
        j = 0  # pointer for string t

        # Traverse both strings
        while i < len(s) and j < len(t):

            # If characters match, move pointer of s
            if s[i] == t[j]:
                i += 1

            # Always move pointer of t
            j += 1

        # If we reached end of s, all characters were matched
        return i == len(s)