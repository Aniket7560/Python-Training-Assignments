numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = []  # Create an empty list to store even numbers

# Loop through each number and add it if it's even
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print(even_numbers)  # Output: [2, 4, 6, 8]
