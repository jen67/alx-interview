#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n: int) -> int:
    """Calculate the minimum number of operations needed to
    get n 'H' characters.

    Args:
        n (int): The target number of 'H' characters.

    Returns:
        int: Minimum number of operations required. Returns 0
        if n is not achievable.
    """
    if n <= 1:
        return 0
        operations = 0
    factor = 2
    # Perform prime factorization
    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1
    return operations
