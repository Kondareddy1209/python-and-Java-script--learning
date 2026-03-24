"""
Problem: Close Strings

Two strings are considered "close" if:
1. They have the same set of characters
2. Their character frequencies can be rearranged to match

This implementation uses dictionaries (no Counter).
"""


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Step 1: If lengths are different → cannot be close
        if len(word1) != len(word2):
            return False
        
        # Step 2: Create frequency dictionaries
        dici1 = {}
        dici2 = {}
        
        # Count frequency of characters in word1
        for i in word1:
            if i in dici1:
                dici1[i] += 1
            else:
                dici1[i] = 1
                
        # Count frequency of characters in word2
        for i in word2:
            if i in dici2:
                dici2[i] += 1
            else:
                dici2[i] = 1
        
        # Step 3: Check if both words have same unique characters
        # If not → cannot transform one into another
        if set(dici1.keys()) != set(dici2.keys()):
            return False
        
        # Step 4: Compare sorted frequency values
        # Order doesn't matter, only distribution matters
        return sorted(dici1.values()) == sorted(dici2.values())


# -----------------------------------
# Example Test Cases
# -----------------------------------
if __name__ == "__main__":
    sol = Solution()
    
    print(sol.closeStrings("abc", "bca"))        # True
    print(sol.closeStrings("aabb", "bbcc"))      # False
    print(sol.closeStrings("cabbba", "abbccc"))  # True