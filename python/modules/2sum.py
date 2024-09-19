def find_sum(arr, target):
    """
    Find a pair of numbers in the array that sum up to the target value.
    
    Args:
    arr (list): A list of unique integers.
    target (int): The target sum value.
    
    Returns:
    tuple: A tuple (num1, num2) of two numbers from the array whose sum equals the target,
           or None if no such pair exists.
    """
    # Create a set to keep track of the numbers we have seen
    seen = set()

    # Iterate over the array
    for num in arr:
        # Calculate the complement (target - current number)
        complement = target - num
        
        # If the complement exists in the set, we've found a pair
        if complement in seen:
            return (complement, num)  # Return the pair as a tuple
        
        # Add the current number to the set of seen numbers
        seen.add(num)
    
    # If no pair is found, return None
    return None

# Example usage:
arr = [1, 2, 3, 4, 5]
target = 8

result = find_sum(arr, target)
print(result)  
