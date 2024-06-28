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

    triangle = [[1]]  # Start with the first row

    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]  # First element of the new row is always 1

        # Generate the interior elements of the row
        for j in range(1, len(prev_row)):
            new_row.append(prev_row[j - 1] + prev_row[j])

        new_row.append(1)  # Last element of the new row is always 1
        triangle.append(new_row)

    return triangle


# Test the function with the provided script
if __name__ == "__main__":
    def print_triangle(triangle):
        for row in triangle:
            print("[{}]".format(",".join([str(x) for x in row])))

    print_triangle(pascal_triangle(5))
