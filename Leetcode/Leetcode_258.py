"""
📌 Problem: Add Digits (LeetCode)

Given an integer num, repeatedly add all its digits until the result has only one digit.

------------------------------------------------------------
🧠 APPROACH 1: Digital Root (Math Formula)
------------------------------------------------------------
Formula:
    result = 1 + (num - 1) % 9   (if num != 0)
    result = 0                   (if num == 0)

✅ Time Complexity: O(1)
✅ Space Complexity: O(1)

💡 Why it works:
- Digital root repeats every 9
- %9 gives pattern but fails for multiples of 9
- So we shift using (num - 1) and +1

------------------------------------------------------------
🧠 APPROACH 2: Recursion (Simulation)
------------------------------------------------------------
Steps:
1. Convert number to string
2. Add digits
3. Repeat until single digit

✅ Time Complexity: O(log n)
✅ Space Complexity: O(log n) (recursive stack)

------------------------------------------------------------
📊 EXAMPLE:
Input: num = 38

Process:
38 → 3 + 8 = 11
11 → 1 + 1 = 2

Output: 2
------------------------------------------------------------
"""


class Solution:
    # --------------------------------------------------------
    # 🚀 Approach 1: Digital Root (Optimal)
    # --------------------------------------------------------
    def addDigits_math(self, num: int) -> int:
        """
        Returns single digit using math formula
        """
        if num == 0:
            return 0
        return 1 + (num - 1) % 9

    # --------------------------------------------------------
    # 🔁 Approach 2: Recursive Approach
    # --------------------------------------------------------
    def addDigits_recursive(self, num: int) -> int:
        """
        Returns single digit by recursively summing digits
        """
        n = str(num)

        # Base cases
        if len(n) == 0:
            return 0
        if len(n) == 1:
            return int(n)

        # Sum digits
        s = 0
        for i in range(len(n)):
            s += int(n[i])

        # Recursive call
        return self.addDigits_recursive(s)


# ------------------------------------------------------------
# 🧪 Testing / Workflow Section
# ------------------------------------------------------------
if __name__ == "__main__":
    sol = Solution()

    test_cases = [0, 5, 9, 10, 18, 38, 99, 1234]

    print("📌 Testing Add Digits Problem\n")

    for num in test_cases:
        math_result = sol.addDigits_math(num)
        recursive_result = sol.addDigits_recursive(num)

        print(f"Input: {num}")
        print(f"Math Approach Output      : {math_result}")
        print(f"Recursive Approach Output : {recursive_result}")
        print("-" * 40)


"""
------------------------------------------------------------
🔄 WORKFLOW SUMMARY

1. Choose approach:
   - Fast → use math formula
   - Learning → use recursion

2. For recursion:
   - Convert number → string
   - Add digits
   - Repeat until single digit

3. For math:
   - Direct formula gives answer instantly

------------------------------------------------------------
🎯 FINAL RECOMMENDATION

Use this in interviews:
    return 0 if num == 0 else 1 + (num - 1) % 9

------------------------------------------------------------
"""