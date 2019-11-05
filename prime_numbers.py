# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

""" Prime Numbers example """

import time

def is_prime(N):
    """ Checks if a given number N is prime or not
    
    Args:
        N : int - Input number
    Returns:
        output : bool - True if N is prime, False if N is not a prime number """
    
    for num in range(2, round(N**0.5)+1):
        if N % num == 0:
            return False
    return True

def prime_check(N):
    """ Returns the numbers under N which are prime numbers 
    
    Args:
        N : int - Input number till which the prime numbers will be returned
    Returns:
        output : list of prime numbers less than N """
    output = []
    for num in range(2, N+1):
        if is_prime(num):
            output.append(num)
    return output

start_time = time.time()
op2 = prime_check(1000000)
print("Time taken for execution of 1000000 is {} seconds".format(time.time() - start_time))

# Time taken for execution of 1000000 is 4.331751346588135 seconds