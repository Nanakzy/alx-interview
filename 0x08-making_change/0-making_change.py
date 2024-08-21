#!/usr/bin/python3
"""0-making_change"""


def makeChange(coins, total):
    """ Generate changes needed to reach total
    Args: coins and total """
    if total <= 0:
        return 0
    check = 0
    temp = 0
    # Initialize DP array with a value greater than the possible minimum coins
    coins.sort(reverse=True)
    for i in coins:
        while check < total:
            check += i
            temp += 1
        if check == total:
            return temp
        check -= i
        temp -= 1
    return -1
