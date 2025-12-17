def remove_duplicates(lst):
    result = []
    for item in lst:
        if item not in result:  # Only add item if it's not already in result
            result.append(item)
    return result

# Example usage
numbers = [1, 2, 3, 2, 4, 5, 1]
print(remove_duplicates(numbers))  # Output: [1, 2, 3, 4, 5]
