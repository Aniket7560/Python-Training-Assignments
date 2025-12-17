# Two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union: All elements from both sets
union = set1 | set2  # or set1.union(set2)
print("Union:", union)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

# Intersection: Common elements between both sets
intersection = set1 & set2  # or set1.intersection(set2)
print("Intersection:", intersection)  # Output: {4, 5}

# Difference: Elements in set1 but not in set2
difference = set1 - set2  # or set1.difference(set2)
print("Difference (set1 - set2):", difference)  # Output: {1, 2, 3}

# Symmetric Difference: Elements that are in either set, but not both
symmetric_difference = set1 ^ set2  # or set1.symmetric_difference(set2)
print("Symmetric Difference:", symmetric_difference)  # Output: {1, 2, 3, 6, 7, 8}
