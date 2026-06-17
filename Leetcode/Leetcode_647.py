"""
LeetCode 647. Palindromic Substrings

Problem:
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

Examples:
Input: s = "abc"
Output: 3
Explanation:
Palindromic substrings: "a", "b", "c"

Input: s = "aaa"
Output: 6
Explanation:
Palindromic substrings:
"a", "a", "a", "aa", "aa", "aaa"

--------------------------------------------------
Approach 1: Brute Force
--------------------------------------------------
Generate all possible substrings and check whether
each substring is a palindrome.

Algorithm:
1. Iterate through all possible starting indices.
2. Iterate through all possible ending indices.
3. Extract the substring.
4. Check if the substring equals its reverse.
5. Increment the count if it is a palindrome.

Time Complexity: O(n³)
- O(n²) substrings
- O(n) palindrome check

Space Complexity: O(n)
- Substring creation and reversal

--------------------------------------------------
Approach 2: Expand Around Center (Optimal)
--------------------------------------------------
Every palindrome has a center.

For each index:
1. Expand around a single character (odd-length palindrome).
2. Expand around two consecutive characters (even-length palindrome).
3. Count all valid palindromes during expansion.

Time Complexity: O(n²)
Space Complexity: O(1)

This is the expected interview solution.
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        Counts all palindromic substrings using
        Expand Around Center.

        Args:
            s (str): Input string

        Returns:
            int: Number of palindromic substrings
        """
        count = 0

        def expand(left: int, right: int) -> None:
            """
            Expands from the center while the substring
            remains a palindrome.
            """
            nonlocal count

            while (
                left >= 0
                and right < len(s)
                and s[left] == s[right]
            ):
                count += 1
                left -= 1
                right += 1

        for i in range(len(s)):
            # Odd-length palindromes
            expand(i, i)

            # Even-length palindromes
            expand(i, i + 1)

        return count


# --------------------------------------------------
# Example Usage
# --------------------------------------------------
if __name__ == "__main__":
    sol = Solution()

    print(sol.countSubstrings("abc"))   # Output: 3
    print(sol.countSubstrings("aaa"))   # Output: 6
    print(sol.countSubstrings("racecar"))  # Output: 10


# --------------------------------------------------
# Dry Run
# --------------------------------------------------
"""
Input:
s = "aaa"

Index 0:
expand(0,0) -> "a"
Count = 1

expand(0,1) -> "aa"
Count = 2

Index 1:
expand(1,1) -> "a", "aaa"
Count = 4

expand(1,2) -> "aa"
Count = 5

Index 2:
expand(2,2) -> "a"
Count = 6

Output:
6
"""


# --------------------------------------------------
# Interview Follow-Ups
# --------------------------------------------------
"""
Q1. Can we solve it in O(n)?
Answer:
Yes, using Manacher's Algorithm.

Time Complexity: O(n)
Space Complexity: O(n)

However, Expand Around Center is preferred in
most coding interviews due to simplicity.

Q2. Difference between:
- Longest Palindromic Substring (LeetCode 5)
- Palindromic Substrings (LeetCode 647)

LeetCode 5:
Return the longest palindrome.

LeetCode 647:
Return the total count of palindromic substrings.

Q3. Why check both (i, i) and (i, i+1)?

(i, i)     -> Odd-length palindromes
Examples:
"a", "aba", "racecar"

(i, i+1)   -> Even-length palindromes
Examples:
"aa", "abba"
"""