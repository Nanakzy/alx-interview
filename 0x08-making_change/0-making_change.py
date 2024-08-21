#!/usr/bin/python3

def makeChange(coins, total):
    if total <= 0:
        return 0
    # Initialize DP array with a value greater than the possible minimum coins
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed for total 0
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[total] if dp[total] != float('inf') else -1
