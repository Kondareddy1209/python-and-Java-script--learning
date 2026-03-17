# max_vowels.py

"""
Problem:
Find the maximum number of vowels in any substring of length k.

This file includes:
1. Brute Force Approach (for understanding)
2. Sliding Window Approach (optimal)

Author: Your Name
"""

class Solution:

    # ------------------------------------------------------------
    # 🔴 Method 1: Brute Force Approach (O(n * k))
    # ------------------------------------------------------------
    def maxVowels_bruteforce(self, s: str, k: int) -> int:
        """
        Logic:
        - Check every substring of size k
        - Count vowels in each substring
        - Keep track of maximum
        
        Time Complexity: O(n * k)
        Space Complexity: O(1)
        """

        vowels = {'a', 'e', 'i', 'o', 'u'}
        max_count = 0

        # Loop through all possible starting indices
        for i in range(len(s) - k + 1):
            count = 0

            # Check substring of length k
            for j in range(i, i + k):
                if s[j] in vowels:
                    count += 1

            # Update maximum vowels found
            max_count = max(max_count, count)

        return max_count


    # ------------------------------------------------------------
    # 🟢 Method 2: Sliding Window Approach (O(n)) ✅ Optimal
    # ------------------------------------------------------------
    def maxVowels(self, s: str, k: int) -> int:
        """
        Logic:
        - Maintain a window of size k
        - Add right character (r)
        - Remove left character (l) when window exceeds size k
        - Track vowel count dynamically
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        vowels = {'a', 'e', 'i', 'o', 'u'}
        count = 0      # current number of vowels in window
        max_count = 0  # result
        l = 0          # left pointer

        # Iterate through string using right pointer
        for r in range(len(s)):

            # Step 1: Add current character to window
            if s[r] in vowels:
                count += 1

            # Step 2: If window size exceeds k, shrink from left
            if r - l + 1 > k:
                if s[l] in vowels:
                    count -= 1
                l += 1

            # Step 3: If window size is exactly k, update answer
            if r - l + 1 == k:
                max_count = max(max_count, count)

        return max_count


# ------------------------------------------------------------
# 🧪 Test the implementation
# ------------------------------------------------------------
if __name__ == "__main__":
    sol = Solution()

    s = "abciiidef"
    k = 3

    print("Input:", s, "k =", k)
    print("Brute Force Output:", sol.maxVowels_bruteforce(s, k))
    print("Sliding Window Output:", sol.maxVowels(s, k))