class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Function to check whether a given string is a palindrome.
        
        A palindrome reads the same forward and backward.
        This solution ignores non-alphanumeric characters
        and is case-insensitive.
        
        Example:
        Input: "A man, a plan, a canal: Panama"
        Output: True
        """

        # Step 1: Clean the string
        # Keep only alphanumeric characters and convert to lowercase
        cleaned = ""
        for ch in s:
            if ch.isalnum():          # check if character is letter or digit
                cleaned += ch.lower() # convert to lowercase and append

        # Step 2: Use two-pointer technique to check palindrome
        left = 0
        right = len(cleaned) - 1

        while left < right:
            if cleaned[left] != cleaned[right]:
                return False  # mismatch found → not a palindrome
            left += 1
            right -= 1

        return True  # all characters matched


# -----------------------------
# Time and Space Complexity
# -----------------------------

# Time Complexity: O(n)
# - We traverse the string once to clean it → O(n)
# - We traverse again using two pointers → O(n)
# - Overall: O(n)

# Space Complexity: O(n)
# - We create a new string 'cleaned' → O(n)