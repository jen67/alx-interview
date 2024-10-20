#!/usr/bin/python3
"""
Main file
"""

def minOperations(n):
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

