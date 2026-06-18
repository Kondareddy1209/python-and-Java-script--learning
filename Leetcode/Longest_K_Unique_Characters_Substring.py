# Longest K Unique Characters Substring

🔗 Problem: https://www.geeksforgeeks.org/problems/longest-k-unique-characters-substring0853/1

## Problem Statement

Given a string `s` and an integer `k`, find the length of the longest substring with exactly `k` unique characters.

If no such substring exists, return `-1`.

### Example 1

```text
Input: s = "aabacbebebe", k = 3
Output: 7

Explanation:
The longest substring with exactly 3 distinct characters is
"cbebebe", whose length is 7.
```

### Example 2

```text
Input: s = "aaaa", k = 2
Output: -1

Explanation:
No substring contains exactly 2 distinct characters.
```

---

# Approach 1: Brute Force (Set)

## Idea

- Start from every index `i`.
- Use a set to store distinct characters in the current substring.
- Expand the substring using index `j`.
- If distinct characters exceed `k`, stop expanding.
- Whenever distinct characters become exactly `k`, update the answer.

## Code

```python
class Solution:
    def longestKSubstr(self, s, k):
        ans = -1

        for i in range(len(s)):
            seen = set()

            for j in range(i, len(s)):
                seen.add(s[j])

                if len(seen) > k:
                    break

                if len(seen) == k:
                    ans = max(ans, j - i + 1)

        return ans
```

## Complexity Analysis

### Time Complexity: O(n²)

- Outer loop runs `n` times.
- Inner loop may run up to `n` times.
- Set insertion and lookup take `O(1)` on average.

### Space Complexity: O(k)

- The set stores at most `k` distinct characters before breaking.

---

# Approach 2: Sliding Window + HashMap (Optimal)

## Idea

- Maintain a sliding window `[left, right]`.
- Use a hashmap to store character frequencies.
- Expand the window by moving the right pointer.
- If the number of distinct characters exceeds `k`, shrink the window from the left.
- Whenever the window contains exactly `k` distinct characters, update the maximum length.

## Code

```python
from collections import defaultdict

class Solution:
    def longestKSubstr(self, s, k):
        left = 0
        ans = -1
        freq = defaultdict(int)

        for right in range(len(s)):
            freq[s[right]] += 1

            while len(freq) > k:
                freq[s[left]] -= 1

                if freq[s[left]] == 0:
                    del freq[s[left]]

                left += 1

            if len(freq) == k:
                ans = max(ans, right - left + 1)

        return ans
```

## Complexity Analysis

### Time Complexity: O(n)

- Each character enters the window once.
- Each character leaves the window at most once.

### Space Complexity: O(k)

- HashMap stores frequencies of at most `k` distinct characters.

---

# Dry Run

```text
s = "aabacbebebe"
k = 3
```

| Right | Window | Distinct Characters | Length |
|---------|---------|-------------------|---------|
| 0 | a | 1 | - |
| 1 | aa | 1 | - |
| 2 | aab | 2 | - |
| 3 | aaba | 2 | - |
| 4 | aabac | 3 | 5 |
| 5 | aabacb | 3 | 6 |
| 6 | cbeb | 3 | 4 |
| 10 | cbebebe | 3 | 7 |

Answer = **7**

---

# Comparison

| Approach | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Brute Force (Set) | O(n²) | O(k) |
| Sliding Window + HashMap | O(n) | O(k) |

## Key Takeaway

- Brute force generates all possible substrings and checks distinct characters.
- Sliding Window efficiently maintains a valid substring with exactly `k` unique characters.
- The optimal solution runs in **O(n)** time and is the expected interview approach.