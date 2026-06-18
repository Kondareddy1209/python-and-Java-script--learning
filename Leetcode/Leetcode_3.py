# 3. Longest Substring Without Repeating Characters

🔗 Problem: https://leetcode.com/problems/longest-substring-without-repeating-characters/

## Problem Statement

Given a string `s`, find the length of the longest substring without repeating characters.

### Example 1

```text
Input: s = "abcabcbb"
Output: 3

Explanation:
The answer is "abc", with length 3.
```

### Example 2

```text
Input: s = "bbbbb"
Output: 1
```

### Example 3

```text
Input: s = "pwwkew"
Output: 3

Explanation:
The answer is "wke", with length 3.
```

---

# Approach 1: Brute Force (Set)

## Idea

- Start from every index `i`.
- Expand the substring character by character.
- Use a set to keep track of characters already seen.
- If a duplicate character is found, stop expanding.
- Update the maximum length found.

## Code

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0

        for i in range(len(s)):
            seen = set()

            for j in range(i, len(s)):
                if s[j] in seen:
                    break

                seen.add(s[j])
                ans = max(ans, j - i + 1)

        return ans
```

## Complexity Analysis

### Time Complexity: O(n²)

- Outer loop runs `n` times.
- Inner loop may run up to `n` times.
- Set lookup and insertion take `O(1)` on average.

### Space Complexity: O(n)

- The set can store up to `n` unique characters.

---

# Approach 2: Optimal Sliding Window

## Idea

- Maintain a window `[left, right]`.
- Expand the window by moving `right`.
- If a character repeats, shrink the window from the left until the duplicate is removed.
- Keep track of the maximum window size.

## Code

```python
from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = defaultdict(int)

        left = 0
        ans = 0

        for right in range(len(s)):
            freq[s[right]] += 1

            while freq[s[right]] > 1:
                freq[s[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans
```

## Complexity Analysis

### Time Complexity: O(n)

- Each character enters the window once.
- Each character leaves the window at most once.

### Space Complexity: O(n)

- Hash map stores character frequencies.

---

# Approach 3: Optimized HashMap (Last Seen Index)

## Idea

Instead of shrinking one character at a time:

- Store the last index where each character appeared.
- If a duplicate is found inside the current window, directly move `left`.
- This avoids unnecessary iterations.

## Code

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}

        left = 0
        ans = 0

        for right, ch in enumerate(s):
            if ch in last_seen and last_seen[ch] >= left:
                left = last_seen[ch] + 1

            last_seen[ch] = right
            ans = max(ans, right - left + 1)

        return ans
```

## Complexity Analysis

### Time Complexity: O(n)

- Each character is processed once.

### Space Complexity: O(n)

- Dictionary stores the last occurrence of characters.

---

# Comparison

| Approach | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Brute Force (Set) | O(n²) | O(n) |
| Sliding Window (Frequency Map) | O(n) | O(n) |
| Last Seen Index (Best) | O(n) | O(n) |

## Key Takeaway

- **Brute Force** is easy to understand but inefficient.
- **Sliding Window** is the standard interview solution.
- **Last Seen Index HashMap** is the most optimized and commonly preferred solution in coding interviews.