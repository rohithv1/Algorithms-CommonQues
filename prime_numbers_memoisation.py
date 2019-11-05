# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 22:39:28 2019

@author: Rohith_Vemulapally
"""

""" Prime Numbers with memoisation technique """

import time

prime_numbers = []

def is_prime(N):
    """ Checks if a given number N is prime or not
    
    Args:
        N : int - Input number
    Returns:
        output : bool - True if N is prime, False if N is not a prime number """
    
    global prime_numbers
    
    last_num = prime_numbers[-1] if prime_numbers else 0
    
    if N < last_num:
        if N in prime_numbers:
            return True
        else:
            return False
    
    sqrt = round(N ** 0.5)
    for num in prime_numbers:
        if sqrt >= num:
            if N % num == 0:
                return False
        else:
            break
    prime_numbers.append(N)
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
op1 = prime_check(1000000)
print("Time taken for execution of 1000000 is {} seconds".format(time.time() - start_time))

# Time taken for execution of 1000000 is 1.4432706832885742 seconds



    