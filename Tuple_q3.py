# Tuple of numbers
numbers = (5, 2, 9, 5, 7, 5)

# Element to count
element = 5
count = 0

# Loop through the tuple to count occurrences
for num in numbers:
    if num == element:
        count += 1

print(f"The element {element} occurs {count} times.")  # Output: 3
