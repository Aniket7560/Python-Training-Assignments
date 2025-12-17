nested_list = [[1, 2], [3, 4], [5, 6]]

# For each inner list, calculate the sum and add it to a new list
sums = []
for inner_list in nested_list:
    sums.append(sum(inner_list))

print(sums)  # Output: [3, 7, 11]
