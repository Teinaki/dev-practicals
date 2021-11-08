# Consider the following 3x3 matrix (3 lists of length 3). Create a list
# comprehension which returns a transpose matrix. Use the list comprehension
# to display the expected output.

matrix = [
    [1, 2, 3],
    [4, 5, 6,],
    [7, 8, 9]
]

# Write your solution here
transposed_matrix = [[row[i] for row in matrix] for i in range(3)]

print(transposed_matrix)
# Expected output:
# [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
