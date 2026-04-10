class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        PROBLEM:
        --------
        Given a string `s` consisting of words and spaces,
        return the length of the last word.

        A word is defined as a sequence of non-space characters.

        --------------------------------------------------------
        APPROACH:
        ---------
        1. Traverse the string from the end (right → left).
        2. Ignore trailing spaces.
        3. Start counting characters when the first letter is found.
        4. Stop when a space is encountered after counting starts.
        5. Return the count.

        WHY THIS WORKS:
        ---------------
        - The last word is located at the end of the string.
        - Traversing backward avoids splitting the string (efficient).
        - Handles edge cases like trailing spaces.

        --------------------------------------------------------
        EXAMPLE:
        --------
        Input: s = "Hello World  "

        Step-by-step:
        - Start from end → skip spaces
        - Find 'd' → start counting
        - Count: d(1), l(2), r(3), o(4), W(5)
        - Stop at space

        Output: 5

        --------------------------------------------------------
        TIME COMPLEXITY:
        ----------------
        O(n)
        - We traverse the string once.

        SPACE COMPLEXITY:
        -----------------
        O(1)
        - No extra space used (constant variables only).

        --------------------------------------------------------
        """

        # Length of string
        n = len(s)

        # Variable to store length of last word
        count = 0

        # Flag to indicate we started counting a word
        started = False

        # Traverse from end of string to beginning
        for i in range(n - 1, -1, -1):

            # If character is NOT a space → part of a word
            if s[i] != " ":
                count += 1          # increase word length
                started = True     # mark that word has started

            # If space found AFTER word started → word ended
            elif started:
                break              # stop counting

        # Return length of last word
        return count