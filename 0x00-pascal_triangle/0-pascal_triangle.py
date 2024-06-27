#!/usr/bin/python3


def pascal_triangle(n):
    """
    This function generates Pascal's triangle up to a specified (n).

    Args:
      n: An integer representing the number of rows in the Pascal's triangle.

    Returns:
      A list of lists of integers representing the Pascal's triangle.
      Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            prev_row = triangle[i - 1]
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)
        triangle.append(row)

    return triangle
