class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        """
        LeetCode 921 - Minimum Add to Make Parentheses Valid

        Approach:
        - Use a stack to keep track of unmatched opening parentheses '('.
        - Traverse each character in the string:
            1. If the character is '(', push it onto the stack.
            2. If the character is ')':
                - If the stack is not empty, pop one '(' as it forms a valid pair.
                - Otherwise, increment 'count' because an extra '(' is needed.
        - After the traversal, any remaining '(' in the stack require matching ')'.

        Return:
        - count + len(stack)
          where:
            count      -> number of unmatched ')'
            len(stack) -> number of unmatched '('

        Example:
        Input: s = "()))(("

        Traversal:
        '(' -> push
        ')' -> pop
        ')' -> stack empty -> count = 1
        ')' -> stack empty -> count = 2
        '(' -> push
        '(' -> push

        Result:
        count = 2
        len(stack) = 2
        Answer = 2 + 2 = 4

        Time Complexity: O(n)
            - Each character is processed once.

        Space Complexity: O(n)
            - In the worst case, the stack stores all opening parentheses.
        """

        count = 0
        stack = []

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(s[i])
            else:
                if stack:
                    stack.pop()
                else:
                    count += 1

        return count + len(stack)