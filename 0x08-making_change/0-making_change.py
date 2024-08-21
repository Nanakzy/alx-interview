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
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed for total 0
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[total] if dp[total] != float('inf') else -1
