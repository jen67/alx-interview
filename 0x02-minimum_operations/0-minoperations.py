#!/usr/bin/python3
""" Minimum Operations """

def minOperations(n: int) -> int:
    """Calculate the minimum number of operations needed to get n 'H' characters.

    Args:
        n (int): The target number of 'H' characters.

    Returns:
        int: Minimum number of operations required. Returns 0 if n is not achievable.
    """
    
    # If n is less than or equal to 1, it's impossible to achieve
    if n <= 1:
        return 0
    
    op = 0  # Operation count
    factor = 2  # Start checking for factors from 2

    # Factorization loop
    while n > 1:
        while n % factor == 0:  # Check if factor divides n
            op += factor  # Count the operations (copy + paste)
            n //= factor  # Reduce n by its factor
        factor += 1  # Move to the next potential factor

    return op
