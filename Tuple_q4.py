# Tuple with a list as an element (mutable)
my_tuple = ([1, 2, 3], "hello", 5)

# Modify the list inside the tuple
my_tuple[0].append(4)  # Adding 4 to the list inside the tuple

print(my_tuple)  # Output: ([1, 2, 3, 4], 'hello', 5)
