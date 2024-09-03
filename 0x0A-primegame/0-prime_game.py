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


def play_round(n):
    """Plays one round of the game."""
    nums = list(range(1, n + 1))
    maria_turn = True

    while True:
        prime_found = False
        for num in nums:
            if is_prime(num):
                remove_prime_and_multiples(nums, num)
                prime_found = True
                break

        if not prime_found:
            return not maria_turn

        maria_turn = not maria_turn


def isWinner(x, nums):
    """Determines the overall winner of the Prime Game."""
    maria_wins, ben_wins = 0, 0

    for n in nums:
        if play_round(n):
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
