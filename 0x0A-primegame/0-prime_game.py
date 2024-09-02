#!/usr/bin/python3

def sieve_of_eratosthenes(max_n):
    primes = [True] * (max_n + 1)
    p = 2
    while p * p <= max_n:
        if primes[p]:
            for i in range(p * p, max_n + 1, p):
                primes[i] = False
        p += 1
    primes[0] = primes[1] = False  # 0 and 1 are not prime numbers
    return primes


def calculate_prime_moves(max_n, primes):
    prime_moves = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_moves[i] = prime_moves[i - 1]
        if primes[i]:
            prime_moves[i] += 1
    return prime_moves


def isWinner(x, nums):
    if x <= 0 or not nums:
        return None

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)
    prime_moves = calculate_prime_moves(max_n, primes)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_moves[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
