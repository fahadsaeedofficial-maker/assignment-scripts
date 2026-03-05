"""
Simple Data Analysis Script
Author: Fahad Saeed
Date: 2026

Description:
This script performs a very basic analysis on a small dataset.
It calculates the average value from a list of numbers and prints the result.

Purpose:
This script is created as part of an academic assignment to demonstrate
a simple, well-documented and citable piece of code hosted on GitHub.
"""

# Example dataset (could represent scores, user ratings, etc.)
data = [10, 15, 20, 25, 30]


def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.

    Parameters:
    numbers (list): A list containing numerical values.

    Returns:
    float: The average of the numbers.
    """
    
    total = sum(numbers)
    count = len(numbers)
    
    average = total / count
    return average


# Run the function
avg = calculate_average(data)

# Print the result
print("Dataset:", data)
print("Average value:", avg)