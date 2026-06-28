class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        """
        LeetCode 856 - Score of Parentheses

        Approach (Stack):
        - Use a stack to store the score at each level of nesting.
        - Initialize the stack with 0, representing the score of the
          outermost level.
        - Traverse each character in the string:
            1. If the character is '(':
               - Start a new nested level by pushing 0 onto the stack.
            2. If the character is ')':
               - Pop the score of the current level.
               - If the popped score is 0, it represents "()", whose score is 1.
               - Otherwise, it represents "(A)", whose score is 2 * A.
               - Add the calculated score to the previous level.

        Why stack = [0]?
        - The initial 0 acts as the base level.
        - Every completed parenthesis contributes its score to its parent level.
        - Without this base level, the first completed pair would have
          nowhere to store its score.

        Example:
        Input: s = "(()(()))"

        Stack Evolution:
        Start      -> [0]
        (          -> [0, 0]
        (          -> [0, 0, 0]
        )          -> [0, 1]
        (          -> [0, 1, 0]
        (          -> [0, 1, 0, 0]
        )          -> [0, 1, 1]
        )          -> [0, 3]
        )          -> [6]

        Output: 6

        Time Complexity: O(n)
            - Each character is processed exactly once.

        Space Complexity: O(n)
            - In the worst case, the stack stores one score for each level
              of nested parentheses.
        """

        stack = [0]

        for ch in s:
            if ch == "(":
                stack.append(0)
            else:
                current_score = stack.pop()
                stack[-1] += max(2 * current_score, 1)

        return stack[0]