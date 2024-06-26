#!/usr/bin/python3

def pascal_triangle(n):
  """
  This function generates Pascal's triangle up to a specified number of rows (n).

  Args:
      n: An integer representing the number of rows in the Pascal's triangle.

  Returns:
      A list of lists of integers representing the Pascal's triangle. Returns an empty list if n <= 0.
  """

  if n <= 0:
    return []

  triangle = [[1]]  # Base case: First row is always [1]

  # Iterate through rows (starting from the second row)
  for i in range(1, n):
    row = [1]  # Each row starts and ends with 1
    # Calculate values for the middle elements using the previous row
    for j in range(1, i):
      prev_row = triangle[i - 1]
      row.append(prev_row[j - 1] + prev_row[j])
    row.append(1)  # Add the last 1
    triangle.append(row)

  return triangle
