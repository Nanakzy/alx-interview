#!/usr/bin/python3
"""prime game"""


def is_prime(num):
    """Checks if a number is prime."""
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


def find_and_remove_prime(nums):
    """Finds a prime in nums and removes it with its multiples."""
    for i in range(2, len(nums)):
        if is_prime(nums[i]):
            prime = nums[i]
            nums[i] = 0  # Mark as removed
            for j in range(i + prime, len(nums), prime):
                nums[j] = 0  # Remove multiples
            return prime
    return None


def isWinner(x, nums):
    """Determines the winner of the Prime Game."""
    maria_wins, ben_wins = 0, 0
    for _ in range(x):
        if not nums:
            ben_wins += 1
            continue
        prime = find_and_remove_prime(nums)
        if prime:
            maria_wins += 1
        else:
            ben_wins += 1
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


if __name__ == "__main__":
    x = int(input("Enter the number of rounds: "))
    nums = list(map(int, input("Enter the integers (separated by spaces): ").split()))
    winner = isWinner(x, nums)
    print("Winner:", winner)
