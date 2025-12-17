def second_largest(lst):
    lst.sort()  # Sort the list in ascending order
    return lst[-2]  # Return the second last element (the second largest)

# Example usage
numbers = [1, 5, 3, 9, 2]
print(second_largest(numbers))  # Output: 5
