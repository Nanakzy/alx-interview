#!/usr/bin/python3
"""
Module: 0-minoperations
"""


def minOperations(n: int) -> int:
    """
    Calculates the fewest number of operations needed to
    result in exactly n H characters.

    Args:
        n (int): The desired number of H characters.

    Returns:
        int: The minimum number of operations required.
        Returns 0 if n is impossible to achieve.
    """
    if n <= 1:
        return 0

    operations = [float('inf')] * (n + 1)
    operations[1] = 0

    for i in range(2, n + 1):
        for j in range(1, i // 2 + 1):
            if i % j == 0:
                operations[i] = min(operations[i], operations[j] + (i // j))

                return operations[n]
