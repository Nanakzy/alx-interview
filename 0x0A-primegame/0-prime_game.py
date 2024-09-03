#!/usr/bin/python3
"""Prime Game Module

This module defines functions for simulating the Prime Game, where two
players, Maria and Ben, take turns removing primes and their multiples
from a list of numbers. The winner is determined by the player who forces
the other player to have no valid moves.
"""

def is_prime(num):
    """Checks if a number is prime.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
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
    """Removes a prime and all its multiples from a list.

    Args:
        nums (list): The list of numbers.
        prime (int): The prime number to remove along with its multiples.

    Modifies:
        nums (list): The list is modified in place, removing the prime
                     and its multiples.
    """
    nums[:] = [n for n in nums if n % prime != 0]


def play_round(n):
    """Simulates one round of the Prime Game.

    Args:
        n (int): The maximum number in the list to play with.

    Returns:
        bool: True if Maria wins the round, False if Ben wins.
    """
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
    """Determines the overall winner of the Prime Game after x rounds.

    Args:
        x (int): The number of rounds to be played.
        nums (list): A list of integers representing the maximum number
                     in the list for each round.

    Returns:
        str: "Maria" if Maria wins more rounds, "Ben" if Ben wins more
             rounds, or None if it's a tie.
    """
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
