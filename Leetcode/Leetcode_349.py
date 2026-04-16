"""
===========================================================
📌 Problem: Intersection of Two Arrays
===========================================================

Given two integer arrays nums1 and nums2,
return an array of their intersection.

Each element in the result must be UNIQUE.

-----------------------------------------------------------
🧠 APPROACH 1: BRUTE FORCE (Using "in")
-----------------------------------------------------------

Idea:
- Loop through nums1
- Check if element exists in nums2
- Also check if it's already added to result (avoid duplicates)

-----------------------------------------------------------
⏱ Time Complexity:
- O(n * m)  → because "in nums2" is O(m)

📦 Space Complexity:
- O(1) (excluding output)

-----------------------------------------------------------
⚠️ Drawback:
- Slow for large inputs
- Repeated searching
"""


from typing import List


class SolutionBruteForce:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []

        for i in nums1:
            # Check if element exists in nums2 AND not already in result
            if i in nums2 and i not in res:
                res.append(i)

        return res


"""
-----------------------------------------------------------
🧠 APPROACH 2: TWO POINTERS (OPTIMIZED)
-----------------------------------------------------------

Idea:
1. Sort both arrays
2. Use two pointers (i, j)
3. Compare elements:
    - If equal → add to result
    - If smaller → move that pointer
4. Avoid duplicates using res[-1]

-----------------------------------------------------------
⏱ Time Complexity:
- Sorting: O(n log n + m log m)
- Traversal: O(n + m)
- Overall: O(n log n + m log m)

📦 Space Complexity:
- O(1) (excluding output)

-----------------------------------------------------------
✅ Advantage:
- Efficient
- No repeated searching
- Uses sorted property smartly
"""


class SolutionTwoPointers:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Step 1: Sort arrays
        nums1.sort()
        nums2.sort()

        i, j = 0, 0
        res = []

        # Step 2: Traverse both arrays
        while i < len(nums1) and j < len(nums2):

            # Case 1: Match found
            if nums1[i] == nums2[j]:
                # Avoid duplicates
                if not res or res[-1] != nums1[i]:
                    res.append(nums1[i])

                i += 1
                j += 1

            # Case 2: nums1 is smaller → move i
            elif nums1[i] < nums2[j]:
                i += 1

            # Case 3: nums2 is smaller → move j
            else:
                j += 1

        return res


"""
===========================================================
🔍 DRY RUN EXAMPLE
===========================================================

nums1 = [4,1,2,2]
nums2 = [2,2,3]

After sorting:
nums1 = [1,2,2,4]
nums2 = [2,2,3]

Step-by-step:
i=0, j=0 → 1 < 2 → i++
i=1, j=0 → 2 == 2 → add 2
i=2, j=1 → 2 == 2 → skip duplicate
i=3, j=2 → 4 > 3 → j++

Result: [2]

===========================================================
🧠 KEY LEARNING
===========================================================

✔ Brute Force:
- Easy to understand
- Slow

✔ Two Pointers:
- Uses sorting
- Moves intelligently
- Avoids unnecessary comparisons

-----------------------------------------------------------
🔥 INTERVIEW TIP:

If asked:
👉 "Optimize time" → Use Hashing
👉 "Optimize space" → Use Two Pointers
👉 "Explain logic clearly" → Use this approach

===========================================================
🚀 END OF FILE
===========================================================
"""