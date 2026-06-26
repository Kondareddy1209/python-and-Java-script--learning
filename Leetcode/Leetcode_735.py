from typing import List

class Solution:
    def asteroidCollision(self, nums: List[int]) -> List[int]:
        """
        LeetCode 735. Asteroid Collision

        Approach:
        ---------
        Use a stack to keep track of asteroids that have survived so far.

        A collision can only occur when:
            - The asteroid on the top of the stack is moving right (+)
            - The current asteroid is moving left (-)

        Cases:
        1. Top asteroid is smaller:
           - Remove it from the stack.
           - Continue checking because the current asteroid may collide
             with previous asteroids.

        2. Both asteroids are equal:
           - Remove the top asteroid.
           - Current asteroid also explodes.
           - Stop processing the current asteroid.

        3. Top asteroid is larger:
           - Current asteroid explodes.
           - Stop processing the current asteroid.

        If the while loop finishes normally (no break),
        the current asteroid survives and is pushed onto the stack.

        Time Complexity:
            O(n)
            Each asteroid is pushed and popped at most once.

        Space Complexity:
            O(n)
            Stack stores the surviving asteroids.
        """

        stack = []

        for asteroid in nums:

            # Collision occurs only when:
            # stack top is moving right (+)
            # current asteroid is moving left (-)
            while stack and stack[-1] > 0 and asteroid < 0:

                # Current asteroid is larger
                if abs(stack[-1]) < abs(asteroid):
                    stack.pop()

                # Both asteroids have equal size
                elif abs(stack[-1]) == abs(asteroid):
                    stack.pop()
                    break

                # Stack top is larger
                else:
                    break

            # Executed only if the while loop did NOT break.
            # This means the current asteroid survived.
            else:
                stack.append(asteroid)

        return stack