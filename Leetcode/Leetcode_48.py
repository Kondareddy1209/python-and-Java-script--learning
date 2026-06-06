# Rotate Image (90 degrees clockwise)
# LeetCode 48

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

n = len(matrix)

# Step 1: Transpose the matrix
# Convert rows into columns by swapping matrix[i][j] with matrix[j][i]
for i in range(n):
    for j in range(i + 1, n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

# Matrix after transpose:
# [
#   [1, 4, 7],
#   [2, 5, 8],
#   [3, 6, 9]
# ]

# Step 2: Reverse each row
# This completes the 90-degree clockwise rotation
for i in range(n):
    matrix[i].reverse()

# Final matrix:
# [
#   [7, 4, 1],
#   [8, 5, 2],
#   [9, 6, 3]
# ]

print(matrix)