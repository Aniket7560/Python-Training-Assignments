# Two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Remove common elements from both sets (intersection)
set1 = set1 - set2  # Remove common elements from set1
set2 = set2 - set1  # Remove common elements from set2

print("Set1 after removing common elements:", set1)  # Output: {1, 2, 3}
print("Set2 after removing common elements:", set2)  # Output: {6, 7, 8}
