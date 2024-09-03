#!/usr/bin/python3
"""Prime game"""


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


def remove_prime_and_multiples(nums, prime):
    """Removes a prime and its multiples from the list."""
    nums[:] = [n for n in nums if n % prime != 0]


def isWinner(x, nums):
    """Determines the winner of the Prime Game."""
    maria_wins, ben_wins = 0, 0

    for round in range(x):
        current_nums = list(range(1, max(nums) + 1))  # Reset nums each round
        maria_turn = True

        while True:
            prime_found = False
            for n in current_nums:
                if is_prime(n):
                    remove_prime_and_multiples(current_nums, n)
                    prime_found = True
                    break

            if not prime_found:
                if maria_turn:
                    ben_wins += 1
                else:
                    maria_wins += 1
                break

            maria_turn = not maria_turn

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None
