# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 19:42:05 2019

@author: Rohith_Vemulapally
"""

""" To check if a given list of numbers are odd numbers 
    Similar for even numbers
    """

#import random

def odd_numbers(num_list):
    """ Filters out odd numbers from a given list 
    
    Args:
        num_list : list - List of numbers
    Returns:
        output : list - List of odd numbers from the num_list """
    
    output = []
    
    for num in num_list:
        if num % 2 != 0:
            output.append(num)
    return output

if __name__ == "__main__":
    num_list = [46, 41, 2, 52, 4, 81, 8, 17, 78, 38]
    # Above result from [random.randint(1, 100) for _ in range(10)]
    odd_num_list = odd_numbers(num_list)
    
    # Below is using filter function in Python
    odd_num_list_filter = list(filter(lambda x : x % 2 != 0, num_list))
    
    print('Yayyy!') if odd_num_list == odd_num_list_filter else print('Alas!!')
    