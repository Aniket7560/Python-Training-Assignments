import copy

# Original list with inner lists (mutable elements)
original_list = [[1, 2], [3, 4], [5, 6]]

# Shallow copy: It copies the outer list but not the inner lists
shallow_copied_list = copy.copy(original_list)

# Deep copy: It copies both the outer list and the inner lists
deep_copied_list = copy.deepcopy(original_list)

# Modify the original list to show how shallow and deep copies behave
original_list[0][0] = 99

print("Original List:", original_list)  # Output: [[99, 2], [3, 4], [5, 6]]
print("Shallow Copy:", shallow_copied_list)  # Output: [[99, 2], [3, 4], [5, 6]]
print("Deep Copy:", deep_copied_list)  # Output: [[1, 2], [3, 4], [5, 6]]
