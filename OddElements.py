"""
TASK: Find all odd occurring elements in an array

STEPS
Define function to find odd occurring elements
Use a hash table to track the count of each element
Iterate over the dictionary to identify elements with an odd count
"""

def odd_occurring_elements(arr):
    count_dict = {}
    odd_occurring = []

    # Count occurrences of each element
    for num in arr:
        count_dict[num] = count_dict.get(num, 0) + 1

    # Check for odd occurrences
    for num, count in count_dict.items():
        if count % 2 != 0:
            odd_occurring.append(num)

    return odd_occurring

# Example:
array = [1, 2, 3, 2, 3, 1, 3, 4, 5, 4, 5]
odd_occurrences = odd_occurring_elements(array)
print(f"Odd occuring elements: {odd_occurrences}")