# 904. Fruit Into Baskets

## Approach: Sliding Window + Hash Map

We use a sliding window to maintain a contiguous subarray that contains at most **2 distinct fruit types**.

- Expand the window by moving the `right` pointer.
- Store the frequency of fruits inside the current window using a hash map.
- If the window contains more than 2 fruit types, shrink it from the left until only 2 types remain.
- Track the maximum valid window length throughout the process.

## Code

```python
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        from collections import defaultdict

        left = 0
        max_fruits = 0
        basket = defaultdict(int)

        # Expand the window using the right pointer
        for right in range(len(fruits)):
            basket[fruits[right]] += 1

            # Shrink the window if more than 2 fruit types exist
            while len(basket) > 2:
                basket[fruits[left]] -= 1

                # Remove fruit type if its count becomes 0
                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]

                left += 1

            # Update the maximum valid window size
            max_fruits = max(max_fruits, right - left + 1)

        return max_fruits
```

## How It Works

### Example

```python
fruits = [1, 2, 1, 2, 3]
```

| Left | Right | Window         | Distinct Fruits | Max Length |
|--------|---------|---------------|----------------|------------|
| 0 | 0 | [1] | 1 | 1 |
| 0 | 1 | [1, 2] | 2 | 2 |
| 0 | 2 | [1, 2, 1] | 2 | 3 |
| 0 | 3 | [1, 2, 1, 2] | 2 | 4 |
| 0 | 4 | [1, 2, 1, 2, 3] | 3 | Invalid |
| 3 | 4 | [2, 3] | 2 | 4 |

The longest valid subarray containing at most 2 distinct fruit types is:

```python
[1, 2, 1, 2]
```

So the answer is:

```python
4
```

## Time Complexity

- Each fruit enters the window once and leaves the window once.
- Therefore, both pointers traverse the array at most one time.

**Time Complexity:** `O(n)`

## Space Complexity

- The hash map stores at most 3 fruit types before shrinking the window.

**Space Complexity:** `O(1)`