#!/usr/bin/python3
'''Module to find Pascal's Triangle integers'''


def pascal_triangle(n):
    '''
    Function to generate Pascal's Triangle up to the nth row

        Parameters:
            n (int): The number of rows of Pascal's triangle

        Returns:
            list: A list of lists representing Pascal's Triangle
    '''
    triangle = []

    if n <= 0:
        return triangle

    for row_num in range(n):
        # Start with a row of 1s
        row = [1] * (row_num + 1)
        
        # Compute the values for the interior cells of the row
        for j in range(1, row_num):
            row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]
        
        # Append the row to the triangle
        triangle.append(row)

    return triangle


# Example usage
if __name__ == "__main__":
    n = 5
    print(pascal_triangle(n))

