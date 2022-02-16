# Author: Esteban Cajamarca
# GitHub username: EstebanCajamarca
# Date: 2/15/2022
# Write a function named square_list that
# takes as a parameter a list of numbers and replaces each value with the square of that value. It should not return
# anything - it should mutate the original list.


def square_list(nums):
    """Returns squared value for every term in list."""
    for i in range(len(nums)):
        # Actions is repeated for every single value in list.
        nums[i] = nums[i] ** 2  # Squaring value.


"""Test
nums = [7, -3, 12, 9]
square_list(nums)
print(nums)"""
